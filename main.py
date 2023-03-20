from ascii import logo
import pandas as pd

data = pd.read_csv('morse_code.csv')
# converting morse csv data into a dictionary with {alphanumeric:morse} {key:value} pairs.
MORSE_CODE_DICT = {row.char: row.code for (index, row) in data.iterrows()}

# adding space ' ' character to morse dictionary.
MORSE_CODE_DICT[' '] = ' '

# display ascii art logo
print(logo)


# function to take alphanumeric message and append corresponding morse code to a list.
def new_message():
    message = input('Please enter your message to be encoded here:\n')
    message_chars = list(message.upper())
    for x in message_chars:
        morse_chars.append(MORSE_CODE_DICT[x])


# continues while loop for future message encoding.
morse_machine_on = True

while morse_machine_on:
    # empty list to receive morse characters.
    morse_chars = []
    try:
        new_message()
        # converts morse list into a string and prints out.
        morse_string = ' '.join(morse_chars)
        print(f'\nYour message in morse code is as follows:\n{morse_string}')
    # catches key errors for characters not contained in the morse dictionary.
    except KeyError as error_message:
        print(f'The character {error_message} cannot be translated into morse code. Please try again.\n')
    else:
        # Gives user choice to continue creating new messages or end program.
        if input('\nWould you like to create another morse code message?y/n\n').upper() == 'N':
            morse_machine_on = False
            print('Bye, thanks for encoding!')




