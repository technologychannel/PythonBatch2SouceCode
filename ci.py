# It Calculate Compound Interest
### Needed Things
# Principal Amount
# Time in years
# Rate of Interest
# Number of times interest applied per time period

p = float(input("Enter the principal amount: "))
t = float(input("Enter the time in month: "))/12
r = float(input("Enter the rate of interest: "))
n = float(input("Enter the number of times interest applied per time period: "))
coumpound_interest = p * (1 + r/n) ** (n*t)
print(f"Compound Interest is {coumpound_interest:.2f}")

