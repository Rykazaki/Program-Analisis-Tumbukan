# Tugas Besar Kelompok 3
# PROGRAM    : Program Analisis Tumbukan Dua Benda Tegar
# DESKRIPSI  : Program yang dapat menentukan jenis tumbukan dan kecepatan akhir benda
#              dalam 1 dimensi & 2 dimensi berdasarkan data yang diinput oleh pengguna.

# KAMUS
# dimensi                : array, berisi dimensi yang dapat dipilih
# nilai_pilihandimensi   : string, nilai dari dimensi yang dipilih


# ALGORITMA

# Import pathlib untuk mengakses gambar dalam folder assets
from pathlib import Path

# Import tkinter sebagai modul yang akan digunakan
import tkinter as tk
from tkinter import ttk, Canvas, Entry, Text, Button, PhotoImage, messagebox

# Import fungsi yang berada dalam file jenistumbukan.py dan vakhir.py
import jenistumbukan
import vakhir


# Inisialisasi path untuk mengakses folder assets yang berisi gambar
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

# Definisi fungsi relative_to_assets untuk mengakses path
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Set-up window dan menempatkannya di tengah layar
window = tk.Tk()
window.geometry("640x480")
windowWidth = 640
windowHeight = 480
positionRight = int(window.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(window.winfo_screenheight()/2.2 - windowHeight/2)
window.geometry("+{}+{}".format(positionRight, positionDown))
window.title('Program Analisis Tumbukan')
window.resizable(False, False)
window.configure(bg = "#FFFFFF")

# Membuat array yang berisi pilihan dimensi yang bisa dipilih dan
# menginisialisasi variabel nilai_pilihandimensi
dimensi = ['1 Dimensi', '2 Dimensi']
nilai_pilihandimensi = tk.StringVar()

# Mengubah font dan size font option menu
ttk.Style().configure('TMenubutton', font=("Montserrat SemiBold", 18 * -1))

# Membuat canvas untuk text dan rectangle
canvasmain = Canvas(window, bg = "#FFFFFF", height = 480, width = 640, bd = 0, 
                highlightthickness = 0, relief = "ridge")
canvasmain.place(x = 0, y = 0)

# Membuat tiga rectangle sebagai dasar GUI
canvasmain.create_rectangle(0.0, 0.0, 640.0, 480.0, fill="#FFFFFF", outline="")
canvasmain.create_rectangle( 0.0, 0.0, 320.0, 480.0, fill="#FCA311", outline="")
canvasmain.create_rectangle( 29.0, 226.0, 288.0, 233.0, fill="#1D3557", outline="")

# Membuat text pilih dimensi
canvasmain.create_text(350.0, 80.0, anchor="nw", text="Pilih Dimensi :  ", 
                   fill="#000000", font=("Montserrat SemiBold", 18 * -1))

# Membuat OptionMenu pilihan dimensi
pilihandimensi = ttk.OptionMenu(window, nilai_pilihandimensi, dimensi[0], *dimensi)
pilihandimensi['menu'].configure(font=("Montserrat SemiBold", 18 * -1))
pilihandimensi.place(x=487.0, y=77.0, anchor="nw")

# Membuat button untuk memilih jenis program yang ingin dijalankan
# Button menentukan jenis tumbukan
button_image_jenistumbukan = PhotoImage(file=relative_to_assets(
    "button_jenistumbukan.png"))
button_jenistumbukan = Button(image=button_image_jenistumbukan, borderwidth=0, 
                              highlightthickness=0, 
                              command=lambda:  # Program akan terhubung langsung ke fungsi program_jenistumbukan 
                                               # dalam file jenistumbukan
                                  jenistumbukan.program_jenistumbukan(
                                      nilai_pilihandimensi.get()), 
                              relief="flat")
button_jenistumbukan.place(x=377.0, y=145.0, width=224.0, height=96.0)

# Button menentukan kecepatan akhir
button_image_vakhir = PhotoImage(
    file=relative_to_assets("button_vakhir.png"))
button_vakhir = Button(image=button_image_vakhir, borderwidth=0, 
                       highlightthickness=0, 
                       command=lambda:   # Program akan terhubung langsung ke fungsi program_vakhir
                                         # dalam file vakhir
                           vakhir.program_vakhir(
                               nilai_pilihandimensi.get()), 
                           relief="flat")
button_vakhir.place(x=377.0, y=284.0, width=224.0, height=96.0)

# Membuat text
canvasmain.create_text(29.0, 364.0, anchor="nw", text="Kelompok 3", fill="#000000", 
                   font=("Montserrat Regular", 14 * -1))

canvasmain.create_text(29.0, 382.0, anchor="nw", text="K30", fill="#000000", 
                   font=("Montserrat Regular", 14 * -1))

canvasmain.create_text(29.0, 63.0, anchor="nw", text="Program\nAnalisis\nTumbukan", 
                   fill="#000000", font=("Montserrat Bold", 36 * -1))

canvasmain.create_text(29.0, 268.0, anchor="nw", text='Program ini dapat digunakan\nmenentukan '
                   'jenis tumbukan \ndan kecepatan akhir setelah\ntumbukan', 
                   fill="#000000", font=("Montserrat Regular", 14 * -1))
canvasmain.create_text(29.0, 400.0, anchor="nw", text="KU-1102", fill="#000000", 
                   font=("Montserrat Regular", 14 * -1))

# Menjalankan aplikasi agar tetap berjalan sebelum di-close
window.mainloop()
