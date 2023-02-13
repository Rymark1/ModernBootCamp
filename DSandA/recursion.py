# recursion is a function calling itself over and over until it doesn't.
# An example of recursion is opening a gift box which should contain a ball.  However some prankster put within an
# unknown number of gift boxes.  To get to the ball, you will need to open the gift, to open another gift, to open
# another gift, to get the ball.
#
# def open_gift_box():
#     if ball:
#         return ball
#     open_gift_box()
#
# 2 important items to note:
#     The process of opening each new box is the same.
#     Each time we open a box, we make the problem smaller.
#
# The ball in this example is the Base Case -> or when the function will stop calling itself.
# The gift is the recursive case -> Continue calling the function until base case found.
# The base case must be actually possible and there must be a return statement.
#
# The Call Stack is similar to the stacks we previously used.  Each item that gets loaded onto the stack has to
# resolve in order to get to the next level down.  For recursion, that means each time we call the function, it gets
# added to the top of the call stack and must complete before any lower order item on the stack can perform.
# For example:
#
# def funcOne():     We add funcOne to the call stack, perform it and print out "One", then the funcOne on the call
#   print("One")     stack is removed.
#
# def funcOne():     We add funcOne to the call stack, Then we add funcTwo to the call stack, then complete/perform
#   funcTwo()        funcTwo, remove it from the call stack, then funcOne is the primary item on the call stack and
#   print("One")     gets performed printing out "One", then the funcOne on the call is removed.
#

def funcThree():
    print("Three")


def funcTwo():
    funcThree()
    print("Two")


def funcOne():
    funcTwo()
    print("One")


funcOne()


# We are going to make a function for factorial
def factorial(n):
    if n <= 1:
        return 1
    a = factorial(n - 1)
    return n * a


print(factorial(3))


# The way to view this is visualizing the call stack.
#
# factorial(4) gets loaded on the call stack.  It executes until it hits factorial(n-1) or factorial(3).  So:
# factorial(4)
# return 4 * factorial(4-1)
#               |
#            return 3 * factorial(3-1)
#                             |
#                        return 2 * factorial(2-1)
#                                         |
#                                    return 1  since n == 1
#
#  We then have a callstack that looks like this:
#  factorial(1)
#  factorial(2)
#  factorial(3)
#  factorial(4)
#
#  We then go back up the chain. Simplified looking like this:
#
# factorial(4) = 12
#                 |
#           return 4 * 6
#                      |
#                 return 3 * 2
#                            |
#                       return 2 * 1
#                                  |
#                              return 1


def find_first_uppercase_letter(s1):
    if s1 is None or s1 == '':
        return False
    a = ord(s1[0])
    if 65 <= ord(s1[0]) <= 90:
        return s1[0]
    b = s1[1::]
    return find_first_uppercase_letter(s1[1::])


print(find_first_uppercase_letter("testing this out"))
print(find_first_uppercase_letter("testing this Out"))
print(find_first_uppercase_letter("Testing this out"))
print(find_first_uppercase_letter("testing this ouT"))


def maxProfit(prices: list[int]) -> int:
    pass


