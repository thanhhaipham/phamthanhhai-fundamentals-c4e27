print('If x=8, then what is the value of 4(x + 3)?')
ans1 = {'1':35,'2':36,'3':40,'4':44}
for i in ans:
    print(i,ans[i])
dapan = int(input("Your answer is: "))
if dapan == 4:
    print('Bingo')
elif dapan in [ 1,2,3]:
    print('Wrong')
else:
    print('Syntax Error, choose again!')