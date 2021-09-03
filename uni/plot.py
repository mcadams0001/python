# Execute this cell via Shift+Enter so that we can make some plots
import matplotlib.pyplot as plt
import numpy as np

def compound_by_period(balance, rate, num_periods):
    """
    Returns a list of balances by computing the compounded total,
    based on an initial balance and per-period interest rate over 
    the specified number of compounding periods
    
    balance: Initial amount
    rate: increase at each period (supply percentage in decimal form)
    num_periods: the number of periods to compound the balance
    """
    
    balances = [balance]
    for n in range(1,num_periods+1):
        balance = round( balance * (1 + rate), 2)
        balances.append(balance)
    return balances

# wheat: list containing the number of grains of wheat on each square of the chessboard

wheat = compound_by_period(1,1,63)
print(wheat)
print(len(wheat))
total_wheat = sum(wheat)
print(total_wheat)

t = np.arange(1, 63, 1)
print(len(t))
s = compound_by_period(1,63,1)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='square on chessboard', ylabel='number of grains on square',
       title='le18')
ax.grid()

fig.savefig("test.png")
plt.show()