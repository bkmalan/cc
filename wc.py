import sys

lines = []
if not sys.stdin.isatty():
    for line in sys.stdin:
        lines.append(line)
op = ''
target = ''
if len(sys.argv) == 3:
    file_name,  op, target = sys.argv
if len(sys.argv) == 2:

    arg1, arg2 = sys.argv
    target = arg2
    op = ''
    if len(lines):
        op = arg2

if not lines:
    file = open(target, 'r')
    lines = file.readlines()

bytes_total = 0
words_total = 0
for line in lines:
    bytes_total += len(line)
    words_total += len(line.split())

if op == '-c':
    print(bytes_total)
elif op == '-l':
    print(len(lines))
elif op == '-w':
    print(words_total)
else:
    print(f'{len(lines)} {words_total} {bytes_total} {target}')
