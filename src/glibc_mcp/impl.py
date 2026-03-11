from ctypes import CDLL, get_errno as c_get_errno, cast, c_uint64, byref
from .types import DIR_p, Dirent, dirent_p, Stat, stat as c_stat

from mcp.server.fastmcp import FastMCP


LIBC = CDLL("libc.so.6", use_errno=True)
LIBC.opendir.restype = c_uint64
LIBC.fdopendir.restype = c_uint64
LIBC.readdir.restype = dirent_p

mcp = FastMCP("Glibc MCP", json_response=True)


@mcp.tool()
def get_errno() -> int:
    return c_get_errno()


@mcp.tool()
def open(path: str, flags: int, mode: int | None = None) -> int:
    if mode:
        return LIBC.open(path.encode(), flags, mode)
    else:
        return LIBC.open(path.encode(), flags)


@mcp.tool()
def creat(path: str, mode: int) -> int:
    return LIBC.creat(path.encode(), mode)


@mcp.tool()
def openat(dirfd: int, path: str, flags: int, mode: int | None = None) -> int:
    if mode:
        return LIBC.openat(dirfd, path.encode(), flags, mode)
    else:
        return LIBC.openat(dirfd, path.encode(), flags)


@mcp.tool()
def opendir(name: str) -> c_uint64:
    return LIBC.opendir(name.encode())


@mcp.tool()
def fdopendir(fd: int) -> c_uint64:
    return LIBC.fdopendir(fd)


@mcp.tool()
def readdir(dirp: int) -> Dirent | None:
    p = LIBC.readdir(cast(dirp, DIR_p))
    if p:
        return Dirent(p.contents)
    else:
        return None


@mcp.tool()
def stat(path: str) -> (Stat | None, int):
    s = c_stat()
    r = LIBC.stat(path.encode(), byref(s))
    if r < 0:
        return None, r
    return Stat(s), r


@mcp.tool()
def lstat(path: str) -> (Stat | None, int):
    s = c_stat()
    r = LIBC.lstat(path.encode(), byref(s))
    if r < 0:
        return None, r
    return Stat(s), r
