import sys
from numpy  import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatch
import matplotlib.pyplot as plt

import shared

transitions_file = {}

grammars = [g for g in sys.argv[1:]]

files = [g+'-timings.txt' for g in grammars]

# load transition data. Each row is the list of trial stats per this one file

stats = {}

means = {}
nfiles = {}
for i in range(len(grammars)):
	g = grammars[i]
	stats[g] = loadtxt(open(files[i],"rb"),delimiter=",",skiprows=0)
	means[g] = [mean(filerow) for filerow in stats[g]]
	nfiles[g] = len(stats[g]) # num files parsed for this grammar

print nfiles

f, (plt1,plt2) = plt.subplots(2, sharex=True)

m = 0
for g in grammars:
	plt.plot(means[g], linewidth=0.5,
			 color=shared.colors[g], linestyle=shared.styles[g])
	plt.text(len(means[g])-len(g)*10, means[g][len(means[g])-1], g,
			 fontsize=15)
	m = max(m, max(means[g]))

plt.axis(ymax=m*1.05)

#plt.legend(grammars,
		   #loc='upper left' , prop={'family':'serif'})
plt.ylabel('Parse time in ms', family="serif", size=15)
plt.xlabel('Files parsed', family="serif", size=15)
#plt.savefig('parse-time-stats.pdf', format="pdf", bbox_inches='tight', pad_inches=0)
plt.show()

