import sys
from numpy  import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatch
import matplotlib.pyplot as plt

transitions_file = {}

grammars = [g for g in sys.argv[1:]]

files = [g+'-transitions.txt' for g in grammars]

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

for g in grammars:
	plt.plot(means[g], linewidth=0.5)
plt.axis(ymax=.4)
plt.legend(grammars,
		   loc='upper right' , prop={'family':'serif'})
plt.ylabel('ATN to total transitions ratio', family="serif", size=15)
plt.xlabel('Files parsed', family="serif", size=15)
plt.savefig('atn-decay-stats.pdf', format="pdf", bbox_inches='tight', pad_inches=0)
plt.show()
