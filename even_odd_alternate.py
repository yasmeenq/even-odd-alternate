def even_odd_even(n):
    if type(n) is not int:
        raise ValueError("n must be a number.")

    n = str(abs(n))  #convert the number to a string and to positive if negative 
    if len(n) <= 1:  #if the number is 1 digit or less, return false
        return False
    
    x = 0
    while x < len(n):    
        if int(n[x]) % 2 == 1:
            if not int(n[x+1]) %2 == 0:
                return False
        elif int(n[x]) % 2 == 0:
            if not int(n[x+1]) %2 == 1:
                return False
        x += 1
        return True
try:
    print(even_odd_even(1234567892))  #true
    print(even_odd_even(6789)) #true
    print(even_odd_even(5555))  #false
    print(even_odd_even(2222222222))  #false
    print(even_odd_even(3))  #false
    print(even_odd_even(-6789)) #true (will convert it to positive)

#exception handeling
except ValueError as e:
    print("==value error==", e)
except Exception as e:
    print("===General error===", e)
