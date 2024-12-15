import matplotlib.pyplot as plt

def midpoint_circle_with_iterations(x_center, y_center, radius):
    """
    Algoritma Midpoint Circle dengan iterasi yang berakhir saat x >= y.
    """
    # Inisialisasi nilai awal
    x = 0
    y = int(radius)  # Titik awal pada kuadran pertama, y = r (dibulatkan jika pecahan)
    if isinstance(radius, float):
        p = 5/4 - radius  # Jika radius adalah pecahan
    else:
        p = 1 - radius  # P0 = 1 - r jika integer

    iteration = 0
    all_points = []  # Menyimpan titik-titik hasil perhitungan

    # Fungsi untuk menghitung titik-titik simetris
    def add_symmetric_points(x, y):
        return [
            (x_center + x, y_center + y),  # Kuadran 1
            (x_center - x, y_center + y),  # Kuadran 2
            (x_center + x, y_center - y),  # Kuadran 3
            (x_center - x, y_center - y),  # Kuadran 4
            (x_center + y, y_center + x),  # Kuadran 5
            (x_center - y, y_center + x),  # Kuadran 6
            (x_center + y, y_center - x),  # Kuadran 7
            (x_center - y, y_center - x)   # Kuadran 8
        ]
    
    # Iterasi hingga x >= y
    while x <= y:
        # Menampilkan hasil iterasi
        print(f"K = {iteration}")
        print(f"X{iteration} = {x}, Y{iteration} = {y}, P{iteration} = {p}")

        # Jika P < 0, update X dan Y
        if p < 0:
            x += 1
            p += 2 * x + 1
        else:
            x += 1
            y -= 1
            p += 2 * x - 2 * y + 1

        # Simetri 8 Titik: Menambahkan titik simetris untuk iterasi saat ini
        symmetric_points = add_symmetric_points(x, y)
        all_points.extend(symmetric_points)

        # Menampilkan titik simetris yang dihasilkan
        print(f"Simetri 8 titik: {symmetric_points}")

        # Menampilkan gerakan relatif terhadap pusat
        print("Gerakan relatif terhadap pusat:")
        for point in symmetric_points:
            relative_x = point[0] - x_center
            relative_y = point[1] - y_center
            print(f"Titik {point} (Relatif: x = {relative_x}, y = {relative_y})")

        # Menampilkan titik selanjutnya
        print(f"Titik selanjutnya: ({x}, {y})")

        iteration += 1  # Menambah iterasi untuk langkah berikutnya

    return all_points

def plot_circle_with_coordinates(x_center, y_center, radius, points):
    """
    Membuat plot lingkaran berdasarkan titik-titik dari semua kuadran,
    dan menambahkan koordinat (x, y) pada setiap titik.
    """
    fig, ax = plt.subplots()

    # Plot titik-titik hasil perhitungan
    for point in points:
        ax.plot(point[0], point[1], 'ro')  # Titik merah untuk hasil
        # Menambahkan koordinat (x, y) pada setiap titik
        ax.text(point[0] + 0.3, point[1] + 0.3, f"({point[0]},{point[1]})", fontsize=8, color='green')

    # Plot pusat lingkaran
    ax.plot(x_center, y_center, 'bo')  # Titik biru untuk pusat

    # Mengatur properti plot
    ax.set_aspect('equal')
    ax.set_xlim(x_center - radius - 2, x_center + radius + 2)
    ax.set_ylim(y_center - radius - 2, y_center + radius + 2)
    ax.set_title(f"Kurva Lingkaran dengan Pusat ({x_center}, {y_center}) dan Jari-jari {radius}")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.grid(True)
    plt.show()

# Input data lingkaran dari pengguna
try:
    x_center = int(input("Masukkan koordinat x pusat lingkaran: "))
    y_center = int(input("Masukkan koordinat y pusat lingkaran: "))
    radius = float(input("Masukkan jari-jari lingkaran: "))  # Menerima radius sebagai float
except ValueError:
    print("Input tidak valid. Harap masukkan angka.")
    exit()

# Perhitungan hingga x >= y
points = midpoint_circle_with_iterations(x_center, y_center, radius)

# Plot lingkaran dengan koordinat (x, y) pada setiap titik
plot_circle_with_coordinates(x_center, y_center, radius, points)
