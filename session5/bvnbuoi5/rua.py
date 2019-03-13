
# 1. in ra 3 lần hello world
def hello_world():
    print('Hello World')
hello_world()
hello_world()
hello_world()
# 2. Tổng 2 số
def tong(num1,num2):
    return num1 + num2
num1 = int(input('Nhap so thu nhat: '))
num2 = int(input('Nhap so thu hai: '))
print('tong 2 so la',num1+num2)
# 3+4.vẽ hình vuông
from turtle import *
def draw_square(dodai,mau):
    color(mau)
    for i in range(4):
        forward(dodai)
        left(90)
# draw_square(100,'red')
for k in range(30):
        draw_square(k*5,'blue')
        left(17)
        penup()
        forward(k*2)
        pendown()
mainloop()
# 5+6.Vẽ ngôi sao
def draw_star(x,y,dodai):
        penup()
        setx(x)
        sety(y)
        pendown()
        for i in range(5):
                right(144)
                forward(dodai)
speed(0)
color('blue')
for i in range(100):
        import random
        x= random.randint(-300,300)
        y=random.randint(-300,300)     
        dodai=random.randint(3,10)           
draw_star(1,1,100)
mainloop()



