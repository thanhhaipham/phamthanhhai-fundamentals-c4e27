# for <bien DK> in <danh sách>
# các lệnh

for v in 'thanh hai':
    print(v)

for x in range (0,10):
    y=3*x**2 + 2*x +1
    print("y co gia tri cua la: ",y)

# range([start],stop,[step]) tham số là int
for x in range (0,20,3):
    print(x)

print(list(range(10)))

# tinh tong : 1 + 2 + ... + 10

y=0
for x in range(1,11,1):
    y = y + x
print(y)

# tinh tong : 1**2 + 2**2 + ... + 10**2

n = int(input("Nhap n: "))
y=0
for x in range(1,n+1,1):
    y = y + x**2
print(y)

# Nhập năm sinh của 1 người và in ra màn hình như sau:
# Nếu người đó <10 tuổi => in ra " BABY "
# Nếu người đó >=10 <16 tuổi => in ra " TEEN "
# Còn lại in ra " ADULT "