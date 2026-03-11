from .impl import opendir, readdir


def test_file_operations():
    dirp = opendir(".")
    while readdir(dirp):
        pass
