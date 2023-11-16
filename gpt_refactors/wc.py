import sys

def read_lines_from_input():
    lines = []
    if not sys.stdin.isatty():
        for line in sys.stdin:
            lines.append(line)
    return lines

def read_lines_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

def count_metrics(lines):
    bytes_total = sum(len(line) for line in lines)
    words_total = sum(len(line.split()) for line in lines)
    return bytes_total, words_total

def main():
    if len(sys.argv) == 3:
        _, op, target = sys.argv
    elif len(sys.argv) == 2:
        _, target = sys.argv
        op = '' if not lines else target

    lines = read_lines_from_input() if not sys.stdin.isatty() else read_lines_from_file(target)

    bytes_total, words_total = count_metrics(lines)

    if op == '-c':
        print(bytes_total)
    elif op == '-l':
        print(len(lines))
    elif op == '-w':
        print(words_total)
    else:
        print(f'{len(lines)} {words_total} {bytes_total} {target}')

if __name__ == "__main__":
    main()

