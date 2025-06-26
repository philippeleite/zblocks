from cffi import FFI

ffi = FFI()
ffi.cdef('''                                                  
void read_memory(char* buffer, int length, intptr_t address); 
 ''')

ffi.set_source("zutils", '''                                   
#include <stdint.h>                                           
#include <string.h>                                           

#pragma export(read_memory)                                   
void read_memory(char *buffer,                                
                 int length,                                  
                 intptr_t address) {                          
    char * data = (char *)address;                            
    memcpy(buffer, data, length);                             
}                                                             
''')

