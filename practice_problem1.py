# print("hello world")

a = 5 
b = 6

print(a+b)

# print("hello world")

a = 5 
b = 6
print(a+b)

n = 5 
for i in range(1, 11):
    print(f"{n} x {i} = ", n*i)

# P (Principle) = initial amount borrowed
# r (Rate) = Annual Rate 
# t (Time) =  Time period in years

def simple_interest(P, r, t):
    r = r/100
    SI = P*r*t
    return SI

a = simple_interest(10000, 5, 3)
print(a)
