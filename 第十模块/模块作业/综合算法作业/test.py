

def count(number):
    if number <= 0:
        return 0 
    return number + count(number-1)

print(count(100))


def count1(number):
    if number > 0:
        return number + count1(number-1)
    else:
        return 0 

print(count1(100))

def tail_recursion(n,total=0):
    if n == 0:
        return total
    else:
        return tail_recursion(n-1,total+n)

print(tail_recursion(100))