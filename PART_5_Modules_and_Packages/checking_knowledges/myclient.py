import mymod
from mymod import *
if __name__ == '__main__':
    print(f'{mymod.count_lines("myclient.py") = }', f'{mymod.count_chars("myclient.py") = }', f'{mymod.test("myclient.py") = }',
          f'{60 * "-"}', f'{count_lines("myclient.py") = }', f'{count_chars("myclient.py") = }', f'{test("myclient.py") = }', sep='\n')
