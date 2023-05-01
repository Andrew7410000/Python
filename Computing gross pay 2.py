hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
x = float(40)
if h > x:
  pay = ((h - x) * (r * 1.5)) + (x * r)
else: 
  pay = h * r
print(pay)