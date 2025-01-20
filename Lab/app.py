# import numpy as np;
# import matplotlib.pyplot as plt

# x = np.arange(-5,5,.1)
# n = len(x)
# y = np.zeros(n)
# for i in range(n):
#   y[i] = x[i]**2

# plt.plot(x,y)

# plt.show()

# R = 1000
# C = 0.00001
# Vs = 10
# V0 = 5
# t = np.arange(-0.05,0.10,0.00001)
# n = len(t)
# Vc = np.zeros(n)
# for i in range(n):
#   Vc[i] = Vs + (V0 - Vs)(2.71828*(-t[i]/(R*C)))

# plt.plot(t,Vc)
# plt.show()


student={
  'Name':['bibhu','behera'],
  'subject':["ai","ml","bee"],
  "roll no":[100,200,300]
}
x=student.keys()
for key in x:
  print(student.get(key))

graph={
  "A":["B","C"],
  "B":["A","D","E"],
  "C":["A"],
}