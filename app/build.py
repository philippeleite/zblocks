from cffi import FFI

ffi = FFI()
ffi.cdef('''                                                  
void read_memory(char* buffer, int length, intptr_t address); 
void read_memory_auth(char* buffer, int length, intptr_t address); 
 ''')

ffi.set_source("zutils", r'''                                   
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
    unsigned long plist[4];
    unsigned int *lx; 
    plist[0] = (unsigned long)(void *) &system_level;
    plist[1] = (unsigned long)(void *) name;
    plist[2] = (unsigned long)(void *) token;
    plist[3] = (unsigned long)(void *) &wk_rc;  
    __asm(" L 15,x'10'\n"
          " L 15,x'220'(15,0)\n"
          " L 15,x'14'(15,0)\n"
          " L 15,x'80'(15,0)\n"
          " BASR 14,15\n"
          : 
          : "NR:r1"(plist)
          : "r1", "r14", "r15");
    
    unsigned int plist31[3];
    if (wk_rc == 0) {
        lx = (unsigned int *)(void *)token;
        plist31[0] = (unsigned int)(void * __ptr32)buffer;
        plist31[1] = (unsigned int)(void * __ptr32)&length;
        plist31[2] = (unsigned int)(void * __ptr32)&address; 
        __asm(" SAM31\n"
              " PC  0(%[pc])\n"
              " SAM64\n" 
              : 
              : [pc] "r"(lx[1]),
                "NR:r1"(plist31)
              : "r1", "r15");   
    }      
}                                                               
''')

