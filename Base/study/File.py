file = open(file='foo.txt', mode="rb")

print(file.readlines())
# os.SEEK_END
file.read(3)
file.tell()
file.close()
