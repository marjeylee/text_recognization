"""
生成正态分布数据
"""

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


def get_normal_data(mu, sigma, sample_nom):
    return np.random.normal(mu, sigma, sample_nom)[0]


def demo2():
    mu, sigma, num_bins = 0, 5, 50
    x = mu + sigma * np.random.randn(1000000)
    # 正态分布的数据
    n, bins, patches = plt.hist(x, num_bins, normed=True, facecolor='blue', alpha=0.5)
    # 拟合曲线
    y = mlab.normpdf(bins, mu, sigma)
    plt.plot(bins, y, 'r--')
    plt.xlabel('Expectation')
    plt.ylabel('Probability')
    plt.title('histogram of normal distribution: $\mu = 0$, $\sigma=1$')

    plt.subplots_adjust(left=0.15)
    plt.show()
    pass
