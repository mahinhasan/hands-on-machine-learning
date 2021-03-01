import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import sklearn.linear_model
import sklearn.neighbors
import numpy as np
 

def prepare_country_stats(oecd_bli, gdp_per_capita):
    oecd_bli = oecd_bli[oecd_bli["INEQUALITY"] == "TOT"]
    oecd_bli = oecd_bli.pivot(
        index="Country", columns="Indicator", values="Value")
    gdp_per_capita.rename(columns={"2015": "GDP per capita"}, inplace=True)
    gdp_per_capita.set_index("Country", inplace=True)
    full_country_stats = pd.merge(left=oecd_bli, right=gdp_per_capita,
                                  left_index=True, right_index=True)
    full_country_stats.sort_values(by="GDP per capita", inplace=True)
    remove_indices = [0, 1, 6, 8, 33, 34, 35]
    keep_indices = list(set(range(36)) - set(remove_indices))
 
    return full_country_stats[["GDP per capita", 'Life satisfaction']].iloc[keep_indices]
 
 
if __name__ == "__main__":
    oecd_bli = pd.read_csv("handson-ml/datasets/lifesat/oecd_bli_2015.csv", thousands=',')
    gdp_per_capita = pd.read_csv(
        "handson-ml/datasets/lifesat/gdp_per_capita.csv", thousands=',', delimiter='\t', encoding='latin1', na_values='n/a')
 
    country_stats = prepare_country_stats(oecd_bli, gdp_per_capita)
    country_stats.plot(kind='scatter', x="GDP per capita",
                       y="Life satisfaction")
 
    X = np.c_[country_stats["GDP per capita"]]
    Y = np.c_[country_stats["Life satisfaction"]]
 
    
    model = sklearn.linear_model.LinearRegression()
    model.fit(X, Y)
 
    for x in range(10, 50):
        plot_x = 1000 * x
        plot_y = float(model.predict([[plot_x]]))
        plt.scatter(plot_x, plot_y, s=10, color='r')
    plt.show()