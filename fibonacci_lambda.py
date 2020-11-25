"""Fibonacci Lambda"""

fibon = lambda x,f: f(x-1, f) + f(x-2, f)  if(x>1) else( 0 if(x<=0) else 1)
print( fibon(40, fibon) )
