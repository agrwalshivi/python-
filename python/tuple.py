tuple1=("monday","tuesday","wednesday","thursday","friday","saturday","sunday")
val=int(input("enter number (0-6):"))
if val>=0 and val<=6:
    print("value on index number",val,"is:",tuple1[val])
else:
    print("invalid number:")
