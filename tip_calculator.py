def calculate_tip(tip_percentage):
    tip_amount = bill_amount * ( tip_percentage / 100 )
    return tip_amount

while True:
    try:
        bill_amount = float(input("What is the bill amount? "))
        tip_percentage = float(input("What is the tip amount? "))

        if bill_amount < 0 or tip_percentage < 0:
            print("You can not enter negative numbers!")
            continue

        break
    except:
        print("Your input must be a valid number!")
        continue

tip_amount = calculate_tip(tip_percentage)
bill_with_tip = bill_amount + tip_amount

print( f"The tip is ${tip_amount:.2f}" )
print( f"The total bill is ${bill_with_tip:.2f}" )
