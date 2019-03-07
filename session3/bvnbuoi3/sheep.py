print('Hello, my name is Hai and these are my sheep')
flock = [5,7,300,90,24,50,75]
print(flock)

biggest = max(flock)
print('Now my biggest sheep has size',biggest, 'lets shear it' )

biggest_pos = flock.index(max(flock))
flock[biggest_pos]=8
print('After shearing, here is my flock,',flock )

for i in range(1,4):
    flock = [x+50 for x in flock]
    print('MONTH',i)
    print('One month has passed, now here is my flock',flock)
    biggest = max(flock)
    print('Now my biggest sheep has size',biggest,'let sheer it')
    biggest_pos = flock.index(max(flock))
    flock[biggest_pos] = 8
    print('After sheering, here is my flock',flock)


print('My flock has size in total:',sum(flock))
print('I would get',sum(flock),'* 2$', sum(flock)*2,'$')