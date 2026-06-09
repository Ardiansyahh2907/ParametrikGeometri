import numpy as np
import matplotlib.pyplot as plt

print("===================================")
print(" PEMBANGKITAN KURVA PARAMETRIK ")
print("===================================")

# =====================================
# RESOLUSI
# =====================================
step = float(input("Resolusi (contoh 0.1): "))

# =====================================
# LINGKARAN
# =====================================
print("\n=== PARAMETER LINGKARAN ===")
r = float(input("Jari-jari (r): "))
xc1 = float(input("Pusat X: "))
yc1 = float(input("Pusat Y: "))

# =====================================
# ELIPS
# =====================================
print("\n=== PARAMETER ELIPS ===")
a_elips = float(input("Semi-sumbu horizontal (a): "))
b_elips = float(input("Semi-sumbu vertikal (b): "))
xc2 = float(input("Pusat X: "))
yc2 = float(input("Pusat Y: "))

# =====================================
# PARABOLA
# =====================================
print("\n=== PARAMETER PARABOLA ===")
a_parabola = float(input("Konstanta a: "))
xp = float(input("Vertex X: "))
yp = float(input("Vertex Y: "))
t_awal = float(input("t awal: "))
t_akhir = float(input("t akhir: "))

# =====================================
# HIPERBOLA
# =====================================
print("\n=== PARAMETER HIPERBOLA ===")
a_hip = float(input("Konstanta a: "))
b_hip = float(input("Konstanta b: "))
xc4 = float(input("Pusat X: "))
yc4 = float(input("Pusat Y: "))

# =====================================
# PERHITUNGAN LINGKARAN
# =====================================
theta = np.arange(0, 2*np.pi, step)

x_circle = xc1 + r * np.cos(theta)
y_circle = yc1 + r * np.sin(theta)

# =====================================
# PERHITUNGAN ELIPS
# =====================================
x_ellipse = xc2 + a_elips * np.cos(theta)
y_ellipse = yc2 + b_elips * np.sin(theta)

# =====================================
# PERHITUNGAN PARABOLA
# =====================================
t = np.arange(t_awal, t_akhir, step)

x_parabola = xp + a_parabola * (t**2)
y_parabola = yp + 2 * a_parabola * t

# =====================================
# PERHITUNGAN HIPERBOLA
# =====================================
theta_h = np.arange(-1.4, 1.4, step)

x_hyperbola = xc4 + a_hip * (1 / np.cos(theta_h))
y_hyperbola = yc4 + b_hip * np.tan(theta_h)

# =====================================
# JUMLAH TITIK
# =====================================
print("\n===== JUMLAH TITIK =====")
print("Lingkaran :", len(x_circle))
print("Elips     :", len(x_ellipse))
print("Parabola  :", len(x_parabola))
print("Hiperbola :", len(x_hyperbola))

# =====================================
# VISUALISASI
# =====================================
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Lingkaran
axs[0, 0].scatter(x_circle, y_circle, s=10)
axs[0, 0].set_title(f'Lingkaran ({len(x_circle)} titik)')
axs[0, 0].grid(True)
axs[0, 0].axis('equal')

# Elips
axs[0, 1].scatter(x_ellipse, y_ellipse, s=10)
axs[0, 1].set_title(f'Elips ({len(x_ellipse)} titik)')
axs[0, 1].grid(True)
axs[0, 1].axis('equal')

# Parabola
axs[1, 0].scatter(x_parabola, y_parabola, s=10)
axs[1, 0].set_title(f'Parabola ({len(x_parabola)} titik)')
axs[1, 0].grid(True)
axs[1, 0].axis('equal')

# Hiperbola
axs[1, 1].scatter(x_hyperbola, y_hyperbola, s=10)
axs[1, 1].set_title(f'Hiperbola ({len(x_hyperbola)} titik)')
axs[1, 1].grid(True)
axs[1, 1].axis('equal')

plt.suptitle(
    f"Perbandingan Kurva Parametrik (Resolusi = {step})",
    fontsize=14
)

plt.tight_layout()
plt.show()