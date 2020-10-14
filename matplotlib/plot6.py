from matplotlib import pyplot as plt

x = [2,8,9,4,5,10,71,12]
y = [85,98,6,12,0,14,15,100]

plt.scatter(x,y,label='skitcat', color='k', s=100, marker= 'x')

plt.xlabel("y axis")
plt.ylabel("x axis")

plt.title("Scatter plot")
plt.show

