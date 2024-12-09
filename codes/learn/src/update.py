import os
import sys

# please excuse my python i just wanted this to work to edit later
def get_tabs(i):
    acc = []

    for i in range(len(i)):
        acc.append('\t')

    return "".join(acc)
            

def walk_directory(path, add_break=False):
    summary = open('./SUMMARY.md', 'w')
    
    lines = []
    lines.append(f'- [Abstract](./abstract.md)\n')

    for root, dirs, files in os.walk(path):

        for file_name in files:
            result = os.path.join(root, file_name)
            _titles = []

            for header in result.split('/'):
                _titles.append(header)

            print(_titles)
            actual_file_name = _titles.pop()


            if add_break:
                lines.append(f'{"".join(get_tabs(_titles))}- {" > ".join(_titles)}\n')

            lines.append(f'{"".join(get_tabs(_titles))}- [{actual_file_name}](./{result})\n')

        print(lines)

    summary.writelines(lines)


if __name__ == '__main__':
    path = sys.argv[1]
    walk_directory(path)
