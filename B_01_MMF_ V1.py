# functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start and End"""

    print(f"{decoration * 3} {statement} {decoration * 6}")


make_statement("Mini-Movie-fundraiser", decoration="🕷")


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
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_answers}")


def instructions():
    make_statement("instructions", "🩻")

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


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        # uses 'strip' to remove whitespace before / after
        response = input(question).strip()

        if response != "":
            return response

        print("sorry, this can't be blank. Please try again./n")


def int_check(question):
    """Checks users enter an integer"""

    error = "Oops - Please enter an integer."

    while True:

        try:
            # Return the response if it" an integer
            response = int(input(question))

            return response

        except ValueError:
            print(error)


# main routine goes here


# initialise ticket numbers
MAX_TICKETS = 5
tickets_sold = 0

# initialise variables / non-default options for string checker
payment_ans = ('cash', 'credit')

print()
want_instructions = string_check("DO you want to see the instructions")

if want_instructions == "yes":
    instructions()

print()
while tickets_sold < MAX_TICKETS:
    # ask user for their name
    name = not_blank("Name: ")

    # if name is exit code, break out of loop
    if name == "xxx" and tickets_sold >0:
        break
    elif name == "xxx":
        print("Oops, you need to sell at least one ticket.")
        print()
        continue

        # Aks for their age check it's between 12 and 120

    age = int_check("Age: ")

    # Output error message/ success message
    if age < 12:
        print(f"{name}, Sorry you are too young for this movie")
        continue
    elif age > 120:
        print(f"{name} ?? THat looks like a typo (too old?)")
        continue
    else:
        pass
    # ask user for payment method (cash / credit / ca / cr)
    pay_method = string_check("Payment method: ", payment_ans, 2)
    print(f"{name} has bought a ticket  ({pay_method})")
    print()

    tickets_sold += 1
if tickets_sold == MAX_TICKETS:
    print(f"you have sold all the tickets (ie: {MAX_TICKETS} tickets)")
else:
    print(f"You have sold {tickets_sold} / {MAX_TICKETS} tickets.")
