print("Escriu el primer numero: ")
num1 = input()
print("Escriu el segon numero: ")
num2 = input()
if (num1 > num2):
    txt = "El num més gran és: {nums}!"
    print(txt.format(nums = num1))
elif (num2 > num1):
    txt = "El num més gran és: {nums}!"
    print(txt.format(nums = num2))
    