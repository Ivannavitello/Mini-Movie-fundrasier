# functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start and End"""

    print(f"{decoration * 3} {statement} {decoration * 3}")


make_statement("Programing is cool and Fun", decoration=3)



def string_check(question, valid_answers=('yes', 'no'),
                 num_letters=1):
    """Checks that users enter the full word
    or the 'n' letter/s of a word  from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_answers:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the first letter
            elif response == item[num_letters]:
                return item

        print(f"Please choose an option from {valid_answers}")


def instructions():
    make_statement("instructions" , "🩻")

    print('''

For each ticket holder enter ...
- Their name
-Their age
- The payment method (cash / credit)

THe program will record the ticket sale and calculate the ticket cost (and the profit).

Once you have either sold all of the tickets or entered the 
exit code ('xxx'), the program will display the ticket sales information and 
write the data to a text file.

It will also choose one lucky ticket holder who wins the draw (their ticket is free).
''')


# main routine goes here
print()
want_instructions = string_check("DO you want to see the instructions")

if want_instructions =="yes":
    instructions()

print()
print("program continues.. ")
