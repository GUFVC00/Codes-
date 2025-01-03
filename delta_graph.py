from BSM_GREEKS_CLASSES import BlackScholesModel,Greeks
import matplotlib.pyplot as plt
x = []
y = []
x2 = []
y2 = []
for i in range(100):
    bsm = BlackScholesModel(S=50+i, K=100, T=1, r=0.05, sigma = 0.1)
    bsg = Greeks(S=50+i, K=100, T=1, r=0.05, sigma=0.1)
    y.append(bsg.delta_c())
    x.append(50+i)
    x2.append(50+i)
    y2.append(bsm.call_option_price())

    
plt.figure(figsize=(10, 5))
plt.plot(x, y)
plt.title('Delta of a Call Option as Underlying Price Changes')
plt.xlabel('Stock Price')
plt.ylabel('Delta')
plt.grid(True)
plt.show()

plt.figure(figsize=(10,5))
plt.plot(x2, y2)
plt.title('Option as Underlying Price Changes')
plt.xlabel('Stock Price')
plt.ylabel('Option')
plt.grid(True)
plt.show()