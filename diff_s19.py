import sys

lines_to_print = 2000000000

data_to_ignore = """
C3C3C3C3C3C3C3C3C3C3C3C3C3C3C3C3C3C3C3C3C3C3C3C3C3C3C3C3C3C3C3C3
0000000000000000000000000000000000000000000000000000000000000000
""".split()

def myprint(str):
    global lines_to_print
    if lines_to_print > 0:
        print str
        lines_to_print = lines_to_print - 1

def print_nonempty_s3(srec):
    data = srec[13:-2]
    if data not in data_to_ignore:
        myprint(srec)
        #myprint('Data:'+data)
    else:    
        #myprint(srec+' Ignored')
        pass

if len(sys.argv) < 2:
    inputfile1 = 'eol.s19' 
else:
    inputfile1 = sys.argv[1]
if len(sys.argv) < 3:
    inputfile2 = 'eol_with_data.s19'
else:
    inputfile2 = sys.argv[2]

f1 = open(inputfile1)
f2 = open(inputfile2)

f1_lines = sorted(f1.readlines())
f2_lines = sorted(f2.readlines())

f1.close()
f2.close()

f1_next = 0
f2_next = 0

while (f1_next < len(f1_lines)) and (f2_next < len(f2_lines)):
    f1_line = f1_lines[f1_next].strip()
    f2_line = f2_lines[f2_next].strip()
    if f1_line[:2] <> 'S3':
        myprint('-'+f1_line)
        f1_next = f1_next + 1
        continue
    if f2_line[:2] <> 'S3':
        myprint('+'+f2_line)
        f2_next = f2_next + 1
        continue
    f1_addr = f1_line[4:12]
    f2_addr = f2_line[4:12]
    #myprint(f1_addr+' '+f2_addr)
    if f1_addr == f2_addr:
        if f1_line <> f2_line:
            print_nonempty_s3('-'+f1_line)
            print_nonempty_s3('+'+f2_line)
        f1_next = f1_next + 1
        f2_next = f2_next + 1
    elif f1_addr < f2_addr:
        print_nonempty_s3('-'+f1_line)
        f1_next = f1_next + 1
    else:
        print_nonempty_s3('+'+f2_line)
        f2_next = f2_next + 1

#myprint('Remaining lines....')
map(lambda l: print_nonempty_s3('-'+l.strip()), f1_lines[f1_next:])
map(lambda l: print_nonempty_s3('+'+l.strip()), f2_lines[f2_next:])

