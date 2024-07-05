#iterative implementation to calculate factorial.

#n: int
number = int(input('please enter a number: ')) 

#subroutine to iterate
def iterative_factorial(n):
    answer = 1
    for i in range(1,n+1):
        answer = answer * i
    return answer 

print(iterative_factorial(number))

