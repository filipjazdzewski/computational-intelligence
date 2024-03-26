import numpy as np

weights = {
    "wiek": [-0.46122, 0.78548],
    "waga": [0.97314, 2.10584],
    "wzrost": [-0.38203, -0.57847],
    "bias1": [0.80109, 0.43528],
    "bias2": [-0.2368],
    "hidden2": [-0.81546, 1.03775],
}


# Funkcja aktywacji
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def forwardPass(wiek, waga, wzrost):
    hidden1 = (
        wiek * weights["wiek"][0]
        + waga * weights["waga"][0]
        + wzrost * weights["wzrost"][0]
        + weights["bias1"][0]
    )
    hidden1_po_aktywacji = sigmoid(hidden1)
    hidden2 = (
        wiek * weights["wiek"][1]
        + waga * weights["waga"][1]
        + wzrost * weights["wzrost"][1]
        + weights["bias1"][1]
    )
    hidden2_po_aktywacji = sigmoid(hidden2)
    output = (
        hidden1_po_aktywacji * weights["hidden2"][0]
        + hidden2_po_aktywacji * weights["hidden2"][1]
        + weights["bias2"][0]
    )
    return output


print(forwardPass(23, 75, 176))
# Wynik z pdf: 0.798528
# Wynik z mojego programu: 0.7871056221494851
# Różnica wynika prawdopodbnie ze złego przepisania wag z pdfa (nie dałem rady się rozczytać)
