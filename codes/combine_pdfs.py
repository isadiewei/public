import os
import sys
from pypdf import PdfWriter

def merge_files_from_folder(dir='.', name='export.pdf'):
    cwd = os.getcwd()
    dir = os.path.abspath(dir)
    os.chdir(dir)
    files = os.listdir(dir)
    files.sort()

    files = [os.path.abspath(file) for file in files]
    m = PdfWriter()

    for file in files:
        m.append(file)

    os.chdir(cwd)
    m.write(name)
    m.close()

if __name__ == '__main__':
    merge_files_from_folder(sys.argv[1], sys.argv[2])
