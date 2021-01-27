#codigo exibido na aula de Python do professor Renato Souza/FGV
def fib_otz(n):
    if n < 2:
        return n
    a,b = 1,0
    for i in range(n):
        a,b = b, a+b        
    return b

print(fib_otz(10000))
