import matplotlib.pyplot as plt
import numpy as np

#get data
myfile = open("fl_dat.csv","r")
header = myfile.readline()
everything = myfile.readlines()
date = []
num_pos = []
rate_pos = []
for data in everything:
	piece = data.split(",")
	date.append(piece[0])
	num_pos.append(float(piece[1]))
	rate_pos.append(float(piece[2]))
myfile.close()
#print(date)
#print(num_pos)
#print(rate_pos)

#Calulations
#myarray = np.column_stack((date,num_pos,rate_pos))
#mylist = list(zip(date,num_pos,rate_pos)) #date = myarray[i][0], num = [1], rate = [2]
#print(mylist) #myarray
aMax = max(num_pos)
loc = num_pos.index(max(num_pos)) #location
print(aMax,loc)

#for each in 



#make plot
fig, ax1 = plt.subplots()
color = "blue"
ax1.set_xlabel('date')
for tick in ax1.get_xticklabels():
    tick.set_rotation(45)
ax1.set_ylabel('Number of Postive Cases', color=color)
ax1.plot(date, num_pos, color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax2 = ax1.twinx()
color = 'red'
ax2.set_ylabel('Postive Rate', color=color)
ax2.plot(date, rate_pos, color=color)
ax2.tick_params(axis='y', labelcolor=color)
fig.tight_layout()
plt.show()
