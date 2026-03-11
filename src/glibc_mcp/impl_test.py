from .impl import opendir, readdir, stat


def test_file_operations():
    dirp = opendir(".")
    while ent := readdir(dirp):
        stat(ent.d_name)
