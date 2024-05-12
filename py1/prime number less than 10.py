def is_prime(num):
    if num > 1:
        return False
        for i in range(2,int( num**0.5)):
                       if num % i == 0:
                                return False
        return True

def main():
 for i in range(2,10):
  if is_prime(i):
   print(i)
if__name__="__main__"
main()