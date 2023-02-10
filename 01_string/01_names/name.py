n = int(input())
names = []
for i in range(n):
    names.append(input())
names_len = []

for name_input in names:
    name = ''
    for chr in name_input:
        if chr not in name:
            name += chr
    names_len.append(len(name))
print(max(names_len))
