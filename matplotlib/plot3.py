import matplotlib.pyplot as plt
import matplotlib import style

style.use('ggplot')
x=[5,8,10]
y=[12,16,6]
x1=[6,9,11]
y1=[6,15,7]

plt.plot(x,y,'g',label='line one',linewidth=10)
plt.plot(x1,y1, 'b',label='line two',linewidth=5)

plt.title("Epic Information")
plt.ylabel("Y Axis")
plt.xlabel("X Axis")

plt.show()