import datetime
from pprint import PrettyPrinter
import re
from datetime import date

pp = PrettyPrinter(indent=3)

files = """
    779091968 23 Sep 2009 system.zip
    284164096 14 Aug 2013 to-do-list.xml
    714080256 19 Jun 2013 blockbuster.mpeg
          329 12 Dec 2010 notes.html
    444596224 17 Jan 1950 delete-this.zip
          641 24 May 1987 setup.png
       245760 16 Jul 2005 archive.zip
    839909376 31 Jan 1990 library.dll
"""


def solution(s: str):
    lines = s.split("\n")
    final_lst = []
    filtered_items = list()
    date_since = date(year=1990, month=1, day=31)
    months = (
        ("Jan", 1), ("Feb", 2), ("Mar", 3), ("Apr", 4), ("May", 5), ("Jun", 6),
        ("Jul", 7), ("Aug", 8), ("Sep", 9), ("Oct", 10), ("Nov", 11), ("Dec", 12)
    )

    for line in lines:
        if len(line) >= 1:
            strpd_line = re.sub(r"^\s+", "", line)
            lns_clnd2 = [f_size, day, month, year, file_name] = strpd_line.split(" ")
            size = int(lns_clnd2[0])
            dates = "".join([day, month, year])
            fmt_date = datetime.datetime.strptime(dates, "%d%b%Y")
            final_lst = [size, fmt_date, file_name]

            filtered_items.append(final_lst)
    pp.pprint(filtered_items)


if __name__ == "__main__":
    solution(files)
