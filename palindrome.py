def isPalindrome(string: str) -> bool:
    leftIndex = 0
    rightIndex = len(string) - 1
    result = True

    while leftIndex < rightIndex:
        if string[leftIndex] != string[rightIndex]:
            return False
        leftIndex += 1
        rightIndex -= 1

    return True

# Test inputs
inputs = ["mam", "malayalam", "hello"]

for input_str in inputs:
    result = isPalindrome(input_str)
    if result:
        print(f'"{input_str}" is a palindrome.')
    else:
        print(f'"{input_str}" is not a palindrome.')


for input_str in inputs:
    result = isPalindrome(input_str)
    if result:
        print(f'"{input_str}" is a palindrome.')
    else:
        print(f'"{input_str}" is not a palindrome.')


def isPalindrome(int: int) -> bool:
    leftIndex =0
    rightIndex = True
    result = True

    while leftIndex < rightIndex:
        if int[leftIndex] != int[rightIndex]:
            return False
        leftIndex += 1
        rightIndex -= 1

    return True

inputs = [121, 13231, 11211, 123]
for input_int in inputs:
    result = isPalindrome(input_int)
    if result:
        print(f'"{input_int}" is a palindrome.')
    else:
        print(f'" {input_int}" is not a palindrome')

