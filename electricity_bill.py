def units_cost(units):
    return units * 5

def fixed_charge():
    return 60

def total_bill(units):
    return units_cost(units) + fixed_charge()

units = 100

print("Units:", units)
print("Units Cost:", units_cost(units))
print("Fixed Charge:", fixed_charge())
print("Total Bill:", total_bill(units))