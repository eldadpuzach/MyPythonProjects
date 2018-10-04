# Program to illustrate a loop with condition in the middle.
# Take input from the user untill a vowel is entered

vowels = "aeiouAEIOU"

# infinite loop
while True:
    v = input('Enter vowel: ')
    #condition in the middle
    if v in vowels:
        break
    print("That's not a vowel. Try again!")
print('Thank You!')