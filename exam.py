# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Programming in Python
# ## Exam: July 14, 2022
#
# You can solve the exercises below by using standard Python 3.10 libraries, NumPy, Matplotlib, Pandas, PyMC3.
# You can browse the documentation: [Python](https://docs.python.org/3.10/), [NumPy](https://numpy.org/doc/stable/user/index.html), [Matplotlib](https://matplotlib.org/stable/users/index.html), [Pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html), [PyMC3](https://docs.pymc.io/en/v3/index.html).
# You can also look at the [slides of the course](https://homes.di.unimi.it/monga/lucidi2122/pyqb00.pdf) or your code on [GitHub](https://github.com).
#
# **It is forbidden to communicate with others.** 
#
#
#
#

import numpy as np
import pandas as pd  # type: ignore
import matplotlib.pyplot as plt # type: ignore
import pymc3 as pm   # type: ignore
import arviz as az   # type: ignore

# ### Exercise 1 (max 5 points)
#
# The file [Howell1](./Howell1.csv) (source: https://github.com/rmcelreath/rethinking/blob/master/data/Howell1.csv) contains data about a population of men and women: it records their height (in cm), weight (in kg), age (in years), and a binary variable for the gender (1 is male); fields are separated by `;`. Unfortunately, the records mixed up American and European conventions for decimal numbers: sometimes the values are recorded with the decimal point, sometimes with the decimal comma. 
#
# Load the data in a pandas dataframe, but be sure to get them correctly interpreted. Several strategies are possibile: you can fix the data and load them with pandas, or you can load them as strings and convert them to floats when you already have the data in the dataframe: at the end you are required to have a dataframe with a proper float `dtype`.

with open('Howell1.csv') as untidy:
    with open('howell-tidy.csv', 'w') as tidy:
        for line in untidy:
            line = line.replace(',', '.')
            tidy.write(line)

data = pd.read_csv('howell-tidy.csv', sep=';')

# ### Exercise 2 (max 2 points)
#
# Plot a histogram of the "age" values.
#

# +
fig, ax = plt.subplots()

data['age'].hist(ax=ax, bins='auto')
_ = ax.set_title('age')
# -

# ### Exercise 3 (max 3 points)
#
# Make a figure with two columns of plots. In the first column plot together (contrast) the histograms of 'age' for males and females. In the second column plot the histograms of 'age' for people taller than 1.2m, again contrasting male to females. Use density histograms to make the diagrams easy to compare; add proper titles and legends.
#

# +
fig, ax = plt.subplots(ncols=2)
male = data[data['male'] == 1]
female = data[data['male'] != 1]

ax[0].hist(male['weight'], density=True, label='male')
ax[0].hist(female['weight'], density=True, label='female')
ax[0].set_title('Weight of all')
ax[0].legend()

ax[1].hist(male[male['height'] > 120]['weight'], density=True, label='male')
ax[1].hist(female[female['height'] > 120]['weight'], density=True, label='female')
ax[1].set_title('Weight of taller than 120cm')
_ = ax[1].legend()
# -

# ### Exercise 4 (max 2 points)
#
# Add a column `w_dens` with the ratio between weight and height.

data['w_dens'] = data['weight'] / data['height']

# ### Exercise 5 (max 3 points)
#
# Make a scatterplot of `w_dens` vs. `age`; in the plot the point corresponding to males should be appear in blue, the points corresponding to female in red.
#
#

# +
male = data[data['male'] == 1]
female = data[data['male'] != 1]

fig, ax = plt.subplots()
ax.scatter(male['age'], male['w_dens'], color='blue', label='male')
ax.scatter(female['age'], female['w_dens'], color='red', label='female')
_ = ax.legend()


# -

# ### Exercise 6 (max 7 points)
#
# Define a function `w_dens_by_gender` that takes an age and a boolean value. If the boolean is true, the function should return the age divided by 100 if the age is less or equal to 30, or .30 if the age is greater than 30. If the boolean value is false, the function should return the age divided by 110, if the age is less or equal to 25, or .23 if the age is greater than 25.
# For example, if the parameters are 15 and `True`, the function should return 0.15.
#
# To get the full marks, you should declare correctly the type hints and add a test within a doctest string.

# +
def w_dens_by_gender(age: int, male: bool) -> float:
    """Return w_dens by gender at a given age.
    
    >>> w_dens_by_gender(15, True)
    0.15
    >>> w_dens_by_gender(42, True)
    0.3
    >>> w_dens_by_gender(11, False)
    0.1
    >>> w_dens_by_gender(39, False)
    0.23
    
    """
    if male:
        if age <= 30:
            return age/100
        return .30
    if age <= 25:
        return age/110
    return .23
    
    
# -

# ### Exercise 7 (max 5 points)
#
# Add a column `expected_w_dens` that combine the columns `age` and `male` with the function `w_dens_by_gender`.
#
# To get the full marks avoid the use of explicit loops.
#

data['expected_w_dens'] = data.apply(lambda row: w_dens_by_gender(row['age'], row['male'] == 1), axis=1)

# ### Exercise 8 (max 5 points)
#
# Consider this statistical model:
#
# - the error `expected_w_dens` - `w_dens` is normally distributed, with (unknown) mean $\mu$ and (unknown) standard deviation $\sigma$
# - $\mu$ is normally distributed with mean $=0$ and standard deviation $=5$
# - $\sigma$ is exponentially distributed with $\lambda = 1$
#
# Code this model with pymc3, sample the model, and print the summary of the resulting estimation by using `az.summary`.
#
#
#
#


# +
errs = data['expected_w_dens']-data['w_dens']

with pm.Model() as model:
    mu = pm.Normal('mu', 0, 5)
    sigma = pm.Exponential('sigma', 1)
    error = pm.Normal('error', mu=mu, sigma=sigma, observed=errs)
    
    idata = pm.sample(return_inferencedata=True)
    
    
    
    
    
# -

az.summary(idata)


