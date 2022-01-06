import datetime
import re

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
no_files = ""


def solution(s: str):
    lines = s.split("\n")
    result = 0
    date_since = datetime.datetime(year=1990, month=1, day=31)

    for line in lines:
        if len(line):
            strpd_line = re.sub(r"^\s+", "", line)
            sizes = re.sub(r"$\d+/\^s+", "", strpd_line)
            print(sizes)
            [f_size, day, month, year, _] = strpd_line.split(" ")
            dates = "".join([day, month, year])
            fmt_dates = datetime.datetime.strptime(dates, "%d%b%Y")
            if int(f_size) >= 240 * 2**10 and fmt_dates > date_since:
                result += 1

    return str(result) if result else "NO FILES"


if __name__ == "__main__":
    print(solution(files))