#!/bin/sh
xlc -q64 -Wc,dll -Wc,exportall -Wl,dll -o zblocks.so zblocks.c