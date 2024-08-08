# programme to make a simple calculator using simple python operators
#!/usr/bin/pyhton3

# ask user to enter 2 number 
num1, num2 = input("Enter the two numbers: ").split()

# convert string into regular number
num1 = int(num1)
num2 = int(num2)

# add the two number and asign to sum 
sum = num1 + num2
# subtract two numbers and asign to difference

difference = num1 - num2

# multiply two numbers adn asign to mult

mult = num1 * num2 

# divide two numbers and asign to div

div = num1 / num2

# use floor division and asign to floordiv

floordiv = num1 // num2

# use modulo operator for the two number and asign to remainder

remainder = num1 % num2
# print result

print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, mult))
print("{} / {} = {}".format(num1, num2, div))
print("{} // {} = {}".format(num1, num2, floordiv))
print("{} % {} = {}".format(num1, num2, remainder))
