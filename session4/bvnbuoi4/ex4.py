print('If x=8, then what is the value of 4(x + 3)?')
ans = {'1':35,'2':36,'3':40,'4':44}

true = 0

for i in ans:
    print(i,ans[i])
dapan = int(input('Your answer is: '))
if dapan == 4:
    true = true + 1
    print('Bingo')
elif dapan in [ 1,2,3]:
    print('Wrong')
else:
    print('Syntax Error, choose again!')
print('Jack scores these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean ?')
ans2 = {'1':'About 55','2':'About 65','3':'About 75','4':'About 85'}

for h in ans2:
    print(h, ans2[h])
dapan = int(input('Your answer is: '))
if dapan == 2:
    true = true +1
    print('Bingo')
elif dapan in [ 1,3,4]:
    print('Wrong')
else :
    print('Syntax Error, choose again!')
print('You correctly answer',true,'out of 2 questions')