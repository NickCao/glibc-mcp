from ctypes import CDLL, get_errno as c_get_errno, cast, c_uint64
from .types import DIR_p, Dirent, dirent_p

from mcp.server.fastmcp import FastMCP


LIBC = CDLL("libc.so.6")
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
        return LIBC.open(path, flags, mode)
    else:
        return LIBC.open(path, flags)


@mcp.tool()
def creat(path: str, mode: int) -> int:
    return LIBC.creat(path, mode)


@mcp.tool()
def openat(dirfd: int, path: str, flags: int, mode: int | None = None) -> int:
    if mode:
        return LIBC.openat(dirfd, path, flags, mode)
    else:
        return LIBC.openat(dirfd, path, flags)


@mcp.tool()
def opendir(name: str) -> c_uint64:
    return LIBC.opendir(name)


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
