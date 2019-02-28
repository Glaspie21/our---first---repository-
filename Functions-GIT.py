# 4.13.3: Greetings
# Ben Glaspie
# 2/6/19


name = input("what is your name: ")

def greeting():
    print("Hi there" + name + "!")
    print("Nice to meet you!")

greeting()


# 4.13.4: Functions and variables
# Ben Glaspie
# 2.14.19

x = 11

def print_something():
    x = 13
    print(x)


print_something()
print(x)


# 4.13.5: functions and Varibles part 2
# Ben Glaspie
# 1.13.19

my_variable = 3.6745

def something()

print(my_vairable)

print ssomething

#4.13.6: Functions and variables, part 3


def print_number(x):
    print(str(x))

Print_number(12)
print_number('Hello World')

#4.4.14 Name and age

def name_and_age(name, age):
    print('hi my name is ' + name + ' and I am ' +  str(age) + 'years old.')

name_and_age(Ben Glaspie, 16)
name_and_age(BILL, 999999999999999.1)


#4.14.5: defult peramiter values

def print_two_numbers(x, y = 20):
    print('first number: ', X)
    print('second number: ' + str(y))

    print_two_numbers