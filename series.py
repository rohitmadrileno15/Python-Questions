import math

# -5,10,-15,20,-25

def print_series(n):

    # enter the number of element in series

    for i in range(1, n+1):
        print( int( math.pow( -1 , i) * 5 * i))

    return 

if __name__ == "__main__":

    entered_number = int(input('Enter Number\n'))
    
    print_series( entered_number )
