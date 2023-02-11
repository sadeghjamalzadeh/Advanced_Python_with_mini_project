n = int(input())
list_names = []
ls_repeat = []
for i in range(n):
    name, family = input().split(" ")
    list_names.append(name)
for name in set(list_names):
    ls_repeat.append(list_names.count(name))

print(max(ls_repeat))
