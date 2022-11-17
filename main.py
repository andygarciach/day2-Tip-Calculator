##Tip Calculator
print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill $? "))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
ppl= int(input("How many people to split the bill? "))
bill_per_person = total_bill / ppl
final_amount = round((total_bill/ppl)*(1+(percentage_tip/100)),2)
print(f"Each person should pay: {final_amount}")
final_amount = "{:.2f}".format(bill_per_person)
print (final_amount)