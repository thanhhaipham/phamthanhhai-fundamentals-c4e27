#7+8
def remove_dollar_sign(s):
    snd = s.replace('$','')
    return snd
i = input("Nhap chuoi: ")
print('Chuoi sau khi xoa ki tu $: ',remove_dollar_sign(i))
string_with_no_dollars = remove_dollar_sign("$80% percent of $life is to show $up")
if string_with_no_dollars == "80% percent of life is to show up":
    print("Your function is correct")
else:
    print("Oops, there's a bug")

#9+10
def get_even_list(l):
    daysochan=[]
    for i in range(len(l)):
        if l[i]%2==0:
            daysochan.append(l[i])
    return daysochan
print(get_even_list([1,4,5,-1,10]))
even_list = get_even_list([1, 2, 5, 9, -10, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")

# 11 diem-hcn
def is_inside(a,b):
    if b[0]<a[0]<b[0]+b[2] and b[1]<a[1] < b[1]+b[3]:
        return True
    else:
        return False

print(is_inside([200,120],[140,60,100,200]))

