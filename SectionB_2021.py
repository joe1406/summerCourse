def harshad_checker(n):
    sum = 0

    for digits in str(n):
        sum += int(digits)
    
    if n % sum == 0:
        return True
    else:
        return False

def nth_harshad_number():
    n = int(input('enter a number, n, and will then the program will calculate the nth Harshad Number: '))
    numbers = []
    start = 1
    while len(numbers) < n:
        if harshad_checker(start):
            numbers.append(start)
        start += 1
    
    print(numbers[n-1])



        

