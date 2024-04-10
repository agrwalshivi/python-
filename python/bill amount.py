qty=int(input("enter no of items sold:"))
val=int(input("enter price of 1 item:"))
disc=int(input("ehter discount %:"))
tax=int(input("enter tax %:"))
total=qty*val
disc_amt=total*(disc/100)
taxable=total-disc_amt
tax_amt=total*(tax/100)
final=taxable+tax_amt
print("total amount:",final)
