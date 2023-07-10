def is_palindrome(string):
    length = len(string)
    for i in range(length // 2):
        if string[i] != string[length - i - 1]:
            return False
    return True

string = "лепсспел"
result = is_palindrome(string)
print(result)  #True

string = "helloworld"
result = is_palindrome(string)
print(result)  #False
