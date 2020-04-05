'''
#list

friends = ["Kevin","Karen","Jim","oscar","toby"]
print(friends[1:3])
friends[1]="Mike"
print(friends)
'''


''''
lucky_numbers = [4,8,815,16,23,42]
friends = ["Kevin","Karen","Jim","oscar","toby"]
friends.append("Creed")
friends.insert(1, "kelly")
friends.remove("Jim")
print(friends.index("Kevin"))
print(friends)
lucky_numbers.reverse()
friends2 = friends.copy()
print(friends2)
print(lucky_numbers)
'''
'''
#tuples

coordinates = [(4,5),(6,7),(80.35)]
print(coordinates[0])
'''

'''#function
def say_hi(name,age):
    print("Hello "+name+ ", you are "+str(age))

say_hi("Mike",35)
say_hi("Kevin",70)
'''

'''#end statement
def cube(num):
    return num*num*num

result = cube(4)
print(result)
'''

'''
#if statement
is_male = False
is_tall = True
if is_male or is_tall:
    print("You are male or tall or both")
else:
    print("You are neither male nor tall")

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not (is_tall):
    print("You are a short male")
elif not (is_male) and  is_tall:
    print("You are not male but are tall")
else:
    print("you are  not male and not tall")
'''

'''
#if statement & comparision

def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(30,6,5))
'''
'''
#dictionary
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Mar"])
'''

'''
#while loop
i = 1
while i <= 10:
    print(i)
    i=i+1
print("done with loop")

'''
'''
#for loop
friends = ["jim","karen","kevin"]

for index in range(2):
    if index ==0:
        print ("First iteration")
    else:
        print("not first")
'''

#exponent function
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result=result*base_num
    return result
print(raise_to_power(2,7))


