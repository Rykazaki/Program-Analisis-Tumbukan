# Tugas Besar Kelompok 3
# PROGRAM    : Program Analisis Tumbukan Dua Benda Tegar
# DESKRIPSI  : Program yang dapat menentukan jenis tumbukan dan kecepatan akhir benda
#              dalam 1 dimensi & 2 dimensi berdasarkan data yang diinput oleh pengguna.

# KAMUS
# dimensi                : array, berisi dimensi yang dapat dipilih
# nilai_pilihandimensi   : string, nilai dari dimensi yang dipilih


# ALGORITMA
# Import tkinter sebagai modul yang akan digunakan
import tkinter as tk
from tkinter import ttk

# Import fungsi yang berada dalam file jenistumbukan.py dan vakhir.py
import jenistumbukan
import vakhir

# Mendefinisikan jenis program yang tersedia
# Set-up window
mainwindow = tk.Tk()
mainwindow.title('Program Analisis Tumbukan')
mainwindow.resizable(width=False, height=False)

# Mengubah font dan size font untuk button dan option menu
ttk.Style().configure('TButton', font=('Helvetica', 12), padding=6)
ttk.Style().configure('TMenubutton', font=('Helvetica', 12), padding=6)

# Membuat array yang berisi pilihan dimensi yang bisa dipilih dan
# menginisialisasi variabel nilai_pilihandimensi
dimensi = ['1 Dimensi', '2 Dimensi']
nilai_pilihandimensi = tk.StringVar()

# Menampilkan judul  program menggunakan fungsi Label
title_mainwindow = ttk.Label(mainwindow, text='Program Analisis Tumbukan', 
                             font=('Helvetica', 20))
title_mainwindow.grid(row=0, column=0, columnspan=2, padx=20, pady=5)

title2_mainwindow = ttk.Label(mainwindow, text='Dua Benda Tegar', 
                              font=('Helvetica', 20))
title2_mainwindow.grid(row=1, column=0, columnspan=2, padx=20, pady=5)

# Membuat Label pilihan dimensi
label_pilihandimensi = ttk.Label(mainwindow, text='Pilih dimensi:', 
                                 font=('Helvetica', 12))
label_pilihandimensi.grid(row=2, column=0, pady=5, sticky='e')

# Membuat OptionMenu untuk memilih pilihan dimensi
pilihandimensi = ttk.OptionMenu(mainwindow, nilai_pilihandimensi, dimensi[0], *dimensi)
pilihandimensi.grid(row=2, column=1, pady=5, sticky='w')


# Membuat Button/tombol untuk memilih jenis program yang hendak dijalankan
button_jenis = ttk.Button(mainwindow, text='Menentukan Jenis Tumbukan', 
                          command=lambda : # Program akan terhubung langsung ke fungsi program_jenistumbukan 
                                           # dalam file jenistumbukan
                              jenistumbukan.program_jenistumbukan(
                                  nilai_pilihandimensi.get()))                                
button_jenis.grid(row=3,column=0, columnspan=2, pady=5)

button_kecepatan = ttk.Button(mainwindow, text='Menentukan Kecepatan Akhir', 
                              command=lambda :  # Program akan terhubung langsung ke fungsi program_vakhir 
                                                # dalam file vakhir
                                  vakhir.program_vakhir(
                                      nilai_pilihandimensi.get()))                        
button_kecepatan.grid(row=4, columnspan=2, column=0, pady=(5,10))

# Menjalankan aplikasi agar tetap berjalan sebelum di-close
mainwindow.mainloop()


