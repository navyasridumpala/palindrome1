def is_palindrome(num):
    original_num = num
    reverse_num = 0

    while num != 0:
        digit = num % 10
        reverse_num = reverse_num * 10 + digit
        num //= 10

    return original_num == reverse_num

# Test the function
num = int(input("Enter a number: "))
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")

