e12 = [1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2]
allValues = []
for i in range(7):
    for r in e12:
        allValues.append(round(r * (10 ** i), 1))
print(allValues)