import math

def print_series(n):

    # enter the number of element in series

    first_num = -5

    for i in range(n):
        
        print(first_num)
        first_num +=5

    return 

if __name__ == "__main__":

    entered_number = int(input('Enter Number\n'))
    
    print_series( entered_number )