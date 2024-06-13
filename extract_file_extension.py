import os


def extract_file_extension(file_name):
    return os.path.splitext(file_name)[1].lower()


if __name__ == "__main__":
    print(extract_file_extension("example&title.png"))
    print(extract_file_extension("UGWR_12865603_56. & 58 BUNKER LN_SIGNED AR PHOTO.jpg"))
    print(extract_file_extension("example"))
