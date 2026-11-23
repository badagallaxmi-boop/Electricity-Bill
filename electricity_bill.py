def units_cost(units):
    return units * 5

def fixed_charge():
    return 60

def total_bill(units):
    return units_cost(units) + fixed_charge()

def gst(amount):
    return amount * 5 / 100

def final_bill(units):
    return total_bill(units) + gst(total_bill(units))

units = 100

print("Units:", units)
print("Units Cost:", units_cost(units))
print("Fixed Charge:", fixed_charge())
print("Total Bill:", total_bill(units))
print("GST (5%):", gst(total_bill(units)))
print("Final Bill:", final_bill(units))
