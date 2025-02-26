import pandas
import random

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


def currency(x):
    """Formats numbers as currency ($#.##)"""
    return "${:.2f}".format(x)


# main routine goes here


# initialise ticket numbers
MAX_TICKETS = 25
tickets_sold = 0

# initialise variables / non-default options for string checker
payment_ans = ('cash', 'credit')

# Ticket PRice List
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50

# Credit card surcharge (currently 5%)
CREDIT_SURCHARGE = 0.05

# lists to hold ticket details
all_names = []
all_ticket_costs = []
all_surcharge = []

mini_movie_dict = {
    'Name': all_names,
    'Ticket Price': all_ticket_costs,
    'Surcharge': all_surcharge
}
# Program main heading

# Ask user if they want to see the instructions
# display them if necessary
print()
want_instructions = string_check("DO you want to see the instructions")

if want_instructions == "yes":
    instructions()

print()
# Loop to get name, age and payment detail
while tickets_sold < MAX_TICKETS:
    # ask user for their name
    name = not_blank("Name: ")

    # if name is exit code, break out of loop
    if name == "xxx" and tickets_sold > 0:
        break
    elif name == "xxx":
        print("Oops, you need to sell at least one ticket.")
        print()
        continue

        # Aks for their age check it's between 12 and 120

    age = int_check("Age: ")

    # Output error message/ success message
    if age < 12:
        print(f"{name} is too young")
        continue
        #  Child ticket price is $ 7.50
    elif 12 <= age < 16:
        ticket_price = CHILD_PRICE

        # Adult ticket ($10.50)
    elif 16 <= age < 65:
        ticket_price = ADULT_PRICE

        # Senior Citizen ticket ($6.50)
    elif 65 <= age < 121:
        ticket_price = SENIOR_PRICE

    else:
        print(f"{name} is too old")
        continue

    # ask user for payment method (cash / credit / ca / cr)
    pay_method = string_check("Payment method: ", payment_ans, 2)
    print()

    if pay_method == "cash":
        surcharge = 0

        # if paying by credit, calculate surcharge
    else:
        surcharge = ticket_price * CREDIT_SURCHARGE

        # add name, ticket cost and surcharge to
    all_names.append(name)
    all_ticket_costs.append(ticket_price)
    all_surcharge.append(surcharge)

    tickets_sold += 1
# End of thicket Loop!

# create dataframe / table from dictionary
mini_movie_dict = pandas.DataFrame(mini_movie_dict)

# calculate the total payable for each ticket
mini_movie_dict['Total'] = mini_movie_dict['Ticket Price'] + mini_movie_dict['Surcharge']
mini_movie_dict['Profit'] = mini_movie_dict['Ticket Price'] - 5

# Work out total paid and total profit...
total_paid = mini_movie_dict['Total'].sum()
total_profit = mini_movie_dict['Profit'].sum()

# Currency Formatting (uses currency functions)
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_dict[var_item] = mini_movie_dict[var_item].apply(currency)

# Output movie frame without index
print(mini_movie_dict.to_string(index=False))

print()
print(f"Total Paid: ${total_paid}")
print(f"Total Profit: ${total_profit:.2f}")


# Choose random winner...
winner = random.choice(all_names)

# find index of winner (ie: position in list)
winner_index = all_names.index(winner)
print("winner", winner, "list position", winner_index)

# retrieve ticket price and surcharge

winner_ticket_price = all_ticket_costs[winner_index]
winner_surcharge = all_surcharge[winner_index]

# FInd total won
total_won = winner_ticket_price + winner_surcharge

# winner announcement
print(f"The lucky winner is {winner}. Their ticket worth $ {total_won:.2f} is free!")


if tickets_sold == MAX_TICKETS:
    print(f"you have sold all the tickets (ie: {MAX_TICKETS} tickets)")
else:
    print(f"You have sold {tickets_sold} / {MAX_TICKETS} tickets.")
