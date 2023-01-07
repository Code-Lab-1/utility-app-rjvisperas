import datetime
#our item
items = ["Lays Chips", "Pringles Chips", "Fritos Chips", "Doritos Chips", "Ruffles Chips", "Tostitos Chips", "Coke", "Pepsi", "Mountain Dew", "Fanta", "Sprite"]
prices = [3.50, 7.50, 3.50, 5.50, 2.50, 2.50, 2.50, 2.50, 2.50, 2.50, 2.50]
stock = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
#take order
def take_order():
  order = []
  total_cost = 0
  print("\t****VENDING MACHINE**\t")
  print("Please make your selection:")
  print("-----------------------------")
  while True:
    print("1. Chips")
    print("2. Drinks")
    print("3. Finish order")
    category = int(input())
    if category == 1:
      print("----------Which type of chips would you like?----------")
      for i in range(6):
        print(str(i+1) + ": " + items[i] + " - AED " + str(prices[i]) + " - Stock: " + str(stock[i]))
      selection = int(input())
      if stock[selection - 1] > 0:
        order.append(selection)
        total_cost += prices[selection - 1]
        stock[selection - 1] -= 1
        print("----------Added " + items[selection - 1] + " to order----------")
      else:
        print("----------Sorry, this product is out of stock----------")
    elif category == 2:
      print("----------Which drink would you like?----------")
      for i in range(6, len(items)):
        print(str(i+1) + ": " + items[i] + " - AED " + str(prices[i]) + " - Stock: " + str(stock[i]))
      selection = int(input())
      if stock[selection - 1] > 0:
        order.append(selection)
        total_cost += prices[selection - 1]
        stock[selection - 1] -= 1
        print("----------Added " + items[selection - 1] + " to order----------")
      else:
        print("----------Sorry, this product is out of stock----------")
    elif category == 3:
      break
  return order, total_cost
#dispensing item
def dispense_product(selection):
  print("Dispensing " + items[selection - 1] + "...")
#make suggestion
def make_suggestion(order):
  if 1 in order or 2 in order or 3 in order or 4 in order or 5 in order or 6 in order:
    print("----------You might also enjoy a drink with your chips----------")
  if 7 in order or 8 in order or 9 in order or 10 in order or 11 in order:
    print("----------You might also enjoy chips with your drink----------")
# to complete payment
def p_payment(total_cost):
  print("----------Please insert AED " + str(total_cost) + " to complete your purchase----------")
  payment = float(input())
  if payment < total_cost:
    print("Insufficient payment. Please insert an additional  " + str(total_cost - payment))
    payment += float(input())
  if payment >= total_cost:
    print("----------Thank you for your purchase!----------")
    print_receipt(order, total_cost, payment)
  else:
    print("----------Canceling transaction----------")
#print receipt
def print_receipt(order, total_cost, payment):
  current_time = datetime.datetime.now().strftime("%m/%d/%Y %I:%M %p")
  print("--- Receipt ---")
  print("Date: " + current_time)
  print("Products: " + str(order))
  print("Total cost:  " + str(total_cost))
  print("Payment:  " + str(payment))
  print("Change:  " + str(payment - total_cost))
  print("---------------")

order, total_cost = take_order()
make_suggestion(order)
p_payment(total_cost)