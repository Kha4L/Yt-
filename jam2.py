import tkinter as tk
from time import strftime

# Fungsi untuk update waktu
def update_waktu():
    # Format waktu: Jam:Menit:Detik
    waktu_sekarang = strftime('%H:%M:%S')
    label_jam.config(text=waktu_sekarang)
    
    # Format tanggal: Hari, Tanggal Bulan Tahun
    tanggal_sekarang = strftime('%A, %d %B %Y')
    label_tanggal.config(text=tanggal_sekarang)
    
    # Update setiap 1000 milliseconds (1 detik)
    label_jam.after(1000, update_waktu)

# Buat window utama
window = tk.Tk()
window.title("Jam Digital")
window.geometry("500x250")
window.resizable(False, False)

# Set background color
window.config(bg="#2C3E50")

# Label untuk judul
label_judul = tk.Label(
    window,
    text="JAM-Jaman",
    font=("Arial", 16, "bold"),
    bg="#2C3E50",
    fg="#ECF0F1"
)
label_judul.pack(pady=20)

# Label untuk menampilkan jam
label_jam = tk.Label(
    window,
    font=("Digital-7", 60, "bold"),  # Bisa ganti dengan "Arial" kalau font Digital-7 tidak ada
    bg="#2C3E50",
    fg="#3498DB"
)
label_jam.pack()

# Label untuk menampilkan tanggal
label_tanggal = tk.Label(
    window,
    font=("Arial", 18),
    bg="#2C3E50",
    fg="#ECF0F1"
)
label_tanggal.pack(pady=10)

# Label untuk footer
label_footer = tk.Label(
    window,
    text="Waktu indonesia bagian barat (WIB)",
    font=("Arial", 10),
    bg="#2C3E50",
    fg="#95A5A6"
)
label_footer.pack(side="bottom", pady=10)

# Panggil fungsi update_waktu untuk pertama kali
update_waktu()

# Jalankan aplikasi
window.mainloop()
