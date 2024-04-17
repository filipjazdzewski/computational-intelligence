import os

import cv2


def count_birds(image):
    # Binaryzacja adaptacyjna
    binary_image = cv2.adaptiveThreshold(
        image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2
    )

    # Znalezienie konturów
    contours, _ = cv2.findContours(
        binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    # Liczenie konturów, które są wystarczająco duże (potencjalne ptaki)
    bird_count = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        if 4 < area < 60:  # Zakładamy, że ptak ma powierzchnię między 100 a 500 pikseli
            bird_count += 1

    return bird_count


# Ścieżka do folderu z obrazami
folder_path = "bird_miniatures/"

# Iteracja przez wszystkie pliki w folderze
for filename in os.listdir(folder_path):
    if filename.endswith(".jpg") or filename.endswith(
        ".png"
    ):  # Upewnij się, że wczytujemy tylko obrazy
        image_path = os.path.join(folder_path, filename)
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        bird_count = count_birds(image)
        print(f"{filename}: {bird_count} birds")
