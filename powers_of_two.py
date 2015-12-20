terms = int(input("Enter number of terms : "))

result = list(map(lambda x: 2 ** x, range(terms)))

for i in range(terms):
   print("2 to the power {0} is {1}".format(i, result[i]))
