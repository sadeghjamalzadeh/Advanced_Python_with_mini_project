list = []
while True:
    num = int(input())
    if num != 0:
        list.insert(0,num)
    elif num == 0:
        break
    else:
        print("please inter valid number")
print(*list,sep="\n")

