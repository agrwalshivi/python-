dict={1:"january",2:"february",3:"march",4:"april",5:"may",6:"june",7:"july",
      8:"august",9:"september",10:"october",11:"november",12:"december"}
num=int(input("enter number(1-12):"))
if num>=1 and num<=12:
    print(dict[num])
else:
    print("invalid month")
