from cffi import FFI

ffi = FFI()
ffi.cdef('''                                                  
void read_memory(char* buffer, int length, intptr_t address); 
void read_memory_auth(char* buffer, int length, intptr_t address); 
 ''')

ffi.set_source("zutils", r'''                                   
#include <stdint.h>                                           
#include <stdlib.h>                                           
#include <stdio.h>                                           
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
    // const char *name = "ZBLOCKS         ";
    const char name[] = {0xe9, 0xc2, 0xd3, 0xd6, 0xc3, 0xd2, 0xe2, 0x40,
                         0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40};  
    unsigned char token[16];   
    unsigned int wk_rc;  
    unsigned long plist[4];
    unsigned int *lx; 
    plist[0] = (unsigned long)(void *) &system_level;
    plist[1] = (unsigned long)(void *) name;
    plist[2] = (unsigned long)(void *) token;
    plist[3] = (unsigned long)(void *) &wk_rc;  
    __asm(" LLGT 15,x'10'\n"
          " L 15,x'220'(15,0)\n"
          " L 15,x'14'(15,0)\n"
          " L 15,x'80'(15,0)\n"
          " BASR 14,15\n"
          : 
          : "NR:r1"(plist)
          : "r1", "r14", "r15");
           
    // printf("wk_rc = %d\n", wk_rc);
    unsigned long plistpc[3];
    if (wk_rc == 0) {
        lx = (unsigned int *)(void *)token;
        plistpc[0] = (unsigned long)(void *)buffer;
        plistpc[1] = (unsigned long)length;
        plistpc[2] = (unsigned long)address;
        // printf("plistpc = %016x\n", plistpc);
        // printf("plistpc[0] = %016x\n", plistpc[0]);     
        // printf("plistpc[1] = %016x\n", plistpc[1]);     
        // printf("plistpc[2] = %016x\n", plistpc[2]);     
        // printf("lx[1] = %08x\n", lx[1]);  
        __asm(" LLGT 14,%[pc]\n" 
              " PC  0(14)\n"
              : 
              : [pc] "m"(lx[1]),
                "NR:r1"(plistpc)
              : "r1", "r14", "r15");   
    }       
}                                                               
''')

