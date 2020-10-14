from matplotlib import pyplot as plt

x = [1,2,3,4]
y = [9,5,2,1]
x1 = [2,5,6,4,]
y1 = [10,20,15,15]

plt.bar(x,y, label="bar one")
plt.bar(x1,y1,label= "bar two", color='g')


plt.legend

plt.title("Bar Graph")
plt.ylabel("Bar Height")
plt.xlabel("Bar Width")

plt.show()

