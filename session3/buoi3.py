# Nhập n số từ bàn phím và in ra tổng n số vừa nhập

# n = int(input("Nhập n: "))
# tong = 0
# for i in range(n):
#     so = int(input("Nhập số: "))
#     tong = tong + so
# print(tong)


# n = int(input("Nhập số: "))
# if n%2==0:
#     print(n,' là số chẵn')
# else:
#     print(n,' là số lẻ')


# n = int(input("Nhập số tuổi: "))
# if n<10:
#     print('baby')
# elif 10<=n<16:
#     print('teen')
# else:
#     print('adult')


# yob = input('Nhập năm sinh: ')
# while not yob.isdigit():
#     print("Mời nhập lại")
#     yob = input('Nhập năm sinh: ')
# age = 2019 - int(yob)
# print("Tuổi của bạn là",age)




# mk = input("Enter your password: ")
# while len(mk)<8:
#     print("Mật khẩu chưa đủ kí tự. Mời nhập lại")
#     mk = input("Enter your password: ")
# print("Mật khẩu của bạn là: ",mk)


# loop_count = 0
# while loop_count<3:
#     print('loop count: ',loop_count)
#     #loop_count+=1
#     loop_count = loop_count+1
#     if loop_count>=3:
#         break
# print('aa')



# a = int(input("Nhập a: "))
# b = int(input("Nhập b: "))
# c = int(input("Nhập c: "))

# delta=(b**2)-(4*a*c)

# if delta<0:
#     print("Phương trình vô nghiệm")
# elif delta==0:
#     print("Phương trình có nghiệm kép")
#     x= -b/(2*a)
# elif delta>0:
#     print("Phương trình có 2 nghiệm phân biệt")
#     x1 = (-b+(delta**0.5))/(2*a)
#     x2 = (-b-(delta**0.5))/(2*a)
# print(x1,x2)

ls=[]
n = int(input("Mời bạn nhập số phần tử: "))
for i in range(1,n+1):
    print("Nhập phần tử thứ ",i)
    so = int(input(""))
    ls.append(so)
print("dãy bạn vừa nhập là: ")
print(ls)

print("Tổng dãy vừa nhập là: ")
print(sum(ls))

print("Phần tử thứ 2 trong dãy là: ")
print(ls[1])