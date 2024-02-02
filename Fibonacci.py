def fibonacci_generation():
    a,b = 0,1
    while True:
        yield a
        
        
        a,b = b,a+b
        
fibo=fibonacci_generation()
for i in range(9):
    print(next(fibo))


