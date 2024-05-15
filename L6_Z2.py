import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt


def lambda_function(t):
    return 5 + 0.5 * np.sin(2 * np.pi * t / 24)


T = 10
num_samples = 200

# Wyznacz m(T) poprzez całkowanie funkcji lambda(t) od 0 do T
m_T = spi.quad(lambda_function, 0, T)

# Wygeneruj N_T z rozkładu Poissona o parametrze m(T)
N_T = np.random.poisson(m_T)

# Wygeneruj num_samples punktów czasowych w przedziale [0, T]
time_points = np.sort(np.random.uniform(0, T, num_samples))

# Wygeneruj num_samples czasów oczekiwania z dystrybuanty F(t) = m(t) / m(T)
waiting_times = np.array(
    [np.random.exponential(scale=1 / lambda_function(t)) for t in time_points]
)

# Liczba zdarzeń na interwałach czasowych
event_counts = np.random.poisson(waiting_times)

# Trajektoria procesu Poissona
trajectory = [(time_points[i], event_counts[i]) for i in range(num_samples)]

# Trajektorii
plt.figure(figsize=(10, 6))
plt.step(
    [point[0] for point in trajectory],
    np.cumsum([point[1] for point in trajectory]),
    where="post",
)
plt.xlabel("Czas")
plt.ylabel("Liczba zdarzeń")
plt.title("Trajektoria niejednorodnego procesu Poissona")
plt.grid(True)
plt.show()


# Wykres liczby zdarzeń na wygenerowanej trajektorii
plt.figure(figsize=(10, 6))
plt.step(
    [point[0] for point in trajectory],
    np.cumsum([point[1] for point in trajectory]),
    where="post",
    label="Empiryczna liczba zdarzeń",
)
plt.plot(
    [0, T], [0, N_T[0]], "r--", label="Teoretyczna liczba zdarzeń w czasie T ($N_T$)"
)
plt.xlabel("Czas")
plt.ylabel("Liczba zdarzeń")
plt.title("Porównanie empirycznej i teoretycznej liczby zdarzeń na trajektorii")
plt.grid(True)
plt.legend()

plt.show()
