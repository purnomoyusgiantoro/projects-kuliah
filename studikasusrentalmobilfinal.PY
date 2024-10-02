import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3


hargamobil = {
    "Mobil Sedan": {"H": 150000, "M": 1000000, "B": 4000000},
    "Mobil SUV": {"H": 200000, "M": 1350000, "B": 5500000},
    "Mobil Alphard": {"H": 500000, "M": 3000000, "B": 14500000},}


conn = sqlite3.connect('data_transaksi.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users 
               (name TEXT PRIMARY KEY NOT NULL, jenis TEXT NOT NULL, kode TEXT NOT NULL,
                harga INTEGER NOT NULL, lama INTEGER NOT NULL, subtotal INTEGER NOT NULL, potongan INTEGER NOT NULL, 
                total INTEGER NOT NULL, bayar INTEGER NOT NULL,jumlahbayar INTEGER NOT NULL ,kembali INTEGER NOT NULL)''')
conn.commit()


def aktifkan_isian():
    nama_entry.config(state='normal')
    jenis_combobox.config(state='normal')
    kode_combobox.config(state='normal')
    lama_entry.config(state='normal')
    uang_entry.config(state='normal')


def tambah():
    aktifkan_isian()
    bersihkan_isian()
    nama_entry.focus()


def simpan():
    try:
        nama_user = nama_entry.get()
        jenismobil = jenis_combobox.get()
        kodepinjaman = kode_combobox.get()
        lamarental = int(lama_entry.get())
        uangbayar = int(uang_entry.get())

        if not jenismobil or not kodepinjaman or not lamarental or not uangbayar:
            raise ValueError("Semua kolom harus diisi")

        hargasewa = hargamobil[jenismobil][kodepinjaman]
        subtotal = hargasewa * lamarental

        if lamarental > 2:
            potongan = subtotal * 0.1
        else:
            potongan = 0

        totalbayar = subtotal - potongan
        jumlahbayar = totalbayar
        uangkembali = uangbayar - totalbayar

        cursor.execute("SELECT name FROM users WHERE name=?", (nama_user,))
        if cursor.fetchone():  
            raise ValueError("Data dengan nama yang sama sudah ada")
        cursor.execute("""
            INSERT INTO users (name, jenis, kode, harga, lama, subtotal, potongan, total, bayar, jumlahbayar, kembali)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", 
            (nama_user, jenismobil, kodepinjaman, hargasewa, lamarental, subtotal, potongan, totalbayar, uangbayar, jumlahbayar, uangkembali))

        conn.commit()
        muat_data()
        bersihkan_isian()
        nonaktifkan_isian()

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))
    except sqlite3.IntegrityError:
        messagebox.showwarning("Kesalahan Basis Data", "Data gagal disimpan, periksa kembali input")



def hapus():
    selected_item = tree.selection()
    if selected_item:
        nama_user = tree.item(selected_item[0], 'values')[0]
        cursor.execute("DELETE FROM users WHERE name=?", (nama_user,))
        conn.commit()
        tree.delete(selected_item[0])
        bersihkan_isian()
    else:
        messagebox.showwarning("Kesalahan", "Pilih data yang akan dihapus")


def edit():
    try:
        nama_user = nama_entry.get()
        jenismobil = jenis_combobox.get()
        kodepinjaman = kode_combobox.get()
        lamarental = int(lama_entry.get())
        uangbayar = int(uang_entry.get())

        if not jenismobil or not kodepinjaman or not lamarental or not uangbayar:
            raise ValueError("Semua kolom harus diisi")

        hargasewa = hargamobil[jenismobil][kodepinjaman]
        subtotal = hargasewa * lamarental

        if lamarental > 2:
            potongan = subtotal * 0.1
        else:
            potongan = 0

        totalbayar = subtotal - potongan
        jumlahbayar = totalbayar
        uangkembali = uangbayar - totalbayar


        cursor.execute("""
            REPLACE INTO users (name, jenis, kode, harga, lama, subtotal, potongan, total, bayar, jumlahbayar, kembali) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (nama_user, jenismobil, kodepinjaman, hargasewa, lamarental, subtotal, potongan, totalbayar, uangbayar, jumlahbayar, uangkembali))

        conn.commit()
        muat_data()
        bersihkan_isian()
        nonaktifkan_isian()

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

        
def muat_data():
    for row in tree.get_children():
        tree.delete(row)
    cursor.execute("SELECT * FROM users")
    for row in cursor.fetchall():
        tree.insert('', tk.END, values=row)


def bersihkan_isian():
    nama_entry.delete(0, tk.END)
    jenis_combobox.set('')
    kode_combobox.set('')
    harga_label.config(text="")
    lama_entry.delete(0, tk.END)
    subtotal_label.config(text="")
    potongan_label.config(text="")
    total_label.config(text="")
    uang_entry.delete(0, tk.END)
    ukembali_label.config(text="")
    jumlahbayar_label.config(text="")


def nonaktifkan_isian():
    nama_entry.config(state='disabled')
    jenis_combobox.config(state='disabled')
    kode_combobox.config(state='disabled')
    lama_entry.config(state='disabled')
    uang_entry.config(state='disabled')


def keluar():
    window.destroy()


def hitung(event=None):
    try:
        jenismobil = jenis_combobox.get()
        kodepinjaman = kode_combobox.get()
        lamarental = int(lama_entry.get()) if lama_entry.get() else 0
        uangbayar = int(uang_entry.get()) if uang_entry.get() else 0

        if not jenismobil or not kodepinjaman or lamarental <= 0 or uangbayar <= 0:
            return

        hargasewa = hargamobil[jenismobil][kodepinjaman]
        subtotal = hargasewa * lamarental

        if lamarental > 2:
            potongan = subtotal * 0.1
        else:
            potongan = 0

        totalbayar = subtotal - potongan
        jumlahbayar = totalbayar

        harga_label.config(text=f"Rp. {hargasewa}")
        subtotal_label.config(text=f"Rp. {subtotal}")
        potongan_label.config(text=f"Rp. {potongan}")
        total_label.config(text=f"Rp. {totalbayar}")
        jumlahbayar_label.config(text=f"Rp. {jumlahbayar}")

        uangkembali = uangbayar - totalbayar
        ukembali_label.config(text=f"Rp. {uangkembali}")

    except ValueError:
        messagebox.showerror("Input Error", "Masukkan angka yang valid.")


def harga_sewa(event=None):
    try:
        jenismobil = jenis_combobox.get()
        kodepinjaman = kode_combobox.get()

        if not jenismobil or not kodepinjaman:
            return

        hargasewa = hargamobil[jenismobil][kodepinjaman]
        harga_label.config(text=f"Rp. {hargasewa}")

        hitung()

    except ValueError:
        messagebox.showerror("Input Error", "Masukkan angka yang valid.")


def lamarental(event=None):
    try:
        jenismobil = jenis_combobox.get()
        kodepinjaman = kode_combobox.get()
        lamarental = int(lama_entry.get()) if lama_entry.get() else 0

        if not jenismobil or not kodepinjaman or lamarental <= 0:
            return

        hargasewa = hargamobil[jenismobil][kodepinjaman]
        subtotal = hargasewa * lamarental

        if lamarental > 2:
            potongan = subtotal * 0.1
        else:
            potongan = 0

        totalbayar = subtotal - potongan

        harga_label.config(text=f"Rp. {hargasewa}")
        subtotal_label.config(text=f"Rp. {subtotal}")
        potongan_label.config(text=f"Rp. {potongan}")
        total_label.config(text=f"Rp. {totalbayar}")
       
        hitung()

    except ValueError:
            messagebox.showerror("Input Error", "Masukkan angka yang valid.")


def uangbayar(event=None):
    try:
        jenismobil = jenis_combobox.get()
        kodepinjaman = kode_combobox.get()
        lamarental = int(lama_entry.get()) if lama_entry.get() else 0
        uangbayar = int(uang_entry.get()) if uang_entry.get() else 0

        if not jenismobil or not kodepinjaman or lamarental <= 0 or uangbayar <= 0:
            return

        hargasewa = hargamobil[jenismobil][kodepinjaman]
        subtotal = hargasewa * lamarental

        if lamarental > 2:
            potongan = subtotal * 0.1
        else:
            potongan = 0

        totalbayar = subtotal - potongan
        jumlahbayar = totalbayar

        uangkembali = uangbayar - totalbayar
        ukembali_label.config(text=f"Rp. {uangkembali}")

        hitung()

    except ValueError:
        messagebox.showerror("Input Error", "Masukkan angka yang valid.")


def data(event=None):
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        values = item['values']
        if values:
            nama_entry.config(state='normal')
            jenis_combobox.config(state='normal')
            kode_combobox.config(state='normal')
            lama_entry.config(state='normal')
            uang_entry.config(state='normal')

            nama_entry.delete(0, tk.END)
            nama_entry.insert(0, values[0])
            jenis_combobox.set(values[1])
            kode_combobox.set(values[2])
            harga_label.config(text=f"Rp. {values[3]}")
            lama_entry.delete(0, tk.END)
            lama_entry.insert(0, values[4])
            subtotal_label.config(text=f"Rp. {values[5]}")
            potongan_label.config(text=f"Rp. {values[6]}")
            total_label.config(text=f"Rp. {values[7]}")
            uang_entry.delete(0, tk.END)
            uang_entry.insert(0, values[8])
            jumlahbayar_label.config(text=f"Rp. {values[9]}")
            ukembali_label.config(text=f"Rp. {values[10]}")

            hitung()


window = tk.Tk()
lebar = 800
tinggi = 600
window.title("Detail Transaksi Rental Mobil")
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()

newx = int((screenwidth / 2) - (lebar / 2))
newy = int((screenheight / 2) - (tinggi / 2) - 100)
window.geometry(f"{lebar}x{tinggi}+{newx}+{newy}")


for i in range(10):
    window.columnconfigure(i, weight=1)
for i in range(10):
    window.rowconfigure(i, weight=1)

#IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII

# Komponen GUI
t_button = tk.Button(window, text="DETAIL TRANSAKSI", state="disabled", font="Arial 20 underline")
t_button.grid(row=0, column=0, padx=10, pady=10, sticky='wens', columnspan=10)

tk.Label(window, text="Nama Perental*",font=10).grid(row=1, column=0, sticky='w')
nama_entry = tk.Entry(window)
nama_entry.grid(row=1, column=2, padx=10, pady=5, sticky='wens')

tk.Label(window, text="Jenis Mobil*",font=10).grid(row=2, column=0, sticky='w')
jenis_combobox = ttk.Combobox(window, values=list(hargamobil.keys()), state='readonly')
jenis_combobox.grid(row=2, column=2, padx=10, pady=5, sticky='wens')

tk.Label(window, text="Kode Pinjam*",font=10).grid(row=3, column=0, sticky='w')
kode_combobox = ttk.Combobox(window, values=["H", "M", "B"], state='readonly')
kode_combobox.grid(row=3, column=2, padx=10, pady=5, sticky='wens')

tk.Label(window, text="Harga Sewa",font=10).grid(row=4, column=0, sticky='w')
harga_label = tk.Label(window, text="Rp. 0",relief= "ridge",bg="#FFFFFF",anchor='w')
harga_label.grid(row=4, column=2, padx=10, pady=5, sticky='wens')

#IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII

tk.Label(window, text="Lama Rental*",font=10).grid(row=1, column=4, sticky='w')
lama_entry = tk.Entry(window)
lama_entry.grid(row=1, column=5, padx=10, pady=5, sticky='wens')

tk.Label(window, text="SubTotal",font=10).grid(row=2, column=4, sticky='w')
subtotal_label = tk.Label(window, text="Rp. 0",relief= "ridge",bg="#FFFFFF",anchor='w')
subtotal_label.grid(row=2, column=5, padx=10, pady=5, sticky='wens')

tk.Label(window, text="Potongan",font=10).grid(row=3, column=4, sticky='w')
potongan_label = tk.Label(window, text="Rp. 0",relief= "ridge",bg="#FFFFFF",anchor='w')
potongan_label.grid(row=3, column=5, padx=10, pady=5, sticky='wens')

tk.Label(window, text="Total",font=10).grid(row=4, column=4, sticky='w')
total_label = tk.Label(window, text="Rp. 0",relief= "ridge",bg="#FFFFFF",anchor='w')
total_label.grid(row=4, column=5, padx=10, pady=5, sticky='wens')

#IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII

tk.Label(window, text="Uang Bayar*",font=10).grid(row=6, column=0, sticky='w')
uang_entry = tk.Entry(window)
uang_entry.grid(row=6, column=2, padx=10, pady=5, sticky='wens')

tk.Label(window, text="Jumlah Bayar",font=10).grid(row=7, column=0, sticky='w')
jumlahbayar_label = tk.Label(window, text="Rp. 0",relief= "ridge",bg="#FFFFFF",anchor='w')
jumlahbayar_label.grid(row=7, column=2, padx=10, pady=5, sticky='wens')

tk.Label(window, text="Uang Kembali",font=10).grid(row=8, column=0, sticky='w')
ukembali_label = tk.Label(window, text="Rp. 0",relief= "ridge",bg="#FFFFFF",anchor='w')
ukembali_label.grid(row=8, column=2,padx=10, pady=5, sticky='wens')


#IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII

tombol_tambah = tk.Button(window, text="Tambah", command=tambah)
tombol_tambah.grid(row=1, column=9, padx=10, pady=5, sticky='wens')

tombol_simpan = tk.Button(window, text="Simpan", command=simpan)
tombol_simpan.grid(row=2, column=9, padx=10, pady=5, sticky='wens')

tombol_hapus = tk.Button(window, text="Hapus", command=hapus)
tombol_hapus.grid(row=3, column=9, padx=10, pady=5, sticky='wens')

tombol_edit = tk.Button(window, text="Edit", command=edit)
tombol_edit.grid(row=4, column=9, padx=10, pady=5, sticky='wens')

tombol_batal = tk.Button(window, text="Batal", command=bersihkan_isian)
tombol_batal.grid(row=5, column=9, padx=10, pady=5, sticky='wens')

tombol_keluar = tk.Button(window, text="Keluar", command=keluar)
tombol_keluar.grid(row=6, column=9, padx=10, pady=5, sticky='wens')



tree = ttk.Treeview(window, columns=("nama", "jenis", "kode", "harga", "lama", "subtotal", 
                                     "potongan", "total", "bayar","jumlahbayar", "kembali"), show='headings')
tree.heading("nama", text="Nama")
tree.heading("jenis", text="Jenis")
tree.heading("kode", text="Kode")
tree.heading("harga", text="Harga")
tree.heading("lama", text="Lama")
tree.heading("subtotal", text="Subtotal")
tree.heading("potongan", text="Potongan")
tree.heading("total", text="Total")
tree.heading("bayar", text="Bayar")
tree.heading("jumlahbayar", text="Jumlah Bayar")
tree.heading("kembali", text="Kembali")
tree.grid(row=13, column=0, columnspan=10, sticky='wens')


jenis_combobox.bind("<<ComboboxSelected>>", harga_sewa)
kode_combobox.bind("<<ComboboxSelected>>", harga_sewa)
lama_entry.bind("<KeyRelease>", lamarental)
uang_entry.bind("<KeyRelease>", uangbayar)


tree.bind("<ButtonRelease-1>", data)


nonaktifkan_isian()
muat_data()
window.mainloop()
