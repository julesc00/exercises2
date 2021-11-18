"""
A model example with SQLAlchemy
"""

from sqlalchemy import (asc, Column, Integer, String, ForeignKey, Table, func, desc, and_)
from sqlalchemy.orm import relationship, backref, session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

author_publisher = Table(
    "author_publisher",
    Base.metadata,
    Column("author_id", Integer, ForeignKey("author.author_id")),
    Column("publisher_id", Integer, ForeignKey("publisher.publisher_id")),
)

book_publisher = Table(
    "book_publisher",
    Base.metadata,
    Column("book_id", Integer, ForeignKey("book.book_id")),
    Column("publisher_id", Integer, ForeignKey("publisher.publisher_id")),
)


class Author(Base):
    __tablename__ = "author"
    author_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    books = relationship("Book", backref=backref("author"))
    publishers = relationship("Publisher", secondary=author_publisher, back_populates="authors")


class Book(Base):
    __tablename__ = "book"
    book_id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("author.author_id"))
    title = Column(String)
    publishers = relationship("Publisher", secondary=book_publisher, back_populates="books")


class Publisher(Base):
    __tablename__ = "publisher"
    publisher_id = Column(Integer, primary_key=True)
    name = Column(String)
    authors = relationship("Author", secondary=author_publisher, back_populates="publishers")
    books = relationship("Book", secondary=book_publisher, back_populates="publishers")


# Example of a query
author_book_totals = (
    session.query(
        Author.first_name,
        Author.last_name,
        func.count(Book.title).label("book_total")
    )
    .join(Book)
    .group_by(Author.last_name)
    .order_by(desc("book_total"))
    .all()
)


def main():
    """Main entry point of program."""

    # Connect to the database using SQLAlchemy
    with resources.path("project.data", "author_book_publisher.db") as sqlite_filepath:
        engine = create_engine(f"sqlite:///{sqlite_filepath}")
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()

    # Get the number of books printed by each publisher.
    books_by_publisher = get_books_by_publisher(session, ascending=False)
    for row in books_by_publisher:
        print(f"Publisher: {row.name}, total books: {row.total_books}")

    # Get the number of authors each publisher publishes.
    authors_by_publisher = get_authors_by_publishers(session)
    for row in authors_by_publisher(session):
        print(f"Publisher: {row.name}, total authors: {row.total_authors}")

    # Output hierarchical author data
    authors = get_authors(session)
    output_author_hierarchical(authors)

    # Add a new book
    add_new_book(
        session,
        author_name="Stephen King",
        book_title="The Stand",
        publisher_name="Random House"
    )

    # Output the updated hierarchical author data
    authors = get_authors(session)
    output_author_hierarchical(authors)


def get_books_by_publisher(session, ascending=True):
    """Get a list of publishers and the number of books they've published."""

    if not isinstance(ascending, bool):
        raise ValueError(f"Sorting value invalid: {ascending}")

    direction = asc if ascending else desc

    return (
        session.query(
            Publisher.name, func.count(Book.title).label("total_books")
        )
        .join(Publisher.books)
        .group_by(Publisher.name)
        .order_by(direction("total_books"))
    )


def get_authors_by_publishers(session, ascending=True):
    """Get a list of publishers and the numbers of authors they've published."""

    if not isinstance(ascending, bool):
        raise ValueError(f"Sorting value invalid: {ascending}")

    direction = asc if ascending else desc

    return (
        session.query(
            Publisher.name,
            func.count(Author.first_name).label("total_authors")
        )
        .join(Publisher.authors)
        .group_by(Publisher.name)
        .order_by(direction("total_authors"))
    )


def get_authors(session):
    """Get a list of author objects sorted by last name."""
    return session.query(Author).order_by(Author.last_name).all()


def add_new_book(session, author_name, book_title, publisher_name):
    """Adds a new book to the system."""

    # Get the authors fullname.
    first_name, _, last_name = author_name.partition(" ")

    # Check if books exists.
    book = (
        session.query(Book)
        .join(Author)
        .filter(Book.title == book_title)
        .filter(
            and_(
                Author.first_name == first_name, Author.last_name == last_name
            )
        )
        .one_or_none()
    )
    # Create book if needed.
    if book is None:
        book = Book(title=book_title)

    # Get the author.
    author = (
        session.query(Author)
        .filter(
            and_(
                Author.first_name == first_name, Author.last_name == last_name
            )
        )
        .one_or_none()
    )
    # Do we need to create the author?
    if author is None:
        author = Author(first_name=first_name, last_name=last_name)
        session.add(author)

    # Get the publisher.
    publisher = (
        session.query(Publisher)
        .filter(Publisher.name == publisher_name)
        .one_or_none()
    )
    # Do we need to create the publisher?
    if publisher is None:
        publisher = Publisher(name=publisher_name)
        session.add(publisher)

    # Initialize the book relationships
    book.author = author
    book.publishers.append(publisher)
    session.add(book)

    # Commit to db
    session.commit()
