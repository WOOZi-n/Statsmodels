import numpy as np
dat = list(map(int, input().split()))
# 로지스틱로그가능도함수 미분값 산출
init = 0
def lld(x, k = init): # logistic_likelihood_derivative
    arr = np.array(x)
    return len(arr) - 2*np.sum(np.exp(k-arr) / (1 + np.exp(k-arr)))

def diff_lld(x, k):
    eps = 0.001
    return (lld(x, k + eps) - lld(x, k)) / eps

theta = init
adj = 0.00001

while True:
    newtheta = theta - lld(dat, theta) / (diff_lld(dat ,theta) + adj)
    if np.abs(newtheta - theta) < 0.00001:
        break
    theta = newtheta

print(newtheta) # N-R 추정값
print(lld(dat, newtheta)) # N-R 추정값을 넣어 구한 미분값