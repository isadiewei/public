import sys
import os

def replace_chars(filename, original_char, replacement_char):
    original = open(filename, 'r')
    lines = []
    
    for x in original:
        lines.append(
            x.replace(original_char, replacement_char))
    
    original.close()
    new_file = open(filename, 'w')
    
    new_file.writelines(lines)
    new_file.close()
    

if __name__ == '__main__':
    filename = sys.argv[1]
    original_char = sys.argv[2]
    replacement_char = '\n' if sys.argv[3] == "newline" else sys.argv[3]
        
    replace_chars(filename, original_char, replacement_char)
    
