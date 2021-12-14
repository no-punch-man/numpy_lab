import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def init():
    line.set_data([], [])
    return line,

def data_count(i, x, A, l):
	L = [np.array(l, dtype = np.float64)]
	for j in range(i):
		j += 1
		tmp = np.array(L[j - 1] - 0.5 * A @ (L[j - 1]))
		L.append(tmp)
	return [x, L[i]]
    
def animate(i, x, A, l):
	d = data_count(i, x, A, l)
	x = d[0]
	y = d[1]
	line.set_data(x, y)
	return line,


fig, ax = plt.subplots()
line, = ax.plot([], [], lw = 2)
ax.set_xlim(0, 50) 
ax.set_ylim(0, 10)
ax.grid()
 
f = open(r'sources\start.txt', 'r')
lines = f.read().split('\n')
n = len(lines)
A = np.diag(np.full(n, 1)) - np.eye(n, k = -1)
A[0][len(A[0]) - 1] = -1
x = np.linspace(0, 50, len(lines))
print(A)
	
anim = animation.FuncAnimation(fig, animate, frames=256, init_func=init, interval=20, blit = True, fargs = [x, A, lines])
anim.save('result.gif')

