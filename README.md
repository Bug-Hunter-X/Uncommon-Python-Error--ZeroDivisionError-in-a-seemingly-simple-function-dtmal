# Uncommon Python Error: ZeroDivisionError

This repository demonstrates an example of a ZeroDivisionError in Python. While common, the error can sometimes be subtle and requires careful review of the program logic to solve it.

## Bug Description

The function `function_with_uncommon_error` attempts a division by zero if the input `a` is 0. This leads to a `ZeroDivisionError` runtime exception. Standard exception handling can easily solve this issue but is not always the best approach as it can mask more serious logic flaws.

## Solution

The solution file adds exception handling to gracefully catch the `ZeroDivisionError` and prevent the program from crashing. Better still, it adds checks to prevent the division by zero in the first place.