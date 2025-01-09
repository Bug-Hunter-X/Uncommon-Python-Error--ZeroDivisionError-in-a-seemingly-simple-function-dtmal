def function_with_uncommon_error(a, b):
    if a == 0:
        return 0 #Handle the case where a is 0
    else:
        return b / a

result = function_with_uncommon_error(0, 10) #result is now 0
print(result)

try:
    result = function_with_uncommon_error(0, 10)
    print(result)
except ZeroDivisionError:
    print("Error: Division by zero")