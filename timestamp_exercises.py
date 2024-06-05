
a = "2024-02-28T04:39:34Z"


def convert_to_unix_timestamp(timestamp: str) -> int:
    import datetime
    from datetime import timezone
    import time

    dt = datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    unix_timestamp = int(time.mktime(dt.timetuple()))
    return unix_timestamp


if __name__ == "__main__":
    print(convert_to_unix_timestamp(a))
