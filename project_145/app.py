pali = input("Enter a palindrome, please: ")
palilength=len(pali)
slicer=pali[palilength::-1]

if pali == slicer:
    print("It is a palindrome")
else:
    print("Enter a valid palindrome please.")