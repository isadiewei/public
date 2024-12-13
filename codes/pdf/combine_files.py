import os
import sys
from pypdf import PdfWriter

def merge_files_from_list(dir='.', files=[], name='export.pdf'):
    if len(files) == 0:
        print('no files listed')
        return
    
    names = files
    files = os.listdir(dir)
    files.sort()
    
    files = [name for name in names if name in files]
    files = [os.path.abspath(file) for file in files]

    print('merging files:')
    print(files)

    m = PdfWriter()

    for file in files:
        m.append(file)

    m.write(name)
    m.close()
    

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('merge containing_directory local_files_to_merge export_name')
    else:
        filenames = sys.argv[2:len(sys.argv)-1]
        merge_files_from_list(sys.argv[1], filenames, sys.argv[len(sys.argv)-1])
