#include <stdint.h>
#include <string.h>

void read_memory(char *buffer,
                 int length,
                 intptr_t address) {
    char * data = (char *)address;
    memcpy(buffer, data, length);
}