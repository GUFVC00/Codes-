# BSM and roots calculator 
import numpy as np
from scipy.stats import norm

N = norm.cdf   # cumalative distribution function
S = 100         # stock price
T = 1        # time 
sigma = 0.5    # volatility
r = 0.05         # risk
prec = 1e-5

K = 150        # strike
x0 = S/2
x1 =  S*2

      
def BS_CALL(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * N(d1) - K * np.exp(-r*T)* N(d2)


C = BS_CALL(S, K, T, r, sigma)
print('The price given is :',C)

def Ms(x1,x0,S,T,r,sigma):
     for i in range(10):
         fx1 = BS_CALL(S,x1,T,r,sigma) - C
         fx0 = BS_CALL(S,x0,T,r,sigma) - C
         x2 = x1 - fx1 *(x1 - x0)/(fx1-fx0) 
         fx2 = BS_CALL(S,x2,T,r,sigma)
         
         if abs(fx2- C)< prec:
             return x2
         
         x0 = x1
         x1 = x2
K = Ms(x1,x0,S,T,r,sigma)

print(K)