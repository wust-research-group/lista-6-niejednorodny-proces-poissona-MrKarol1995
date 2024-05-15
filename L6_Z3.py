import numpy as np
import matplotlib.pyplot as plt


def thinning(lambda_max, T, lambda_func):
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
            if u2 < lambda_func(t) / lambda_max:
                arrivals.append(t)
    return np.array(arrivals)


def lambda_t1(t):
    """
    Funkcja intensywności dla pierwszego procesu.
    """
    return 5 + 0.5 * np.sin(2 * np.pi * t / 24)


def lambda_t2(t):
    """
    Funkcja intensywności dla drugiego procesu.
    """
    return 3 + np.cos(2 * np.pi * t / 24)


def lambda_t_combined(t):

    return 5 + 0.5 * np.sin(2 * np.pi * t / 24) + 3 + np.cos(2 * np.pi * t / 24)


T = 20

# Generowanie procesów Poissona dla lambda_t1 i lambda_t2
arrivals1 = thinning(lambda_max=0.8, T=T, lambda_func=lambda_t1)
arrivals2 = thinning(lambda_max=0.8, T=T, lambda_func=lambda_t2)

# Połączenie wszystkich zdarzeń
combined_arrivals = np.concatenate((arrivals1, arrivals2))
combined_arrivals.sort()

# Generowanie procesu Poissona dla lambda_t_combined
arrivals_combined = thinning(lambda_max=1.1, T=T, lambda_func=lambda_t_combined)

# Porównanie wszystkich wykresów na jednym
plt.figure(figsize=(10, 5))
plt.step(arrivals1, range(len(arrivals1)), label="Proces 1", where="post", color="blue")
plt.step(
    arrivals2, range(len(arrivals2)), label="Proces 2", where="post", color="green"
)
plt.step(
    combined_arrivals,
    range(len(combined_arrivals)),
    label="Połączone procesy",
    where="post",
    color="red",
)
plt.step(
    arrivals_combined,
    range(len(arrivals_combined)),
    label="Proces Poissona (lambda_t_combined)",
    where="post",
    color="purple",
)
plt.xlabel("Czas")
plt.ylabel("Liczba przybyć")
plt.title("Porównanie procesów Poissona")
plt.legend()
plt.grid(True)
plt.show()

time_points = np.linspace(0, T, 1000)
intensity1 = lambda_t1(time_points)
intensity2 = lambda_t2(time_points)
intensity_combined = lambda_t_combined(time_points)

# Wykresy intensywności
plt.figure(figsize=(10, 5))
plt.plot(time_points, intensity1, label="Proces 1", color="blue")
plt.plot(time_points, intensity2, label="Proces 2", color="green")
plt.plot(time_points, intensity_combined, label="Połączone procesy", color="red")
plt.xlabel("Czas")
plt.ylabel("Intensywność")
plt.title("Porównanie intensywności procesów Poissona")
plt.legend()
plt.grid(True)
plt.show()
