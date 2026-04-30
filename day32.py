
#Data Analysis
'''
Why this is need?
-----------------
-->This is critical bcz it converts raw data into actionable insights,enabling information to decision
making easy and improve operational efficiency

1.Decision-Making
2.Improved-Operational Efficiency
3.Customer Understanding
4.Market Insight
5.Risk management
6.Data-Driven Strategies
'''
#1. matplotlib
#------------
#Line Plot
'''
import matplotlib.pyplot as plt
x=[2,6,15,18,40]
y=[12,13,34,23,15]
plt.plot(x,y)
plt.show()
'''

#Bar Graph
'''
import matplotlib.pyplot as plt
#a=["sports","shows","news"]
#b=[20,40,10]
#plt.bar(a,b)
plt.bar(["sports","shows","news"],[20,40,10])
plt.show()
'''

#Pie Chart
'''
import matplotlib.pyplot as plt
plt.pie([12.34,28,10,33],labels=["A","B","C","D"])
plt.show()
'''

#Histogram
'''
import matplotlib.pyplot as p
p.hist([23,15,78,12])
p.hist([34,25,45,12])
p.show()
'''
#2.Numpy
'''
-->Numpy(Numerical python) is the foundational open-source library for scientific computing in python,
providing high-performance,N-dimensional
-->This enables efficient numerical computation linear algebra, and data manipulation,serving as the
basis like TensorFlow and Scipy
'''
'''
import numpy as np
arr=np.array([1,2,3])
print(arr-1)
'''

#3.pandas
'''
-->This pandas is used for handling structured data in table format
'''

import pandas as pd
data={"Name":["chinni","maha"],"Marks":[67,89]}
a=pd.DataFrame(data)
print(a)





















