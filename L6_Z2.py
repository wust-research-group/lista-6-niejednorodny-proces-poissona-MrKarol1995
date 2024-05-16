import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt
import scipy.interpolate as interp
from typing import List

def lambda_function(t: int) -> float:
    """
    Funkcja intensywności procesu Poissona.

    Parameters:
        t (float): Czas.

    Returns:
        float: Wartość funkcji intensywności w punkcie czasowym t.
    """
    return t

def generate_nonhomogeneous_poisson_process(num_events):
    """
    Generuje niejednorodny proces Poissona na podstawie danych.

    Parameters:
        num_events (int): Liczba zdarzeń do wygenerowania.

    Returns:
        numpy.ndarray: Posortowane czasy zdarzeń w procesie Poissona.
    """
    # Losowanie zmiennych losowych z rozkładu jednostajnego
    u = np.random.rand(num_events)

    # Znajdowanie odpowiadających czasów oczekiwania zgodnie z dystrybuantą
    waiting_times = interp_F(u)

    # Sortowanie czasów oczekiwania
    waiting_times.sort()

    return waiting_times

T = 10
num_samples = 1000

# Wygeneruj 1000 realizacji zmiennej losowej N_t z rozkładu Poissona
N_t_values = []
m_T, _ = spi.quad(lambda_function, 0, T)

for _ in range(num_samples):
    # Wyznacz m(T) poprzez całkowanie funkcji lambda(t) od 0 do T
    m_T, _ = spi.quad(lambda_function, 0, T)

    # Wygeneruj N_T z rozkładu Poissona o parametrze m(T)
    N_T = np.random.poisson(m_T)
    N_t_values.append(N_T)
N_t_values.sort()

# Wykres histogramu wartości N_t
plt.figure(figsize=(10, 6))
plt.hist(N_t_values, bins=20, color='skyblue', edgecolor='black', alpha=0.7)
plt.xlabel("Wartość N_t")
plt.ylabel("Częstość")
plt.title("Histogram 1000 realizacji zmiennej N_t")
plt.grid(True)
plt.show()


# Oblicz dystrybuantę F(t) = m(t) / m(T) dla każdej wartości t
F_values = []

for t in np.linspace(0, T, num_samples):
    # Oblicz całkę funkcji intensywności od 0 do t
    m_t, _ = spi.quad(lambda_function, 0, t)
    F_values.append(m_t / m_T)

# Wykres dystrybuanty
plt.figure(figsize=(10, 6))
plt.plot(np.linspace(0, T, num_samples), F_values, color='blue')
plt.xlabel("Czas (t)")
plt.ylabel("Wartość dystrybuanty F(t)")
plt.title("Dystrybuanta rozkładu N_t")
plt.grid(True)
plt.show()


# Dane wejściowe
N_t_values_sorted = np.array(N_t_values)  # Posortowane czasy oczekiwania
F_values_sorted = np.array(F_values)      # Wartości dystrybuanty odpowiadające czasom oczekiwania

# Interpolacja dystrybuanty
interp_F = interp.interp1d(F_values_sorted, np.linspace(0, T, num_samples))

# Generowanie niejednorodnego procesu Poissona na podstawie danych
num_events = len(N_t_values_sorted)
nonhomogeneous_poisson_process = generate_nonhomogeneous_poisson_process(num_events)

# Wykres
plt.figure(figsize=(10, 6))
plt.step(nonhomogeneous_poisson_process, np.arange(1, num_events + 1), where='post', color='orange')
plt.xlabel("Czas")
plt.ylabel("Liczba zdarzeń")
plt.title("Niejednorodny proces Poissona na podstawie danych")
plt.grid(True)
plt.show()
