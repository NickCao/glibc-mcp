from ctypes import (
    POINTER,
    Structure,
    c_uint64,
    c_ushort,
    c_ubyte,
    c_char,
    c_int64,
    c_uint32,
    c_time_t,
)

from dataclasses import dataclass

off_t = c_int64
dev_t = c_uint64
ino_t = c_uint64
mode_t = c_uint32
nlink_t = c_uint64
uid_t = c_uint32
gid_t = c_uint32
dev_t = c_uint64
blksize_t = c_int64
blkcnt_t = c_int64


class DIR(Structure):
    pass


DIR_p = POINTER(DIR)


class dirent(Structure):
    _fields_ = [
        ("d_ino", ino_t),
        ("d_off", off_t),
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


class timespec(Structure):
    _fields_ = [
        ("tv_sec", c_time_t),
        ("tv_nsec", c_time_t),
    ]


@dataclass
class Timespec:
    tv_sec: int
    tv_nsec: int

    def __init__(self, val: timespec):
        self.tv_sec = val.tv_sec
        self.tv_nsec = val.tv_nsec


class stat(Structure):
    _fields_ = [
        ("st_dev", dev_t),
        ("st_ino", ino_t),
        ("st_nlink", nlink_t),
        ("st_mode", mode_t),
        ("st_uid", uid_t),
        ("st_gid", gid_t),
        ("__pad0", c_uint32),
        ("st_rdev", dev_t),
        ("st_size", off_t),
        ("st_blksize", blksize_t),
        ("st_blocks", blkcnt_t),
        ("st_atim", timespec),
        ("st_mtim", timespec),
        ("st_ctim", timespec),
        ("__glibc_reserved", c_int64 * 3),
    ]


@dataclass
class Stat:
    st_dev: int
    st_ino: int
    st_nlink: int
    st_mode: int
    st_uid: int
    st_gid: int
    st_rdev: int
    st_size: int
    st_blksize: int
    st_blocks: int
    st_atim: Timespec
    st_mtim: Timespec
    st_ctim: Timespec

    def __init__(self, val: stat):
        self.st_dev = val.st_dev
        self.st_ino = val.st_ino
        self.st_nlink = val.st_nlink
        self.st_mode = val.st_mode
        self.st_uid = val.st_uid
        self.st_gid = val.st_gid
        self.st_rdev = val.st_rdev
        self.st_size = val.st_size
        self.st_blksize = val.st_blksize
        self.st_blocks = val.st_blocks
        self.st_atim = Timespec(val.st_atim)
        self.st_mtim = Timespec(val.st_mtim)
        self.st_ctim = Timespec(val.st_ctim)
