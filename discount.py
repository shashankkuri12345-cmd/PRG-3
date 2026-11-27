amount = float(input("Enter purchase amount: "))

if amount < 2000:
    discount = amount * 5 / 100
elif amount <= 5000:
    discount = amount * 10 / 100
else:
    discount = amount * 15 / 100

discounted_amount = amount - discount
gst = discounted_amount * 5 / 100
final_amount = discounted_amount + gst

print("Purchase Amount:", amount)
print("Discount:", discount)
print("GST:", gst)
print("Final Amount: Rs.", final_amount)