import sys


def count_lines(file_name):
    with open(file_name, mode='r', encoding='utf-8') as file:
        count = 0
        for line in file:
            count += 1
    return count


def count_chars(file_name):
    with open(file_name, mode='r', encoding='utf-8') as file:
        count = 0
        for line in file:
            count += len(line)
    return count


def test(file_name):
    if len(sys.argv) > 1:
        file_name = sys.argv[0]
    return count_lines(file_name), count_chars(file_name)


if __name__ == '__main__':
    print(test('mymod.py'))



