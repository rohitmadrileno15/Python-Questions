import math


def number_is_prime(n):

   if n <= 1:
      return False

   elif n == 2:
      return True

   elif n > 2 and n % 2 == 0:
      return False

   else:

      for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

      return True
    
if __name__ == "__main__":

    entered_number = int(input('Enter Number\n'))
    
    for i in range(entered_number):

        if(number_is_prime(i)):
            print(i)
