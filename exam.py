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

pass

# ### Exercise 2 (max 2 points)
#
# Plot a histogram of the "age" values.
#

# +
pass
# -

# ### Exercise 3 (max 3 points)
#
# Make a figure with two columns of plots. In the first column plot together (contrast) the histograms of 'age' for males and females. In the second column plot the histograms of 'age' for people taller than 1.2m, again contrasting male to females. Use density histograms to make the diagrams easy to compare; add proper titles and legends.
#

# +
pass
# -

# ### Exercise 4 (max 2 points)
#
# Add a column `w_dens` with the ratio between weight and height.

pass

# ### Exercise 5 (max 3 points)
#
# Make a scatterplot of `w_dens` vs. `age`; in the plot the point corresponding to males should be appear in blue, the points corresponding to female in red.
#
#

# +
pass
# -

# ### Exercise 6 (max 7 points)
#
# Define a function `w_dens_by_gender` that takes an age and a boolean value. If the boolean is true, the function should return the age divided by 100 if the age is less or equal to 30, or .30 if the age is greater than 30. If the boolean value is false, the function should return the age divided by 110, if the age is less or equal to 25, or .23 if the age is greater than 25.
# For example, if the parameters are 15 and `True`, the function should return 0.15.
#
# To get the full marks, you should declare correctly the type hints and add a test within a doctest string.

# +
pass
# -

# ### Exercise 7 (max 5 points)
#
# Add a column `expected_w_dens` that combine the columns `age` and `male` with the function `w_dens_by_gender`.
#
# To get the full marks avoid the use of explicit loops.
#

pass

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
pass
# -
