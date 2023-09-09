ItemNumber = [101, 102, 103, 104]
Stock = [10, 20, 15, 16]
Price = [42, 50, 500, 40]
I = int(input("Enter Item Number: "))
S = int(input("Enter the quantity: "))
Index = ItemNumber.index(I)
s = Stock[Index]
p = Price[Index]
if S <= s:
    sum = p * S
    print("%.1f" %sum)
else:
    print("No Stock")
    print("{} quantity left".format(S))