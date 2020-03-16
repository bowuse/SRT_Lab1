import random
import math
import matplotlib.pyplot as plt

N = 256
w = 900
n = 10
t = [i for i in range(N)]


def count_sin():
    res = []
    for i in range(n):
        A = random.random()
        fi = random.random() * 6.28
        res_i = [A * math.sin(w * t[i] * i + fi) for i in range(N)]
        res.append(res_i)
    return res


def count_x_t():
    #######
    # Випадковий сигнал
    #######
    res = count_sin()
    x_t = []
    for i in range(N):
        x = 0
        for j in range(n):
            x += res[j][i]
        x_t.append(x)
    return x_t


def count_m_x():
    #######
    # Математичне сподівання
    #######
    m_x = []
    res = count_sin()
    for i in range(len(res)):
        temp = 0
        for j in range(len(res[i])):
            temp += res[i][j]
        m_x.append(temp / N)
    return sum(m_x) / n


def count_d_x():
    #######
    # Дисперсія
    #######
    signal = count_x_t()
    m_x = count_m_x()
    d_x = 0
    for i in range(len(signal)):
        d_x += (signal[i] - m_x) ** 2
    return d_x / N


def show_plot(x_t):
    plt.plot(t, x_t)
    plt.xlabel('x(t) = sum(A*sin(wt+f))')
    plt.grid(True)
    plt.show()


def save_result_in_file(m_x, d_x):
    with open('result.txt', 'a+') as f:
        f.writelines([
            'Число гармонік в сигналі n: {}\n'.format(n),
            'Гранична частота w: {}\n'.format(w),
            'Кількість дискретнх відліків N: {}\n'.format(N),
            'Mатематичне сподівання: {}\n'.format(m_x),
            'Дисперсія: {}\n'.format(d_x),
            '\n'])


def main():
    x_t = count_x_t()
    m_x = count_m_x()
    d_x = count_d_x()
    save_result_in_file(m_x, d_x)

    print('Число гармонік в сигналі n: {}'.format(n))
    print('Гранична частота w: {}'.format(w))
    print('Кількість дискретнх відліків N: {}'.format(N))
    print('Mатематичне сподівання: {}'.format(m_x))
    print('Дисперсія: {}'.format(d_x))

    show_plot(x_t)


if __name__ == '__main__':
    main()
