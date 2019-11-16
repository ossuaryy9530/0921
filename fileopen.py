f = open("simple.txt", 'r') #fileopen.py와 simple.txt 파일은 같은 폴더에 있어야함
data = f.read()
print(data)
f.close()
