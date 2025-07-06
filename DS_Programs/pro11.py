#you can use *args and ** kwargs to accept a variable number of arguements in function.

def total_sum(*numbers):
    result = 0
    for num in numbers:
        result += num
    return result

print(total_sum(1, 2, 3, 4))

