import os


def extract_file_extension(file_name):
    print(os.path.splitext(file_name)[1].lower())
    breakpoint()
    return os.path.splitext(file_name)[1].lower()


if __name__ == "__main__":
    test_files = [
        'file.txt', 'document.pdf', 'image.jpeg',
        'file!.txt', 'document@.pdf', 'image#.jpeg',
        'file$.txt', 'document%.pdf', 'image^.jpeg',
        'file&.txt', 'document*.pdf', 'image(.jpeg',
        'file).txt', 'document-.pdf', 'image_.jpeg',
        'file+.txt', 'document=.pdf', 'image,.jpeg',
        'file;.txt', 'document\'.pdf', 'image".jpeg',
        'file`.txt', 'document~.pdf', 'file name.txt',
        'document name.pdf', 'image name.jpeg', 'file',
        'document', 'image', '.file', '.document', '.image',
        'file.name.txt', 'document.name.pdf', 'image.name.jpeg',
        'fileé.txt', 'documentç.pdf', 'imageü.jpeg',
        'file123!.txt', 'document456@.pdf', 'image789#.jpeg',
        'archive.tar.gz', 'script.py', 'data.json'
    ]
    for f in test_files:
        print(f"{f} -> {extract_file_extension(f)}")
