sum = 0
q = "quit"
while True:
    Number = input("Enter the Price (type 'quit' to exit): ")
    if Number.lower() != q:
        Number = int(Number)
        sum += Number
    else:
        print("Your Total Price is:", sum)
        print("Thanks For Using Kirana Cal")
        break
