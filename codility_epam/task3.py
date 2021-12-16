import datetime
from pprint import PrettyPrinter
import re
from datetime import date

pp = PrettyPrinter(indent=3, depth=3)

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
    lines_cleaned = []
    finished_line = []
    final_lst = []
    date_since = date(year=1990, month=1, day=31)
    months = (
        ("Jan", 1), ("Feb", 2), ("Mar", 3), ("Apr", 4), ("May", 5), ("Jun", 6),
        ("Jul", 7), ("Aug", 8), ("Sep", 9), ("Oct", 10), ("Nov", 11), ("Dec", 12)
    )
    pre_date = ""

    for line in lines:
        if len(line) >= 1:
            strpd_line = re.sub(r"^\s+", "", line)
            lns_clnd2 = [f_size, day, month, year, file_name] = strpd_line.split(" ")
            for _ in lns_clnd2:
                size = int(lns_clnd2[0])

            print(lns_clnd2)

    pp.pprint(lines_cleaned)


if __name__ == "__main__":
    solution(files)
