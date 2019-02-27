print("a")
for i in range(20):
    print("*",end="")

print("b")
n = int(input("Mời nhập n: "))
for k in range(n):
    print("*",end="")

print("c")
for h in range(4):
    print("x * ",end="")
print("x")

print("d")
n = int(input("Nhập n: "))
if n%2==0:
    for h in range(int(n/2)):
        print("x * ",end="")
else:
    for h in range(int(n/2)):
        print("x * ",end="")
    print("x")

print("e")
print()
print("f")

for v in range(3):
    for i in range(7):
        print("* ",end="")
    print()

print("g")
m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))
for v in range(m):
    for i in range(n):
        print("* ",end="")
    print()