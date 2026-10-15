'''
program to check whether a character is a vowel or consonant.
'''
ch=(input('Enter the character='))
ch=ch.lower()
# Convert to lowercase to handle both uppercase and lowercase letters
if ch in ['a','e','i','o','u']:
        print(f'{ch} is vowel')
elif ch.isalpha():
        print(f'{ch}is consonant')
else :
        print('Invailed input ! please enter alphabet')