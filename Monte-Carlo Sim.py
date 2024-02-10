import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

num_of_simulations = 100

def stock_monte_carlo(S0, mu, sigma, N=1000):
    result = []
    # number of simulation - possible S(t) realizations (of the process)
    for _ in range(num_of_simulations):
        prices = [S0]
        for _ in range(N):
            # we simulate the change day by day (t = 1)
            stock_price = prices[-1] * np.exp((mu - 0.5 * sigma**2) + sigma * np.random.normal())
            prices.append(stock_price)
        result.append(prices)
    simulation_data = pd.DataFrame(result)
    # the given columns will contain the time series ffor a given simulation
    simulation_data = simulation_data.T

    print(simulation_data)

if __name__ == '__main__':
    stock_monte_carlo(50, 0.0002, 0.01)