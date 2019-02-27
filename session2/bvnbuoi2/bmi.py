height = float (input("Chiều cao của bạn là: (cm)"))
weight = float (input("Cân nặng của bạn là: (kg)"))

height= height/100

bmi = weight / (height * height)

print("Chỉ số BMI của bạn là: ",bmi)

if bmi<16:
    print(" Severely underweight ")
elif 16 < bmi < 18.5:
    print(" Underweight ")
elif 18.5 < bmi < 25:
    print(" Normal ")
elif 25 < bmi < 30:
    print(" Overweight ")
else:
    print(" Obese ")
