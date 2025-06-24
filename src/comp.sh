#!/bin/sh

# Compile using IBM Open XL C/C++ for z/OS 2.1
ibm-clang64 -shared -o zblocks.so zblocks.c