#include <stdint.h>
#include <string.h>

#pragma export(read_memory)
void read_memory(char *buffer,
                 int length,
                 intptr_t address) {
    char * data = (char *)address;
    memcpy(buffer, data, length);
}