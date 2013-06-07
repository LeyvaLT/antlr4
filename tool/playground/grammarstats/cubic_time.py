from numpy  import *
import matplotlib.pyplot as plt

transitions_file = 'Cubic-timings'

# load timing data; column of times per file
f = open(transitions_file+'.txt',"rb")
timing = []
for line in f.readlines():
	timing.append(int(line.strip()))

trials = 1
N = len(timing)

x = array(arange(1,N+1,1), dtype=float)

# fit polynomial max 5
fit = polyfit(x, array(timing), 5)
poly = poly1d(fit)
print poly
y = poly(x)

x2 = pow(x,2)
x3 = pow(x,3)
x4 = pow(x,4)

# 0.0407 x^3 - 4.644 x^2 + 188 x - 1378

ratio = divide(timing,x3)

plt.plot(y, color="red", linewidth=0.5)
plt.plot(timing, color="blue", linewidth=0.5)

#plt.plot(divide(timing,x2), linewidth=0.5, color="blue")
#plt.plot(divide(timing,x3), linewidth=0.5, color="green")
#plt.plot(divide(timing,x4), linewidth=0.5, color="red")
#plt.plot(x3, linewidth=0.5, color="red")
#plt.plot(x4, linewidth=0.5, color="red")

plt.ylabel('Wallclock parse time (ms)', family="serif")
plt.title(transitions_file+" (files N="+str(N)+")")
plt.xlabel('File size in tokens (x, xx, xxx, ...)', family="serif")
plt.savefig(transitions_file+'-stats.pdf', format="pdf")
plt.show()