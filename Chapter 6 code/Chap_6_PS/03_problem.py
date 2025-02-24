p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click"

message = input("Enter your comments: ")
if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("Spam detected")
else:
    print("Spam not detected")