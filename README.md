# diff_s19
Generates inline diff of S Records between two files

Assumes S Records are in S3 format with 25 bytes of data typically known as '.s19' files.
Ignores all zeros or data byte pattern 0xC3

Usage: python diff_s19.py <file1> <file2>

Lines only in the first file are prefixed by '-'
Lines only in the second file are prefixed by '+
