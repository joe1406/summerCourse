
def prime_checker():
    Finished = 'yes'
    while Finished == 'yes':
        integer = int(input('please enter a number to check if its prime or not: '))
        if integer <= 1:
            print('try again, the number is not greater than 1')
        else:
            remainders = []
            for i in range(2,integer//2 + 1):
                remainders.append(integer%i)
            if all(remainders) != 0:
                print('this number is a prime')
            else:
                print('this number is not a prime')
            Finished = input('do you want to input another integer? (yes/no) ')

prime_checker()

