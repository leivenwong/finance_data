import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fixed_income = 0.05
fixed_retracement = 0
a = 0.21372
a_retracement = 0.39244
dia = 0.08671
dia_retracement = 0.2438
h = 0.07541
h_retracement = 0.29686

i = 0
out = pd.DataFrame()
revenue = []
retracement = []
sharp = []
fix_w = []
a_w = []
dia_w = []
h_w = []

for wfix in np.arange(0, 1.01, 0.01):
    for wa in np.arange(0, 1.01, 0.01):
        for wdia in np.arange(0, 1.01, 0.01):
            for wh in np.arange(0, 1.01, 0.01):
                if wfix + wa + wdia + wh == 1:
                    fix_w.append(wfix)
                    a_w.append(wa)
                    dia_w.append(wdia)
                    h_w.append(wh)
                    revenue_sum = wfix * fixed_income + wa * a + wdia * dia + wh * h
                    revenue.append(revenue_sum)
                    retracement_sum = wa * a_retracement + wdia * dia_retracement \
                                    + wh * h_retracement
                    if retracement_sum == 0:
                        sharp_sum = 0
                    else:
                        sharp_sum = revenue_sum / retracement_sum
                    retracement.append(retracement_sum)
                    sharp.append(sharp_sum)
                    i += 1
                    print(i)

out['fix_w'] = fix_w
out['a_w'] = a_w
out['dia_w'] = dia_w
out['h_w'] = h_w
out['revenue'] = revenue
out['retracement'] = retracement
out['sharp'] = sharp
print(out)

fig = plt.figure(figsize=(9,6))
#ax = fig.gca(projection='3d')
plt.scatter(revenue, retracement)
plt.xlabel('profit')
plt.ylabel('risk')
plt.show()

#out.to_excel('out.xlsx')
