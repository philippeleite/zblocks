from cffi import FFI

ffi = FFI()
ffi.cdef('''
void read_memory(char* buffer, int length, intptr_t address);
 ''')
C = ffi.dlopen('./zblocks.so')

def read_memory(buffer: bytearray, size: int, address: int):
    C.read_memory(ffi.from_buffer(buffer), size, address)