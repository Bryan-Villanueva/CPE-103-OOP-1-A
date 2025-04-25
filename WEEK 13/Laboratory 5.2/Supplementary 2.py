fout = open('SURNAME.txt', 'w')
fout.write('This is the original text.\n')
fout.close()

fhand = open('SURNAME.txt', 'r')
print('Content after creation:')
print(fhand.read())
fhand.close()

fout = open('SURNAME.txt', 'a')
fout.write('This is the updated text.\n')
fout.close()

fhand = open('SURNAME.txt', 'r')
print('Content after update:')
print(fhand.read())
fhand.close()

import os
os.remove('SURNAME.txt')
print('File deleted.')
