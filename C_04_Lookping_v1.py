
# initialise ticket numbers
MAX_TICKETS = 10
tickets_sold = 0

while tickets_sold < MAX_TICKETS:
    name = input("Name: ")

    # if name is exit code, break out of loop
    if name == "XXX":
        break

    tickets_sold +=1
if tickets_sold == MAX_TICKETS:
    print(f"you have sold all the tickets (ie: {MAX_TICKETS} tickets)")
else:
    print(f"You have sold {tickets_sold} / {MAX_TICKETS} tickets.")




