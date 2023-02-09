p, d = input().split()
n = 1
while True:
    Modulus = (int(d) * n) % int(p)
    if Modulus <= (int(p) / 2):
        print(int(d) * n)
        break
    n += 1
