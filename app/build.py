from cffi import FFI

ffi = FFI()
ffi.cdef('''                                                  
void read_memory(char* buffer, int length, intptr_t address); 
void read_memory_auth(char* buffer, int length, intptr_t address); 
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

#pragma export(read_memory_auth)
void read_memory_auth(char *buffer,                                
                      int length,                                  
                      intptr_t address) {
    unsigned int system_level = 4;    
    const char *name = "ZBLOCKS         ";
    unsigned char token[16];   
    unsigned int wk_rc;  
    unsigned int plist[4];
    plist[0] = (unsigned int * __ptr32)(void *) &system_level;
    plist[1] = (unsigned int * __ptr32)(void *) name;
    plist[2] = (unsigned int * __ptr32)(void *) token;
    plist[3] = (unsigned int * __ptr32)(void *) &wk_rc;  
    __asm(" SAM31"
          " L 15,x'10'"
          " L 15,x'220'(15,0)"
          " L 15,x'14'(15,0)"
          " L 15,x'08'(15,0)"
          " BAS 14,15"
          " SAM64"
          : 
          : "NR:r1"(plist)
          : "r1", "r14", "r15");
    
    if (wk_rc == 0) {
        lx = (unsigned int *)(void *)token;
        plist[0] = (unsigned int * __ptr32)(void *)buffer;
        plist[1] = (unsigned int * __ptr32)(void *)&length;
        plist[2] = (unsigned int * __ptr32)(void *)&address; 
        __asm(" SAM31"
              " PC  0(%[pc])"
              " SAM64" 
              : 
              : [pc] "r"(lx[1]),
                "NR:r1"(plist)
              : "r1", "r15");   
    }      
}                                                               
''')

