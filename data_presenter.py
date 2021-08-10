# invoices = open('CupcakeInvoices.csv')
# # for invoice in invoices:
# #     print(invoice)
# #     print(type(invoice))
# all_equals = 0
# chocolate_cake = []
# strawberry_cake = []
# vanilla_cake = []
# for total in invoices:
#     total = total.rstrip('\r\n').split(',')
#     last = float(total[-1])
#     second_last = int(total[-2])
#     mult = last * second_last
#     all_equals += mult
#     print(all_equals)
    
# invoices.cancle()
                  

import matplotlib.pyplot as plt

cupcake_invoices = open('CupcakeInvoices.csv')

chocolate_price = 0
strawberry_price = 0
vanilla_price = 0 

for line in cupcake_invoices:
    line = line.rstrip('\r\n').split(',')
    if line[2] == "Chocolate":
        chocolate_price += round(int(line[3]), float(line[4]))
    elif line[2] == "Strawberry":
        strawberry_price += round(int(line[3]), float(line[4]))
    elif line[2] == "Vanilla":
        vanilla_price += round(int(line[3]), float(line[4]))

data = {
    "Chocolate": chocolate_price,
    "Strawberry": strawberry_price,
    "Vanilla": vanilla_price
}

courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize=(10,5))

plt.bar(courses, values, color='maroon', width=0.4)

plt.xlabel("Types of cupcakes")
plt.ylabel("total sales")
plt.title("Total Cupcakes sales")
plt.show()


# i could not get my matplotlib to work. I think becuase mac comes with python but after updating python there are two and im trying to pull matlablib out of the wrong file and cant figure out how to pull out of the other file. after a couple hours of tryingn im pushing it to github