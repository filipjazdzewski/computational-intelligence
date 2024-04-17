import cv2


def convert_to_grayscale_avg(image):
    # Obliczanie średniej wartości kanałów RGB dla każdego piksela
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image


def convert_to_grayscale_custom(image):
    # Obliczanie wartości szarej piksela na podstawie zalecanych współczynników
    gray_image = (
        0.299 * image[:, :, 2] + 0.587 * image[:, :, 1] + 0.114 * image[:, :, 0]
    )
    gray_image = gray_image.astype("uint8")  # Konwersja na typ uint8
    return gray_image


# Wczytanie obrazu
image_path = "rivendell.jpg"
image = cv2.imread(image_path)

# Konwersja za pomocą pierwszego sposobu
gray_image_avg = convert_to_grayscale_avg(image)

# Konwersja za pomocą drugiego sposobu
gray_image_custom = convert_to_grayscale_custom(image)

# Wyświetlenie oryginalnego obrazu i obrazów w skali szarości
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image (Average)", gray_image_avg)
cv2.imshow("Grayscale Image (Custom)", gray_image_custom)
cv2.waitKey(0)
cv2.destroyAllWindows()
