def sayhi(name, age):
    print("Hello " + name + "! You are " + age)
sayhi("Mike", "35")

def cube(num):
    return num*num*num

result = cube(4)
print(result)

is_male = False
is_tall = False
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("you are a short male")
elif not(is_male) and is_tall:
    print("you are not a male but tall")
else:
    print("You are neither a male nor tall")

def max_num(num1,num2,num3):
    if num1>=num2 and num1 >=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3
result=max_num(18,108,45)
print(result)