# functions go here

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


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        # uses 'strip' to remove whitespace before / after
        response = input(question).strip()

        if response != "":
            return response

        print("sorry, this can't be blank. Please try again./n")


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


# main routine goes here

# initialise variables / non-default options for string checker
payment_ans = ('cash', 'credit')

print()
while True:
    print()

    # ask user for their name
    name = not_blank("Name: ")

    # Aks for their age check it's between 12 and 120
    age = int_check("Age: ")

    # Output error message/ success message
    if age < 12:
        print(f"{name} is too young")
        continue
    elif age > 120:
        print(f"{name} is too old")
        continue
    else:
        pass
    # ask user for payment method (cash / credit / ca / cr)
    pay_method = string_check("Payment method: ", payment_ans, 2)
    print(f"{name} has bought a ticket  ({pay_method})")



