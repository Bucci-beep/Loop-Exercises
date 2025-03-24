'''
Write a Python program that uses a for loop to calculate the compound interest over a specified number of years. The formula for compound interest is:
A=P×(1+rn)ntA = P \times \left(1 + \frac{r}{n}\right)^{nt}A=P×(1+nr)nt

'''

# Defining initial parameters
P = 1000       # Principal amount, e.g., $1000
r = 0.05       # Annual interest rate (5%)
n = 4          # Interest is compounded quarterly
t = 10         # Total number of years

#Initilize the amount with the principal
amount = P

# Loop over each year to calculate compound interest
for year in range(1, t +1):
    amount = amount * (1 + r/n) **n
    print(f"Year {year}: ${amount:.2f}")

