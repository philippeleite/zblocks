from zutils import lib, ffi

def read_memory(buffer: bytearray, size: int, address: int):
    lib.read_memory(ffi.from_buffer(buffer), size, address)

def read_memory_auth(buffer: bytearray, size: int, address: int):
    lib.read_memory_auth(ffi.from_buffer(buffer), size, address)