# n = int(input('Nhập số chữ số: '))
# tong=0
# trungbinh = 0
# for i in range(n):
#     so = int(input("Nhập số: "))
#     tong = tong + so
# print('Tổng các số trên là',tong)
# trungbinh = tong/n
# print('Trung bình các số trên là',trungbinh)

# -----------------------------------------

# def say_hi():
#     print('hi')
#     print('bye')

# say_hi()
# say_hi()
# say_hi()
# say_hi()

# def add_two_number(x,y):

#     print('tong hai so la',x+y)
# # a = int(input('Nhap so thu nhat: '))
# # b = int(input('Nhap so thu hai: '))
# add_two_number(150+0*2,500)

# def add_two_number(a,b):
#     return a+b
# num1 = int(input('Nhap so thu nhat: '))
# num2 = int(input('Nhap so thu hai: '))
# num3 = int(input('Nhap so thu ba: '))
# sum_1_2 = add_two_number(num1,num2)
# sum_3= add_two_number(sum_1_2,num3)
# print('Toong 3 so:',sum_3)

# def add_two_number(a,b):
#     return a+b
# # print(add_two_number(add_two_number(1,2),3))
# x = 121+add_two_number(3,4)
# print(x)

# def abs_of_number(a):
#     if a>0:
#         return a
#         print('tri tuyet doi la',a)
#     else:
#         return -a
#         print('tri tuyet doi la',-a)
#     print('tri tuyet doi la',a)
# x=abs_of_number(-12)
# tong= 12 + abs_of_number(-12)
# print(x)
# print(tong)


# def evaluate(a,b,operator):
#     if operator == '+':
#         return a+b
#     elif operator == '-':
#         return a-b
#     elif operator == '*':
#         return a*b
#     elif operator == '/':
#         return a/b
#     else:
#         return None
# x = evaluate(5,6,'*')
# print(x)

def is_prime(n):
    if n<2:
        return False
    for v in range(2,n):
        if n%v==0:
            return False
    return True
so = int(input('nhap so can ktra: '))
for v in range(2,so+1):
    if is_prime(v):
        print('snt la:',v)



# if is_prime(so):
#     print('la snt')
# else:
#     print('k la snt')