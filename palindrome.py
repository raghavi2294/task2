string=input("Enter a String:")
rev = string[::-1]

if string == rev:
    print(rev + " is Palindrome")
else:
    print(rev + " is not Palindrome")