fout = open('VILLANUEVA.txt', 'w')
fout.write('Analysis of file handling in Python.\n')
fout.write('File handling involves operations like read, write, and update.\n')
fout.close()

fhand = open('VILLANUEVA.txt', 'r')
for line in fhand:
    print(line.strip())
fhand.close()
