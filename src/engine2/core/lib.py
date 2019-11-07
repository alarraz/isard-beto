import ctypes


def get_tid():
    tid = ctypes.CDLL('libc.so.6').syscall(186)
    return tid
