from ctypes import (
    POINTER,
    Structure,
    c_uint64,
    c_ushort,
    c_ubyte,
    c_char,
    c_int64,
)

from dataclasses import dataclass


class DIR(Structure):
    pass


DIR_p = POINTER(DIR)


class dirent(Structure):
    _fields_ = [
        ("d_ino", c_uint64),
        ("d_off", c_int64),
        ("d_reclen", c_ushort),
        ("d_type", c_ubyte),
        ("d_name", c_char * 256),
    ]


dirent_p = POINTER(dirent)


@dataclass
class Dirent:
    d_ino: int
    d_off: int
    d_reclen: int
    d_type: int
    d_name: str

    def __init__(self, val: dirent):
        self.d_ino = val.d_ino
        self.d_off = val.d_off
        self.d_reclen = val.d_reclen
        self.d_type = val.d_type
        self.d_name = val.d_name.decode()
