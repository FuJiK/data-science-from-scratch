from matplotlib import pyplot as plt
variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squard = [256,128,64,32,16,8,4,2,1]
total_error = [x + y for x, y in zip(variance, bias_squard)]
xs = [i for i, _ in enumerate(variance)]

plt.plot(xs, variance, 'g-', label='variance') #緑の実線
plt.plot(xs, bias_squard, 'r-.', label='bias^2') #赤の点線
plt.plot(xs, total_error, 'b:', label='total error') #青の点線
# 各線にlabelを指定しているので、凡例が自動で描かれる
plt.legend(loc = 9) # loc = 9 :上部中央
plt.xlabel("model complexity")
plt.title("The Bias-Variance Tradeoff")
plt.show()