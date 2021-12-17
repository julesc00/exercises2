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
    final_lst, filtered_items = [], []
    date_since = datetime.datetime(year=1990, month=1, day=31)

    for line in lines:
        if len(line):
            strpd_line = re.sub(r"^\s+", "", line)
            [f_size, day, month, year, file_name] = strpd_line.split(" ")
            dates = "".join([day, month, year])
            fmt_dates = datetime.datetime.strptime(dates, "%d%b%Y")
            final_lst = [int(f_size), fmt_dates, file_name]
            if final_lst[0] >= 240 * 2**10 and final_lst[1] > date_since:
                filtered_items.append(final_lst)

    return len(filtered_items) if len(filtered_items) else "NO FILES"


if __name__ == "__main__":
    print(solution(files))
