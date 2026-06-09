import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# PARAMETER RESOLUSI
# ==========================================
resolutions = [0.5, 0.1, 0.01]

# ==========================================
# LINGKARAN
# ==========================================
def circle(r, step):
    theta = np.arange(0, 2*np.pi, step)

    x = r * np.cos(theta)
    y = r * np.sin(theta)

    return x, y

# ==========================================
# ELIPS
# ==========================================
def ellipse(a, b, step):
    theta = np.arange(0, 2*np.pi, step)

    x = a * np.cos(theta)
    y = b * np.sin(theta)

    return x, y

# ==========================================
# PARABOLA
# ==========================================
def parabola(a, step):
    t = np.arange(-5, 5, step)

    x = a * t**2
    y = 2 * a * t

    return x, y

# ==========================================
# HIPERBOLA
# ==========================================
def hyperbola(a, b, step):
    theta = np.arange(-1.4, 1.4, step)

    x = a * (1/np.cos(theta))  # sec(theta)
    y = b * np.tan(theta)

    return x, y


# ==========================================
# VISUALISASI
# ==========================================
fig, axs = plt.subplots(4, 3, figsize=(16, 16))

for col, step in enumerate(resolutions):

    # Lingkaran
    x, y = circle(5, step)
    axs[0, col].scatter(x, y, s=10)
    axs[0, col].set_title(f'Lingkaran\nstep={step}')
    axs[0, col].set_aspect('equal')
    axs[0, col].grid(True)
    axs[0, col].set_xlim(-6, 6)
    axs[0, col].set_ylim(-6, 6)

    # Elips
    x, y = ellipse(6, 3, step)
    axs[1, col].scatter(x, y, s=10)
    axs[1, col].set_title(f'Elips\nstep={step}')
    axs[1, col].set_aspect('equal')
    axs[1, col].grid(True)
    axs[1, col].set_xlim(-7, 7)
    axs[1, col].set_ylim(-4, 4)

    # Parabola
    x, y = parabola(1, step)
    axs[2, col].scatter(x, y, s=10)
    axs[2, col].set_title(f'Parabola\nstep={step}')
    axs[2, col].set_aspect('equal')
    axs[2, col].grid(True)
    axs[2, col].set_xlim(-1, 26)
    axs[2, col].set_ylim(-12, 12)

    # Hiperbola
    x, y = hyperbola(2, 2, step)
    axs[3, col].scatter(x, y, s=10)
    axs[3, col].set_title(f'Hiperbola\nstep={step}')
    axs[3, col].set_aspect('equal')
    axs[3, col].grid(True)
    axs[3, col].set_xlim(-15, 15)
    axs[3, col].set_ylim(-15, 15)

plt.subplots_adjust(
    left=0.05,
    right=0.95,
    top=0.95,
    bottom=0.05,
    hspace=0.5,
    wspace=0.3
)

plt.show()