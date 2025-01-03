import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as si
import mplfinance as mpf
import plotly.graph_objects as go
from datetime import datetime

class BlackScholesModel:
    def __init__(self, S, K, T, r, sigma):
        self.S = S        # Underlying asset price
        self.K = K        # Option strike price
        self.T = T        # Time to expiration in years
        self.r = r        # Risk-free interest rate
        self.sigma = sigma  # Volatility of the underlying asset

    def d1(self):
        return (np.log(self.S / self.K) + (self.r + 0.5 * self.sigma ** 2) * self.T) / (self.sigma * np.sqrt(self.T))
    
    def d2(self):
        return self.d1() - self.sigma * np.sqrt(self.T)
    
    def call_option_price(self):
        return (self.S * si.norm.cdf(self.d1(), 0.0, 1.0) - self.K * np.exp(-self.r * self.T) * si.norm.cdf(self.d2(), 0.0, 1.0))
    
    def put_option_price(self):
        return (self.K * np.exp(-self.r * self.T) * si.norm.cdf(-self.d2(), 0.0, 1.0) - self.S * si.norm.cdf(-self.d1(), 0.0, 1.0))
    
    #Greeks calculus
class Greeks(BlackScholesModel):
    def delta_c(self):
        return si.norm.cdf(self.d1())
    def gamma(self):
        return si.norm.pdf(self.d1())/(self.sigma*self.S*np.sqrt(self.T))
    def theta_c(self):
        return -self.S*self.sigma*si.norm.pdf(self.d1())/(2*np.sqrt(self.T))
    def vega(self):
        return self.S*np.sqrt(self.T)*si.norm.pdf(self.d1())
    def rho_c(self):
        return self.K*self.T*np.exp(-self.r*self.T)*si.norm.cdf(self.d2()) 
