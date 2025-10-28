import cv2
import numpy as np
import os

# Pastikan folder output ada
os.makedirs("output", exist_ok=True)

# ===============================
# 1. BUAT KANVAS DAN KARAKTER
# ===============================
canvas = np.zeros((400, 400, 3), dtype=np.uint8)

# Kepala
cv2.rectangle(canvas, (120, 80), (280, 240), (0, 255, 255), -1)

# Mata
cv2.circle(canvas, (160, 140), 20, (0, 0, 0), -1)
cv2.circle(canvas, (240, 140), 20, (0, 0, 0), -1)
cv2.circle(canvas, (160, 140), 8, (255, 255, 255), -1)
cv2.circle(canvas, (240, 140), 8, (255, 255, 255), -1)

# Mulut
cv2.line(canvas, (160, 200), (240, 200), (0, 0, 0), 4)

# Antena
cv2.line(canvas, (200, 80), (200, 40), (255, 0, 0), 3)
cv2.circle(canvas, (200, 30), 10, (0, 0, 255), -1)

# Badan
cv2.rectangle(canvas, (140, 240), (260, 350), (0, 255, 0), -1)

# Nama karakter
cv2.putText(canvas, "R-BOT", (130, 390), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

# Simpan karakter asli
cv2.imwrite("output/karakter.png", canvas)
cv2.imshow("Karakter Asli", canvas)

# ===============================
# 2. TRANSFORMASI GAMBAR
# ===============================
rows, cols = canvas.shape[:2]

# --- Translasi (geser posisi) ---
M_translate = np.float32([[1, 0, 50], [0, 1, 30]])
translated = cv2.warpAffine(canvas, M_translate, (cols, rows))
cv2.imwrite("output/translate.png", translated)
cv2.imshow("Translasi", translated)

# --- Rotasi (putar) ---
M_rotate = cv2.getRotationMatrix2D((cols / 2, rows / 2), 30, 1)
rotated = cv2.warpAffine(canvas, M_rotate, (cols, rows))
cv2.imwrite("output/rotate.png", rotated)
cv2.imshow("Rotasi", rotated)

# --- Resize (ubah ukuran) ---
resized = cv2.resize(canvas, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
cv2.imwrite("output/resize.png", resized)
cv2.imshow("Resize", resized)

# --- Crop (potong gambar) ---
cropped = canvas[100:300, 120:320]
cv2.imwrite("output/crop.png", cropped)
cv2.imshow("Crop", cropped)

# ===============================
# 3. OPERASI ARITMATIKA & BITWISE
# ===============================

# Background polos (warna oranye muda)
background = np.full((400, 400, 3), (255, 200, 150), dtype=np.uint8)
cv2.imwrite("output/background.png", background)
cv2.imshow("Background", background)

# --- Operasi cv2.add() ---
added = cv2.add(canvas, background)
cv2.imwrite("output/add.png", added)
cv2.imshow("Add (Gabungan)", added)

# --- Operasi cv2.bitwise_and() ---
bitwise_and = cv2.bitwise_and(canvas, background)
cv2.imwrite("output/bitwise_and.png", bitwise_and)
cv2.imshow("Bitwise AND", bitwise_and)

# --- Operasi cv2.bitwise_not() (bonus efek negatif) ---
bitwise_not = cv2.bitwise_not(canvas)
cv2.imwrite("output/bitwise_not.png", bitwise_not)
cv2.imshow("Bitwise NOT", bitwise_not)

# ===============================
# 4. TUNGGU & TUTUP SEMUA WINDOW
# ===============================
cv2.waitKey(0)
cv2.destroyAllWindows()
