# -*- coding:utf-8 -*-
# @Time    :2022/10/28 22:13
# @Author  :ZZK
# @ File   :Calculate_antibody_titer.py
# Description:
import sys

import numpy as np
import matplotlib.pyplot as plt
import sympy

x_input = input("Please enter x axis data separated by space and press enter.\n")
y_input = input("Please enter y axis data separated by space and press enter.\n")
dj0 = [float(xx) for xx in x_input.split(" ")]
dis0 = [float(yy) for yy in y_input.split(" ")]
if len(dj0) != len(dis0):
    print("x,y data volume is not equal, the program stops!")
    sys.exit()
if len(dj0) == 1 or len(dis0) == 1:
    print("The entered data does not follow the space separation rule, the program stops!")
    sys.exit()
print(dj0, dis0)
# dj0 = [0.15, 0.5, 1.5, 5,15]
# dis0 = [0.01, 0.03, 0.07,0.16, 0.31]#13
x0 = np.array(dj0)
y0 = np.array(dis0)

para0 = np.polyfit(x0, y0, 2)

y_0 = para0[0] * x0 ** 2 + para0[1] * x0 + para0[2]
print("Equation coefficient：", para0)

plt.scatter(x0, y0)
plt.plot(x0, y_0, "r")

r = np.corrcoef(y0, y_0)[0, 1]
print("R^2：", r ** 2)
xxx = sympy.symbols("x")
aa = para0[0]
bb = para0[1]
cc = para0[2]
while True:
    yyy = input("Please input all y's separated by Spaces!：\n")
    y_one = yyy.split(" ")
    a_one = []
    for y_ in y_one:
        fun1 = f'{aa}*x**2 + {bb}* x + {cc}'
        aa0 = sympy.solve([f'{fun1} - {y_}'], [xxx])
        # x_top = -1 * (float(bb) / (2 * float(aa)))
        if aa0[0][0] <= 0:
            a_one.append(0.0)
        else:
            a_one.append(round(aa0[0][0], 4))
        # print(a[0][0])

    num_one = input("Input the amount added，for example 0.5 , 1.5 or other (x10^9)：\n")
    final_a_one = []
    for num_ in a_one:
        if num_ < 0:
            num_ = 0
        final_a_one.append(round(float(num_one) - num_, 2))
    # for num in final_a_one:
    print("The number of neutralized virions obtained by counting:", final_a_one)

    # final_a_one的值
    print("The first value is 0, the divisor cannot be 0, automatically removed.")
    yyyy = input("Input volume, spacing separation!：\n")
    volume = yyyy.split(" ")
    result = []
    for index, item in enumerate(final_a_one):
        print(index, item)
        if item > 0 and float(volume[index]) > 0:
            print(index, round(item / float(volume[index]), 4))
            result.append(round(item / float(volume[index]), 4))
    print(result)
    print("mean value:", round(sum(result) / len(result), 4))
