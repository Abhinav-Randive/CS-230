def is_palindrome(word):

    lower_word = word.lower()
    return lower_word == lower_word[::-1]

word = "Python"
if is_palindrome(word):
    bool = True
    print("Yes, it is a palindrome")

else:
    bool = False
    print("No, this is not a palindrome")

