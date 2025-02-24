import pandas


# lists to hold ticket details
all_names = ["A", "B", "C", "D", "E"]
all_ticket_costs = [7.50, 7.50, 10.50, 10.50, 6.50]
all_sruchage =[0, 0, 0.53, 0.53, 0]

mini_movie_dict = {
    'Name': all_names,
    'Ticket Price': all_ticket_costs,
    'Surcharge': all_sruchage
}


# create dataframe / table from dictionary
mini_movie_dict = pandas.DataFrame(mini_movie_dict)


# calculate the total payable for each ticket
mini_movie_dict['Total'] = mini_movie_dict['Ticket Price'] + mini_movie_dict['Surcharge']
mini_movie_dict['Profit'] = mini_movie_dict['Ticket Price'] - 5

# Work out total paid and total profit...
total_paid = mini_movie_dict['Total'].sum()
total_profit = mini_movie_dict['Profit'].sum()

print(mini_movie_dict)
print()
print(f"Ttal PAid: ${total_paid}:.2f")
print(f"Total Profit: ${total_profit:.2f}")









