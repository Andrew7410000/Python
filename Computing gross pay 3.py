hrs = input("Enter Hours:")
fhrs = float(hrs)
rate = input("Enter Rate:")
frate = float(rate)

def computepay(h, r):
    fr = float(r)
    fh = float(h)
    if fr < 0:
        return "Error"
    elif fh < 0:
        return "Error"
    elif fh < 40:
        return fh * fr
    elif fh > 40:
        return ((fh - 40) * (fr * 1.5)) + (40 * fr)
    else:
        print ("NaN")

p = computepay(hrs, rate)
print("Pay", p)