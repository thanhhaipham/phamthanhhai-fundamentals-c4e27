price = {'banana':4,'apple':2,'orange':1.5,'pear':3}
stock = {'banana':6,'apple':0,'orange':32,'pear':15}

tong=0
for i in price:
    tong = tong + (price[i] * stock[i])
print(tong)
