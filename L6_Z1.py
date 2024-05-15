import numpy as np
import matplotlib.pyplot as plt


def thinning(lambda_max, T):
    """
    Generuje niejednorodny proces Poissona na przedziale [0, T] za pomocą metody przerzedzeń.
    """
    arrivals = []
    t = 0
    while t < T:
        u1 = np.random.rand()
        u2 = np.random.rand()
        inter_arrival_time = -np.log(u1) / lambda_max
        t += inter_arrival_time
        if t < T:
            if u2 < lambda_t(t) / lambda_max:
                arrivals.append(t)
    return np.array(arrivals)


def lambda_t(t):
    """
    Funkcja intensywności.
    """
    return 5 + 0.5 * np.sin(2*np.pi*t/24)


T = 20
arrivals = thinning(lambda_max=0.8, T=T)

# Wykres procesu Poissona
plt.figure(figsize=(10, 5))
plt.step(arrivals, range(len(arrivals)))
plt.xlabel("Czas")
plt.ylabel("Liczba przybyć")
plt.title("Niejednorodny proces Poissona (metoda przerzedzeń)")
plt.grid(True)
plt.show()
