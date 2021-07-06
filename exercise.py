
balance = 100.0
rate = 0.03

print(0, round(balance,2))
for n in range(1,11):
    balance = round(balance * (1 + rate), 2)
    print(n, round(balance,2))
    
def compound(balance, rate, num_periods):
    current_balance = balance
    print(0, round(current_balance,2))
    for n in range(1,num_periods):
        current_balance = round(current_balance * (1 + rate), 2)
        print(n, current_balance)
    return current_balance

def compound_by_period(balance, rate, num_periods):
    balances = []
    current_balance = balance
    print(0, round(current_balance,2))
    balances.append(current_balance)
    for n in range(1,num_periods):
        current_balance = round(current_balance * (1 + rate), 2)
        print(n, current_balance)
        balances.append(current_balance)
    return balances

def change_per_period(balances):
    change = []
    for i in range(1,len(balances)):
        change.append(balances[i]-balances[i-1])
    return change

print("--- compound")
compound(100.0, 0.03, 11)

print("--- compound_by_period")
print(compound_by_period(100.0, 0.03, 11))

print("--- wheat")
wheat =compound_by_period(1, 1, 64)
print(wheat)
total_wheat=sum(wheat)
print(total_wheat)
print(18446744073709551615==total_wheat)
