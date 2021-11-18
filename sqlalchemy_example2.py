
from sqlalchemy import (asc, desc)
from sqlalchemy.orm import session


def get_books_by_publisher(session, ascending=True):
    """Get a list of publishers and the number of books they've published."""

    if not isinstance(ascending, bool):
        raise ValueError(f"Sorting value invalid: {ascending}")

    direction = asc if ascending else desc

    return (
        session.query(
            Publisher
        )
    )
