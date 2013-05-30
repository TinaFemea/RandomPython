__author__ = 'tina'

is_even = raw_input("What number would you like me to check?  ")
while not is_even.isdigit():
    is_even = raw_input("Error: Please enter a number in the form of '1', '2', etc.  ")

def even(checked_number):
    i = int(checked_number)
    if i % 2:
        print "%d is even." % i
    else:
        print "%d is not even." % i

print even(is_even)