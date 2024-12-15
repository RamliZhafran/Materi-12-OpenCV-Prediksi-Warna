import cv2
import numpy as np

# Membuka kamera
cap = cv2.VideoCapture(0)

while True:
    # Membaca frame dari kamera
    ret, frame = cap.read()
    
    if not ret:
        print("Gagal membaca frame dari kamera.")
        break
    
    # Membalik frame secara horizontal
    frame = cv2.flip(frame, 1)
    
    # Menampilkan frame
    cv2.imshow("Camera", frame)
    
    # Menunggu tombol tekan, keluar jika tombol ESC ditekan
    key = cv2.waitKey(1)
    if key == 27:  # Tombol ESC
        break

# Melepaskan kamera dan menutup jendela
cap.release()
cv2.destroyAllWindows()