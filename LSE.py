#LSE 구현
import numpy as np

x = np.array(list(map(int, input().split())))
y = np.array(list(map(int, input().split())))
xmean = np.mean(x)
ymean = np.mean(y)

sxx = ((x - xmean)**2).sum()
sxy = ((y - ymean)*(x-xmean)).sum()



estedB1 = sxy/sxx
estedB0 = ymean - estedB1*xmean
print("%d x + %d = y" %(estedB1, estedB0))


MSE = ((y-estedB1*x-estedB0)**2).mean()
print("MSE = %d" %MSE)
