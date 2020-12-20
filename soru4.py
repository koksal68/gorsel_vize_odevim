def compareDigits(num3digit):
    hunds = int(num3digit / 100)
    tens = int((num3digit % 100) / 10)
    ones = int(num3digit % 10)

    if hunds != tens and hunds != ones and tens != ones:
        print(hunds, tens, ones, sep='')

for num3digit in range(100, 1000):
	compareDigits(num3digit)