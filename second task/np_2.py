import numpy as np
import matplotlib.pyplot as plt
def open_(filename):
    f = open(filename)
    return f

for i in [r'sources\signal01.dat', r'sourcessignal02.dat', r'sources\signal03.dat']:
    s = i[41:49]
    data = np.array(open_(i).read().split('\n'), dtype = np.float64)
    filt_data = []
    filt_data.append(data[0])
    for i in range(len(data)):
        n = i + 1;
        start = n - 9;
        if start < 0:
            start = 0;
        filt_data.append(np.mean(data[start:n]))
    x = [i + 1 for i in range(len(data))]
    t = [i + 1 for i in range(len(filt_data))]
    plt.subplot(1, 2, 1)
    plt.plot(x, data,'-',
            linewidth = 1,
            color = 'navy')
    plt.grid()
    plt.title('Сырой сигнал')

    plt.subplot(1, 2, 2)
    plt.plot(t, filt_data,'-',
            linewidth = 1,
            color = 'cornflowerblue')
    plt.grid()
    plt.title('После фильтра')

    plt.savefig(s + ".png")
    
