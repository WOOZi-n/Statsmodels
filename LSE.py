#LSE 구현
import numpy as np

x = list(map(int, input().split()))
y = list(map(int, input().split()))
xmean = np.mean(x)
ymean = np.mean(y)
sxx=0
sxy=0
for a,b in zip(x,y):
    sxx += (a-xmean)**2
    sxy += (a-xmean)*(b-ymean)

print("%d x + %d = y" %((sxy/sxx), ymean-(sxy/sxx)*xmean))


