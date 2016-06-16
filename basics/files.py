import codecs

# 1. write a for append
f = open('./example/io.txt', 'a')
f.write("write 1\n")
print("write 2\n", file=f)
f.close()

# 2. 'rU' is the "Universal" convert different line-endings so they always come through as a simple '\n'.
f = open('./example/io.txt', 'rU')
for line in f:
    print(line)

one_line = f.readline()
all_as_list = f.readlines()
all_as_one_line = f.read()

f.close()

# 3. read as unicode
f = codecs.open('./example/io.txt', 'rU', 'utf-8')
