orders = [(102, "Ali"), (99, "Vali"), (150, "Sami")]

juft_orders = []  

for order in orders:
    raqam = order[0]  
    if raqam % 2 == 0:  
        juft_orders.append(order) 

print(juft_orders)
