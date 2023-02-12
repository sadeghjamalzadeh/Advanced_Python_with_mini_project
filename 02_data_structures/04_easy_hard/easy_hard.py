print(*sorted([int(value) for index, value in enumerate(list(map(int, input().split(" ")))) if ((index + 1) % 6) == 0 and int(value) % 6 == 0]))
