def collatz(number):
    if number%2==0:
        print(number//2)
        return number//2
    else:
        print(number*3+1)
        return 3*number+1
e=input()
try:
    e=int(e)
    while True:
        e=collatz(e)
        if e==1:
            break
except ValueError:
    print("User must enter an integer")
        
    
