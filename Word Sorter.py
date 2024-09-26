f = open("WordAll.txt", "r")
file = open("Word11.txt", "a")
array = []

for i in range(1000):
    txt = f.readline()
    if len(txt) == 12:
        array.append(txt)
print(array)
file.writelines(array)
file.close
