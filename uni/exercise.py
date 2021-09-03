
balance = 100.0
rate = 0.03
num_periods = 10

print(0, round(balance,2))
for n in range(1,num_periods):
    balance = round(balance * (1 + rate), 2)
    print(n, round(balance,2))
    
balance = 100.0    

def compound(balance, rate, num_periods):
    current_balance = round(balance,2)
    print(0, current_balance)
    for n in range(1,num_periods):
        current_balance = round(current_balance * (1 + rate), 2)
        print(n, current_balance)
    return current_balance

def compound_by_period(balance, rate, num_periods):
    """
    Calculates the compound balance after number of periods for given interest rate
    """
    balances = []
    current_balance = round(balance,2)
    print(0, current_balance)
    balances.append(current_balance)
    for n in range(1,num_periods):
        current_balance = round(current_balance * (1 + rate), 2)
        print(n, current_balance)
        balances.append(current_balance)
    return balances

def change_per_period(balances):
    change = []
    for i in range(1,len(balances)):
        change.append(round(balances[i]-balances[i-1],2))
    return change

print("--- compound initial balance:", balance)
compound(balance, rate, num_periods)

print("--- compound_by_period initial balance", balance)
balances = compound_by_period(balance, rate, num_periods)
print(balances)

print("--- change_per_period initial balance", balance)
print(change_per_period(balances))

print("--- wheat")
wheat =compound_by_period(1, 1, 64)
print(wheat)
total_wheat=sum(wheat)
print(total_wheat)
print(18446744073709551615==total_wheat)
