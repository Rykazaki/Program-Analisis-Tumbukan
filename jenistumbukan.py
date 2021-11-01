# Tugas Besar Kelompok 3
# PROGRAM    : Subprogram Menentukan Jenis Tumbukan
# DESKRIPSI  : Program yang dapat menentukan jenis tumbukan dalam 1 dimensi 
#              & 2 dimensi berdasarkan data yang diinput oleh pengguna.

# CREDIT
# Pembuatan GUI dibantu dengan modul Tkinter Designer karya Parth Jadhav

# KAMUS LOKAL
# pilihandimensi    : string, nilai dari dimensi yang dipilih
# m1                : float, nilai dari massa benda 1 
# v1_awal           : float, nilai dari kecepatan benda 1 sebelum tumbukan     
# v1x_awal          : float, nilai komponen sumbu x dari kecepatan benda 1 sebelum tumbukan
# v1y_awal          : float, nilai komponen sumbu y dari kecepatan benda 1 sebelum tumbukan
# v1_akhir          : float, nilai dari kecepatan benda 1 setelah tumbukan     
# v1x_akhir         : float, nilai komponen sumbu x dari kecepatan benda 1 setelah tumbukan
# v1y_akhir         : float, nilai komponen sumbu y dari kecepatan benda 1 setelah tumbukan
# m2                : float, nilai dari massa benda 2 
# v2_awal           : float, nilai dari kecepatan benda 2 sebelum tumbukan     
# v2x_awal          : float, nilai komponen sumbu x dari kecepatan benda 2 sebelum tumbukan
# v2y_awal          : float, nilai komponen sumbu y dari kecepatan benda 2 sebelum tumbukan
# v2_akhir          : float, nilai dari kecepatan benda 2 setelah tumbukan     
# v2x_akhir         : float, nilai komponen sumbu x dari kecepatan benda 2 setelah tumbukan
# v2y_akhir         : float, nilai komponen sumbu y dari kecepatan benda 2 setelah tumbukan
# momentum_awal     : float, nilai dari momentum sistem sebelum tumbukan
# momentumx_awal    : float, nilai komponen sumbu x dari momentum sistem sebelum tumbukan
# momentumy_awal    : float, nilai komponen sumbu y dari momentum sistem sebelum tumbukan
# momentum_akhir    : float, nilai dari momentum sistem setelah tumbukan
# momentumx_akhir   : float, nilai komponen sumbu x dari momentum sistem setelah tumbukan
# momentumy_akhir   : float, nilai komponen sumbu y dari momentum sistem setelah tumbukan
# restitusi         : float, nilai koefisien restitusi dari tumbukan
# ek_awal           : float, nilai energi kinetik sistem sebelum tumbukan
# ek_akhir          : float, nilai energi kinetik sistem setelah tumbukan



# ALGORITMA
# Import modul tkinter yang dibutuhkan
import tkinter as tk
from tkinter import Canvas, Entry, Text, Button, PhotoImage, messagebox

# Import pathlib untuk mengakses gambar dalam folder assets
from pathlib import Path

# Inisialisasi path untuk mengakses folder assets yang berisi gambar               
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

# Definisi fungsi relative_to_assets untuk mengakses path
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def program_jenistumbukan(pilihandimensi): # Mendefinisikan program untuk menentukan jenis tumbukan

# =============================================================================
# Algoritma Bagian Pemrosesan Data
# Pada bagian ini, terdapat dua fungsi, yaitu jenistumbukan_satudimensi dan
# jenistumbukan_duadimensi yang berguna untuk memproses input dan menampilkan
# output pada display.
# =============================================================================

    def jenistumbukan_satudimensi(): # Mendefinisikan program untuk menentukan kecepatan dalam 1 dimensi
        try:
            m1 = float(entry_massa1.get())              # Menerima input berupa massa benda 1 dalam kg
            v1_awal = float(entry_v1awal.get())         # Menerima input berupa kecepatan awal benda 1 dalam m/s
            v1_akhir = float(entry_v1akhir.get())       # Menerima input berupa kecepatan akhir benda 1 dalam m/s
        
            m2 = float(entry_massa2.get())              # Menerima input berupa massa benda 2 dalam kg
            v2_awal = float(entry_v2awal.get())         # Menerima input berupa kecepatan awal benda 2 dalam m/s
            v2_akhir = float(entry_v2akhir.get())       # Menerima input berupa kecepatan akhir benda 2 dalam m/s
            
            if m1 <= 0 or m2 <= 0:
                messagebox.showerror('Error', 'Massa harus bernilai positif.',      # Memunculkan messagebox Error jika massa yang dimasukkan bernilai negatif
                                     parent=jenistumbukan1dimensi)
                return
            
            if v1_awal == 0 and v2_awal == 0:                                       # Memunculkan messagebox Error jika kecepatan awal kedua benda nol
                messagebox.showerror('Error', 
                                     'Kedua benda diam dan tidak akan bertumbukan.', 
                                     parent=jenistumbukan1dimensi)
                return
            
            if v1_awal == v2_awal:                                                  # Memunculkan messagebox Error jika kecepatan awal kedua benda sama
                messagebox.showerror('Error', 
                                     'Kedua benda memiliki kecepatan awal yang sama '
                                     'dan tidak akan bertumbukan.', 
                                     parent=jenistumbukan1dimensi)
                return
                
            momentum_awal = round(m1*v1_awal + m2*v2_awal, 3)                       # Rumus perhitungan untuk menentukan momentum awal
            momentum_akhir = round(m1*v1_akhir + m2*v2_akhir,3)                     # Rumus perhitungan untuk menentukan momentum akhir
            restitusi = round((v1_akhir-v2_akhir)/(v2_awal-v1_awal), 3)             # Rumus perhitungan untuk menentukan koefisien restitusi
            ek_awal = round((1/2)*m1*(v1_awal**2)+(1/2)*m2*(v2_awal**2), 3)         # Rumus perhitungan untuk menentukan energi kinetik awal sistem
            ek_akhir = round((1/2)*m1*(v1_akhir**2)+(1/2)*m2*(v2_akhir**2), 3)      # Rumus perhitungan untuk menentukan energi kinetik akhir sistem
            
        except ValueError:
            # Memberikan pesan error jika nilai yang diinput bukan merupakan bilangan real
            messagebox.showerror('Error', 'Masukkan bilangan real.',                
                             parent=jenistumbukan1dimensi)
            return
            
        except:
            # Memberikan pesan error jika terjadi error selain error yang telah didefinisikan sebelumnya
            messagebox.showerror('Error', 'Terjadi error.', parent=jenistumbukan1dimensi)  
            return
            
        if momentum_awal != momentum_akhir:
            # Ketika input tidak sesuai dengan Hukum Kekekalan Momentum, maka jenis tumbukan tidak dapat ditentukan
            messagebox.showwarning('Peringatan',
                                   'Nilai yang anda masukkan tidak sesuai dengan '
                                   'Hukum Kekekalan Momentum, sehingga jenis '
                                   'tumbukan tidak dapat ditentukan.', 
                                   parent=jenistumbukan1dimensi)
            text_jenistumbukan.config(state='normal')
            text_jenistumbukan.delete(1.0, 'end')
            text_jenistumbukan.insert(1.0, 'N/A')
            text_jenistumbukan.config(state='disabled')
            
        elif restitusi == 0:    
            # Memunculkan output jenis tumbukan 'inelastis sempurna' jika koefisien restitusi bernilai 0
            text_jenistumbukan.config(state='normal')
            text_jenistumbukan.delete(1.0, 'end')
            text_jenistumbukan.insert(1.0, 'inelastis sempurna')
            text_jenistumbukan.config(state='disabled')
      
        elif restitusi > 0 and restitusi < 1:   
            # Memunculkan output jenis tumbukan 'elastis sebagian' jika koefisien restitusi bernilai 0<e<1
            text_jenistumbukan.config(state='normal')
            text_jenistumbukan.delete(1.0, 'end')
            text_jenistumbukan.insert(1.0, 'elastis sebagian')
            text_jenistumbukan.config(state='disabled')
    
        elif restitusi == 1:    
            # Memunculkan output jenis tumbukan 'elastis sempurna' jika koefisien restitusi bernilai 1
            text_jenistumbukan.config(state='normal')
            text_jenistumbukan.delete(1.0, 'end')
            text_jenistumbukan.insert(1.0, 'elastis sempurna')
            text_jenistumbukan.config(state='disabled')
       
        elif restitusi > 1:     
            # Memunculkan output jenis tumbukan 'superelastis' jika koefisien restitusi bernilai >1
            text_jenistumbukan.config(state='normal')
            text_jenistumbukan.delete(1.0, 'end')
            text_jenistumbukan.insert(1.0, 'superelastis')
            text_jenistumbukan.config(state='disabled')
       
        else:   
            # Memunculkan output jenis tumbukan 'N/A jika koefisien restitusi bernilai <0
            text_jenistumbukan.config(state='normal')
            text_jenistumbukan.delete(1.0, 'end')
            text_jenistumbukan.insert(1.0, 'N/A')
            text_jenistumbukan.config(state='disabled')
        
        # Memunculkan output koefisien restitusi
        text_restitusi.config(state='normal')                                           
        text_restitusi.delete(1.0, 'end')
        text_restitusi.insert(1.0, f'{restitusi}')
        text_restitusi.config(state='disabled')
    
        # Memunculkan output momentum sistem sebelum tumbukan
        text_momentumawal.config(state='normal')                                        
        text_momentumawal.delete(1.0, 'end')
        text_momentumawal.insert(1.0, f'{momentum_awal}')
        text_momentumawal.config(state='disabled')
        
        # Memunculkan output momentum sistem setelah tumbukan
        text_momentumakhir.config(state='normal')                                       
        text_momentumakhir.delete(1.0, 'end')
        text_momentumakhir.insert(1.0, f'{momentum_akhir}')
        text_momentumakhir.config(state='disabled')
        
        # Memunculkan output energi sistem kinetik sebelum tumbukan
        text_ekawal.config(state='normal')                                              
        text_ekawal.delete(1.0, 'end')
        text_ekawal.insert(1.0, f'{ek_awal}')
        text_ekawal.config(state='disabled')
        
        # Memunculkan output energi sistem kinetik setelah tumbukan
        text_ekakhir.config(state='normal') 
        text_ekakhir.delete(1.0, 'end')                                            
        text_ekakhir.insert(1.0, f'{ek_akhir}')
        text_ekakhir.config(state='disabled')
    
    def jenistumbukan_duadimensi(): # Mendefinisikan program untuk menentukan jenis tumbukan dalam 2 dimensi
        try:
            m1 = float(entry_massa1.get())                          # Menerima input berupa massa benda 1 dalam kg
            v1x_awal = float(entry_v1xawal.get())                   # Menerima input berupa kecepatan awal benda 1 di sumbu-X dalam m/s
            v1y_awal = float(entry_v1yawal.get())                   # Menerima input berupa kecepatan awal benda 1 di sumbu-Y dalam m/s
            v1x_akhir = float(entry_v1xakhir.get())                 # Menerima input berupa kecepatan akhir benda 1 di sumbu-X dalam m/s
            v1y_akhir = float(entry_v1yakhir.get())                 # Menerima input berupa kecepatan akhir benda 1 di sumbu-Y dalam m/s
        
            m2 = float(entry_massa2.get())                          # Menerima input berupa massa benda 2 dalam kg
            v2x_awal = float(entry_v2xawal.get())                   # Menerima input berupa kecepatan awal benda 2 di sumbu-X dalam m/s
            v2y_awal = float(entry_v2yawal.get())                   # Menerima input berupa kecepatan awal benda 2 di sumbu-Y dalam m/s
            v2x_akhir = float(entry_v2xakhir.get())                 # Menerima input berupa kecepatan akhir benda 2 di sumbu-X dalam m/s
            v2y_akhir = float(entry_v2yakhir.get())                 # Menerima input berupa kecepatan akhir benda 2 di sumbu-Y dalam m/s
            
            if m1 <= 0 or m2 <= 0:
                # Memunculkan messagebox Error jika massa yang dimasukkan bernilai negatif
                messagebox.showerror('Error', 'Massa harus bernilai positif.',                  
                                     parent=jenistumbukan2dimensi)
                return
        
            if v1x_awal == 0 and v1y_awal == 0 and v2x_awal == 0 and v2y_awal == 0: 
                # Memunculkan messagebox Error jika kecepatan awal kedua benda di sumbu X dan Y bernilai nol
                messagebox.showerror('Error', 'Kedua benda diam dan tidak akan '
                                     'bertumbukan.', parent=jenistumbukan2dimensi)
                return
            
            if v1x_awal == v2x_awal and v1y_awal == v2y_awal:                                   
                # Memunculkan messagebox Error jika kecepatan awal kedua benda di sumbu X dan Y bernilai sama
                messagebox.showerror('Error', 'Kedua benda memiliki kecepatan '
                                     'awal yang sama dan tidak akan bertumbukan.', 
                                     parent=jenistumbukan2dimensi)
                return
        
            v1_awal = ((v1x_awal**2)+(v1y_awal**2))**(1/2)                                      # Rumus perhitungan untuk menentukan resultan vektor kecepatan awal benda 1
            v2_awal = ((v2x_awal**2)+(v2y_awal**2))**(1/2)                                      # Rumus perhitungan untuk menentukan resultan vektor kecepatan awal benda 2
            v1_akhir = ((v1x_akhir**2)+(v1y_akhir**2))**(1/2)                                   # Rumus perhitungan untuk menentukan resultan vektor kecepatan akhir benda 1
            v2_akhir = ((v2x_akhir**2)+(v2y_akhir**2))**(1/2)                                   # Rumus perhitungan untuk menentukan resultan vektor kecepatan akhir benda 2
            momentumx_awal = round(m1*v1x_awal+m2*v2x_awal, 3)                                  # Rumus perhitungan untuk menentukan momentum awal sistem di sumbu X
            momentumy_awal = round(m1*v1y_awal+m2*v2y_awal, 3)                                  # Rumus perhitungan untuk menentukan momentum awal sistem di sumbu Y
            momentumx_akhir = round(m1*v1x_akhir+m2*v2x_akhir, 3)                               # Rumus perhitungan untuk menentukan momentum akhir sistem di sumbu X
            momentumy_akhir = round(m1*v1y_akhir+m2*v2y_akhir, 3)                               # Rumus perhitungan untuk menentukan momentum akhir sistem di sumbu Y
            ek_awal = round((1/2)*m1*(v1_awal**2)+(1/2)*m2*(v2_awal**2), 3)                     # Rumus perhitungan untuk menentukan energi kinetik awal sistem
            ek_akhir = round((1/2)*m1*(v1_akhir**2)+(1/2)*m2*(v2_akhir**2), 3)                  # Rumus perhitungan untuk menentukan energi kinetik akhir sistem

        except ValueError:
            # Memunculkan messagebox Error jika input bukan merupakan bilangan real
            messagebox.showerror('Error', 'Masukkan bilangan real.',                            
                                 parent=jenistumbukan2dimensi)
            return
            
        except:
            # Memberikan pesan error jika terjadi error selain error yang telah didefinisikan sebelumnya
            messagebox.showerror('Error', 'Terjadi error.', parent=jenistumbukan2dimensi)              
            return

        if momentumx_awal != momentumx_akhir or momentumy_awal != momentumy_akhir:              
            # Ketika input tidak sesuai dengan Hukum Kekekalan Momentum, maka jenis tumbukan tidak dapat ditentukan
            messagebox.showwarning('Peringatan', 'Nilai yang anda masukkan tidak '              
                                   'sesuai dengan Hukum Kekekalan Momentum, '
                                   'sehingga jenis tumbukan tidak dapat ditentukan.', 
                                   parent=jenistumbukan2dimensi)
            text_jenistumbukan.config(state='normal')
            text_jenistumbukan.delete(1.0, 'end')
            text_jenistumbukan.insert(1.0, 'N/A')
            text_jenistumbukan.config(state='disabled')
            
        elif v1x_akhir == v2x_akhir and v1y_akhir == v2y_akhir:                                 
            # Memunculkan output jenis tumbukan 'inelastis sempurna' jika kecepatan akhir kedua benda di sumbu X dan Y bernilai sama
            text_jenistumbukan.config(state='normal')                                           
            text_jenistumbukan.delete(1.0, 'end')
            text_jenistumbukan.insert(1.0, 'inelastis sempurna')
            text_jenistumbukan.config(state='disabled')
        
        elif ek_awal == ek_akhir:                                                               
            # Memunculkan output jenis tumbukan 'elastis sempurna' jika energi kinetik awal dan akhir bernilai sama
            text_jenistumbukan.config(state='normal')                                           
            text_jenistumbukan.delete(1.0, 'end')
            text_jenistumbukan.insert(1.0, 'elastis sempurna')
            text_jenistumbukan.config(state='disabled')
    
        elif ek_awal > ek_akhir:                                                               
            # Memunculkan output jenis tumbukan 'elastis sebagian' jika energi kinetik awal lebih besar dari energi kinetik akhir
            text_jenistumbukan.config(state='normal')
            text_jenistumbukan.delete(1.0, 'end')
            text_jenistumbukan.insert(1.0, 'elastis sebagian')
            text_jenistumbukan.config(state='disabled')
       
        elif ek_awal < ek_akhir:                                                                
            # Memunculkan output jenis tumbukan 'superelastis' jika energi kinetik awal lebih kecil dari energi kinetik akhir
            text_jenistumbukan.config(state='normal')                                           
            text_jenistumbukan.delete(1.0, 'end')
            text_jenistumbukan.insert(1.0, 'superelastis')
            text_jenistumbukan.config(state='disabled')
       
        else:                                                                                   
            # Memunculkan output jenis tumbukan 'N/A' jika terjadi kasus diluar yang telah disebutkan
            text_jenistumbukan.config(state='normal')
            text_jenistumbukan.delete(1.0, 'end')
            text_jenistumbukan.insert(1.0, 'N/A')
            text_jenistumbukan.config(state='disabled')
            
        # Memunculkan output momentum awal di sumbu-X
        text_momentumxawal.config(state='normal')                                               
        text_momentumxawal.delete(1.0, 'end')
        text_momentumxawal.insert(1.0, f'{momentumx_awal}')
        text_momentumxawal.config(state='disabled')
        
        # Memunculkan output momentum awal di sumbu-Y
        text_momentumyawal.config(state='normal')                                              
        text_momentumyawal.delete(1.0, 'end')
        text_momentumyawal.insert(1.0, f'{momentumy_awal}')
        text_momentumyawal.config(state='disabled')
        
        # Memunculkan output momentum akhir di sumbu-X
        text_momentumxakhir.config(state='normal')                                              
        text_momentumxakhir.delete(1.0, 'end')
        text_momentumxakhir.insert(1.0, f'{momentumx_akhir}')
        text_momentumxakhir.config(state='disabled')
        
        # Memunculkan output momentum akhir di sumbu-Y
        text_momentumyakhir.config(state='normal')                                              
        text_momentumyakhir.delete(1.0, 'end')
        text_momentumyakhir.insert(1.0, f'{momentumy_akhir}')
        text_momentumyakhir.config(state='disabled')
        
        # Memunculkan output energi kinetik awal
        text_ekawal.config(state='normal')                                                      
        text_ekawal.delete(1.0, 'end')
        text_ekawal.insert(1.0, f'{ek_awal}')
        text_ekawal.config(state='disabled')
        
        # Memunculkan output energi kinetik akhir
        text_ekakhir.config(state='normal')                                                     
        text_ekakhir.delete(1.0, 'end')
        text_ekakhir.insert(1.0, f'{ek_akhir}')
        text_ekakhir.config(state='disabled')
        
# =============================================================================
# Algoritma Bagian Display
# Pada bagian ini, terdapat dua cabang sesuai dengan dimensi yang dipilih pengguna.
# Kedua cabang ini  berisi perintah-perintah tkinter untuk membuat display yang
# akan menerima input dan menampilkan output sesuai dengan dimensi yang dipilih.
# =============================================================================

    if pilihandimensi=='1 Dimensi': # Jika opsi yang dipilih adalah 1 dimensi
        
        # Set-up window dan menempatkannya di tengah layar
        jenistumbukan1dimensi = tk.Toplevel()
        jenistumbukan1dimensi.geometry("820x500")
        windowWidth = 820
        windowHeight = 500
        positionRight = int(jenistumbukan1dimensi.winfo_screenwidth()/2 - windowWidth/2)
        positionDown = int(jenistumbukan1dimensi.winfo_screenheight()/2.2 - windowHeight/2)
        jenistumbukan1dimensi.geometry("+{}+{}".format(positionRight, positionDown))
        jenistumbukan1dimensi.configure(bg = "#FFFFFF")
        jenistumbukan1dimensi.resizable(False, False)
        
        # Membuat canvas sebagai tempat bagi seluruh text dan rectangle
        canvasjenistumbukan1dimensi = Canvas(
            jenistumbukan1dimensi,
            bg = "#FFFFFF",
            height = 500,
            width = 820,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvasjenistumbukan1dimensi.place(x = 0, y = 0)
        
        # Membuat dua rectangle dan text sebagai header dan judul subprogram
        # menentukan jenis tumbukan satu dimensi
        canvasjenistumbukan1dimensi.create_rectangle(
            0.0,
            0.0,
            820.0,
            100.0,
            fill="#FCA311",
            outline="")
        
        canvasjenistumbukan1dimensi.create_text(
            23,
            10,
            anchor="nw",
            text="Menentukan\nJenis\nTumbukan",
            fill="#000000",
            font=("Montserrat Bold", 18 * -1))
        
        canvasjenistumbukan1dimensi.create_text(
            189.0,
            35.0,
            anchor="nw",
            text="1 Dimensi",
            fill="#000000",
            font=("Montserrat Bold", 18 * -1))
        
        canvasjenistumbukan1dimensi.create_rectangle(
            165.0,
            19.0,
            168.0,
            81.0,
            fill="#000000",
            outline="")
        
        # Membuat tiga rectangle sebagai frame untuk data benda 1, benda 2, 
        # dan hasil
        canvasjenistumbukan1dimensi.create_rectangle(
            20.0,
            123.0,
            400.0,
            213.0,
            fill="#E5E5E5",
            outline="")
        
        canvasjenistumbukan1dimensi.create_rectangle(
            122.0,
            305.0,
            698.0,
            471.0,
            fill="#E5E5E5",
            outline="")
        
        canvasjenistumbukan1dimensi.create_rectangle(
            421.0,
            123.0,
            801.0,
            213.0,
            fill="#E5E5E5",
            outline="")
        
        # Data Benda 1
        canvasjenistumbukan1dimensi.create_text(
            29.0,
            112.0,
            anchor="nw",
            text="Benda 1",
            fill="#000000",
            font=("Montserrat Medium", 16 * -1))
        
        # Membuat text untuk massa benda 1
        canvasjenistumbukan1dimensi.create_text(
            34.0,
            137.0,
            anchor="nw",
            text="Massa",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        canvasjenistumbukan1dimensi.create_text(
            234.0,
            137.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat entry untuk memasukkan input berupa massa benda 1
        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_jenistumbukan1dimensi_1.png"))
        entry_bg_1 = canvasjenistumbukan1dimensi.create_image(
            302.0,
            144.0,
            image=entry_image_1)
        
        entry_massa1 = Entry(
            jenistumbukan1dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        entry_massa1.place(
            x=252.0,
            y=134.0,
            width=100.0,
            height=18.0)
        
        # Membuat text untuk satuan massa (kg)
        canvasjenistumbukan1dimensi.create_text(
            370.0,
            137.0,
            anchor="nw",
            text="kg",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat text untuk kecepatan benda 1 sebelum tumbukan
        canvasjenistumbukan1dimensi.create_text(
            34.0,
            163.0,
            anchor="nw",
            text="Kecepatan sebelum tumbukan",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        canvasjenistumbukan1dimensi.create_text(
            234.0,
            163.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat entry untuk memasukkan input berupa kecepatan benda 1 
        # sebelum tumbukan
        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_jenistumbukan1dimensi_2.png"))
        entry_bg_2 = canvasjenistumbukan1dimensi.create_image(
            302.0,
            170.0,
            image=entry_image_2)
        
        entry_v1awal = Entry(
            jenistumbukan1dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        entry_v1awal.place(
            x=252.0,
            y=160.0,
            width=100.0,
            height=18.0)
        
        # Membuat text untuk satuan kecepatan (m/s)
        canvasjenistumbukan1dimensi.create_text(
            370.0,
            163.0,
            anchor="nw",
            text="m/s",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat text untuk kecepatan benda 1 setelah tumbukan
        canvasjenistumbukan1dimensi.create_text(
            34.0,
            189.0,
            anchor="nw",
            text="Kecepatan setelah tumbukan",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        canvasjenistumbukan1dimensi.create_text(
            234.0,
            189.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat entry untuk memasukkan input berupa kecepatan benda 1
        # setelah tumbukan
        entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_jenistumbukan1dimensi_3.png"))
        entry_bg_3 = canvasjenistumbukan1dimensi.create_image(
            302.0,
            196.0,
            image=entry_image_3)
        
        entry_v1akhir = Entry(
            jenistumbukan1dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        entry_v1akhir.place(
            x=252.0,
            y=186.0,
            width=100.0,
            height=18.0)
        
        # Membuat text untuk satuan kecepatan (m/s)
        canvasjenistumbukan1dimensi.create_text(
            370.0,
            189.0,
            anchor="nw",
            text="m/s",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Data Benda 2
        canvasjenistumbukan1dimensi.create_text(
            429.0,
            112.0,
            anchor="nw",
            text="Benda 2",
            fill="#000000",
            font=("Montserrat Medium", 16 * -1))
        
        # Membuat text untuk massa benda 2
        canvasjenistumbukan1dimensi.create_text(
            434.0,
            137.0,
            anchor="nw",
            text="Massa",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        canvasjenistumbukan1dimensi.create_text(
            634.0,
            137.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat entry untuk memasukkan input berupa massa benda 2
        entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_jenistumbukan1dimensi_4.png"))
        entry_bg_4 = canvasjenistumbukan1dimensi.create_image(
            706.0,
            144.0,
            image=entry_image_4)
        
        entry_massa2 = Entry(
            jenistumbukan1dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        entry_massa2.place(
            x=656.0,
            y=134.0,
            width=100.0,
            height=18.0)
        
        # Membuat text untuk satuan massa (kg)
        canvasjenistumbukan1dimensi.create_text(
            772.0,
            137.0,
            anchor="nw",
            text="kg",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat text untuk kecepatan benda 2 sebelum tumbukan
        canvasjenistumbukan1dimensi.create_text(
            434.0,
            163.0,
            anchor="nw",
            text="Kecepatan sebelum tumbukan",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        canvasjenistumbukan1dimensi.create_text(
            634.0,
            163.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat entry untuk memasukkan input berupa kecepatan benda 2 
        # sebelum tumbukan
        entry_image_5 = PhotoImage(
            file=relative_to_assets("entry_jenistumbukan1dimensi_5.png"))
        entry_bg_5 = canvasjenistumbukan1dimensi.create_image(
            706.0,
            170.0,
            image=entry_image_5)
        
        entry_v2awal = Entry(
            jenistumbukan1dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        entry_v2awal.place(
            x=656.0,
            y=160.0,
            width=100.0,
            height=18.0)
        
        # Membuat text untuk satuan kecepatan (m/s)
        canvasjenistumbukan1dimensi.create_text(
            772.0,
            163.0,
            anchor="nw",
            text="m/s",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat text untuk kecepatan benda 2 setelah tumbukan
        canvasjenistumbukan1dimensi.create_text(
            434.0,
            189.0,
            anchor="nw",
            text="Kecepatan setelah tumbukan",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        canvasjenistumbukan1dimensi.create_text(
            634.0,
            189.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat entry untuk memasukkan input berupa kecepatan benda 2 
        # setelah tumbukan
        entry_image_6 = PhotoImage(
            file=relative_to_assets("entry_jenistumbukan1dimensi_6.png"))
        entry_bg_6 = canvasjenistumbukan1dimensi.create_image(
            706.0,
            196.0,
            image=entry_image_6)
        
        entry_v2akhir = Entry(
            jenistumbukan1dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        
        entry_v2akhir.place(
            x=656.0,
            y=186.0,
            width=100.0,
            height=18.0)
        
        # Membuat text untuk satuan kecepatan (m/s)
        canvasjenistumbukan1dimensi.create_text(
            772.0,
            189.0,
            anchor="nw",
            text="m/s",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat text untuk catatan keakuratan
        canvasjenistumbukan1dimensi.create_text(
            249.0,
            218.0,
            anchor="nw",
            text="Catatan: Untuk hasil yang akurat, masukkan 4 angka di belakang koma ",
            fill="#000000",
            font=("Montserrat Regular", 9 * -1))
        
        # Membuat button Jalankan Program! yang bila ditekan akan menjalankan
        # perhitungan
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_jenistumbukan1dimensi.png"))
        button_jenistumbukan1dimensi = Button(
            jenistumbukan1dimensi,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: jenistumbukan_satudimensi(),
            relief="flat")
        button_jenistumbukan1dimensi.place(
            x=313.0,
            y=244.0,
            width=195.0,
            height=41.0)
        
        # Data Hasil
        canvasjenistumbukan1dimensi.create_text(
            135.0,
            293.0,
            anchor="nw",
            text="Hasil",
            fill="#000000",
            font=("Montserrat Medium", 16 * -1))
        
        # Membuat text untuk besar momentum sistem sebelum tumbukan
        canvasjenistumbukan1dimensi.create_text(
            139.0,
            318.0,
            anchor="nw",
            text="Besar momentum sistem sebelum tumbukan",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        canvasjenistumbukan1dimensi.create_text(
            441.0,
            318.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat TextArea untuk menampilkan output berupa besar momentum sebelum
        # tumbukan
        entry_image_7 = PhotoImage(
            file=relative_to_assets("text_jenistumbukan1dimensi_7.png"))
        entry_bg_7 = canvasjenistumbukan1dimensi.create_image(
            543.0,
            324.0,
            image=entry_image_7)
        
        text_momentumawal = Text(
            jenistumbukan1dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        text_momentumawal.place(
            x=463.0,
            y=314.0,
            width=160.0,
            height=18.0)
        text_momentumawal.config(
            state='disabled')
        
        # Membuat text untuk satuan momentum (kg . m/s)
        canvasjenistumbukan1dimensi.create_text(
            642.0,
            317.0,
            anchor="nw",
            text="kg . m/s",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat text untuk besar momentum sistem setelah tumbukan
        canvasjenistumbukan1dimensi.create_text(
            139.0,
            344.0,
            anchor="nw",
            text="Besar momentum sistem setelah tumbukan",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        canvasjenistumbukan1dimensi.create_text(
            441.0,
            344.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat TextArea untuk menampilkan output berupa besar momentum sistem
        # setelah tumbukan
        entry_image_8 = PhotoImage(
            file=relative_to_assets("text_jenistumbukan1dimensi_8.png"))
        entry_bg_8 = canvasjenistumbukan1dimensi.create_image(
            543.0,
            350.0,
            image=entry_image_8)
        
        text_momentumakhir = Text(
            jenistumbukan1dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        text_momentumakhir.place(
            x=463.0,
            y=340.0,
            width=160.0,
            height=18.0)
        text_momentumakhir.config(
            state='disabled')
        
        # Membuat text untuk satuan momentum (kg . m/s)
        canvasjenistumbukan1dimensi.create_text(
            642.0,
            343.0,
            anchor="nw",
            text="kg . m/s",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat text untuk besar energi kinetik sistem sebelum tumbukan
        canvasjenistumbukan1dimensi.create_text(
            139.0,
            370.0,
            anchor="nw",
            text="Besar energi kinetik sistem sebelum tumbukan",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        canvasjenistumbukan1dimensi.create_text(
            441.0,
            370.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat TextArea yang akan menampilkan output berupa besar energi
        # kinetik sistem sebelum tumbukan
        entry_image_9 = PhotoImage(
            file=relative_to_assets("text_jenistumbukan1dimensi_9.png"))
        entry_bg_9 = canvasjenistumbukan1dimensi.create_image(
            543.0,
            376.0,
            image=entry_image_9)
        
        text_ekawal = Text(
            jenistumbukan1dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        text_ekawal.place(
            x=463.0,
            y=366.0,
            width=160.0,
            height=18.0)
        text_ekawal.config(
            state='disabled')
        
        # Membuat text untuk satuan energi kinetik (J)
        canvasjenistumbukan1dimensi.create_text(
            642.0,
            369.0,
            anchor="nw",
            text="J",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat text untuk besar energi kinetik sistem setelah tumbukan
        canvasjenistumbukan1dimensi.create_text(
            139.0,
            396.0,
            anchor="nw",
            text="Besar energi kinetik sistem setelah tumbukan",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        canvasjenistumbukan1dimensi.create_text(
            441.0,
            396.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat TextArea untuk menampilkan output berupa besar energi kinetik
        # sistem setelah tumbukan
        entry_image_10 = PhotoImage(
            file=relative_to_assets("text_jenistumbukan1dimensi_10.png"))
        entry_bg_10 = canvasjenistumbukan1dimensi.create_image(
            543.0,
            402.0,
            image=entry_image_10)
        
        text_ekakhir = Text(
            jenistumbukan1dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        text_ekakhir.place(
            x=463.0,
            y=392.0,
            width=160.0,
            height=18.0)
        text_ekakhir.config(
            state='disabled')
        
        # Membuat text untuk satuan energi kinetik (J)
        canvasjenistumbukan1dimensi.create_text(
            642.0,
            395.0,
            anchor="nw",
            text="J",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat text untuk nilai koefisien restitusi
        canvasjenistumbukan1dimensi.create_text(
            139.0,
            422.0,
            anchor="nw",
            text="Nilai koefisien restitusi",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        canvasjenistumbukan1dimensi.create_text(
            441.0,
            422.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat TextArea untuk menampilkan output berupa nilai koefisien
        # restitusi
        entry_image_11 = PhotoImage(
            file=relative_to_assets("text_jenistumbukan1dimensi_11.png"))
        entry_bg_11 = canvasjenistumbukan1dimensi.create_image(
            543.0,
            428.0,
            image=entry_image_11)
        
        text_restitusi = Text(
            jenistumbukan1dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        text_restitusi.place(
            x=463.0,
            y=418.0,
            width=160.0,
            height=18.0)
        text_restitusi.config(
            state='disabled')
        
        # Membuat text untuk jenis tumbukan
        canvasjenistumbukan1dimensi.create_text(
            139.0,
            448.0,
            anchor="nw",
            text="Jenis tumbukan",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        canvasjenistumbukan1dimensi.create_text(
            441.0,
            448.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat TextArea untuk manmpilkan output berupa jenis tumbukan yang
        # terjadi
        entry_image_12 = PhotoImage(
            file=relative_to_assets("text_jenistumbukan1dimensi_12.png"))
        entry_bg_12 = canvasjenistumbukan1dimensi.create_image(
            543.0,
            454.0,
            image=entry_image_12)
        
        text_jenistumbukan = Text(
            jenistumbukan1dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        text_jenistumbukan.place(
            x=463.0,
            y=444.0,
            width=160.0,
            height=18.0)
        text_jenistumbukan.config(
            state='disabled')
        
        # Membuat text untuk catatan pembulatan
        canvasjenistumbukan1dimensi.create_text(
            275.0,
            478.0,
            anchor="nw",
            text="Catatan: Hasil dibulatkan hingga 3 angka di belakang koma ",
            fill="#000000",
            font=("Montserrat Regular", 9 * -1))
        
        # Menjalankan aplikasi agar tetap berjalan sebelum di-close
        jenistumbukan1dimensi.mainloop()

    
    elif pilihandimensi =='2 Dimensi': # Jika opsi yang dipilih adalah 2 dimensi

        # Set-up window dan menempatkannya di tengah layar
        jenistumbukan2dimensi = tk.Toplevel()
        jenistumbukan2dimensi.geometry("1200x500")
        windowWidth = 1200
        windowHeight = 500
        positionRight = int(jenistumbukan2dimensi.winfo_screenwidth()/2 - windowWidth/2)
        positionDown = int(jenistumbukan2dimensi.winfo_screenheight()/2.2 - windowHeight/2)
        jenistumbukan2dimensi.geometry("+{}+{}".format(positionRight, positionDown))
        jenistumbukan2dimensi.configure(bg = "#FFFFFF")
        jenistumbukan2dimensi.resizable(False, False)
        
        # Membuat canvas sebagai tempat bagi seluruh text dan rectangle
        canvasjenistumbukan2dimensi = Canvas(
            jenistumbukan2dimensi,
            bg = "#FFFFFF",
            height = 500,
            width = 1200,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvasjenistumbukan2dimensi.place(x = 0, y = 0)
        
        # Membuat dua rectangle dan text sebagai header dan judul subprogram
        # menentukan jenis tumbukan satu dimensi
        canvasjenistumbukan2dimensi.create_rectangle(
            0.0,
            0.0,
            1200.0,
            100.0,
            fill="#FCA311",
            outline="")
        
        canvasjenistumbukan2dimensi.create_text(
            23,
            10.0,
            anchor="nw",
            text="Menentukan\nJenis\nTumbukan",
            fill="#000000",
            font=("Montserrat Bold", 18 * -1))
        
        canvasjenistumbukan2dimensi.create_text(
            189.0,
            35.0,
            anchor="nw",
            text="2 Dimensi",
            fill="#000000",
            font=("Montserrat Bold", 18 * -1))
        
        canvasjenistumbukan2dimensi.create_rectangle(
            165.0,
            19.0,
            168.0,
            81.0,
            fill="#000000",
            outline="")
        
        # Membuat tiga rectangle sebagai frame untuk data benda 1, benda 2, 
        # dan hasil
        canvasjenistumbukan2dimensi.create_rectangle(
            35.0,
            123.0,
            585.0,
            213.0,
            fill="#E5E5E5",
            outline="")
        
        canvasjenistumbukan2dimensi.create_rectangle(
            202.0,
            305.0,
            999.0,
            449.0,
            fill="#E5E5E5",
            outline="")
        
        canvasjenistumbukan2dimensi.create_rectangle(
            615.0,
            123.0,
            1165.0,
            213.0,
            fill="#E5E5E5",
            outline="")
        
        # Data Benda 1
        canvasjenistumbukan2dimensi.create_text(
            44.0,
            112.0,
            anchor="nw",
            text="Benda 1",
            fill="#000000",
            font=("Montserrat Medium", 16 * -1))
        
        # Membuat text untuk massa benda 1
        canvasjenistumbukan2dimensi.create_text(
            49.0,
            137.0,
            anchor="nw",
            text="Massa",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        canvasjenistumbukan2dimensi.create_text(
            249.0,
            137.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat entry untuk memasukkan input berupa massa benda 1
        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_jenistumbukan2dimensi_1.png"))
        entry_bg_1 = canvasjenistumbukan2dimensi.create_image(
            317.0,
            144.0,
            image=entry_image_1)
        
        entry_massa1 = Entry(
            jenistumbukan2dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        entry_massa1.place(
            x=267.0,
            y=134.0,
            width=100.0,
            height=18.0)
        
        # Membuat text untuk satuan massa (kg)
        canvasjenistumbukan2dimensi.create_text(
            384.0,
            137.0,
            anchor="nw",
            text="kg",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat text untuk kecepatan benda 1 sebelum tumbukan
        canvasjenistumbukan2dimensi.create_text(
            49.0,
            163.0,
            anchor="nw",
            text="Kecepatan sebelum tumbukan",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        canvasjenistumbukan2dimensi.create_text(
            249.0,
            163.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat entry untuk memasukkan input berupa komponen sumbu x dari
        # kecepatan benda 1 sebelum tumbukan
        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_jenistumbukan2dimensi_2.png"))
        entry_bg_2 = canvasjenistumbukan2dimensi.create_image(
            317.0,
            170.0,
            image=entry_image_2)
        
        entry_v1xawal = Entry(
            jenistumbukan2dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        entry_v1xawal.place(
            x=267.0,
            y=160.0,
            width=100.0,
            height=18.0)
        
        # Membuat text untuk unit vektor sumbu x (i)
        canvasjenistumbukan2dimensi.create_text(
            384.0,
            163.0,
            anchor="nw",
            text="i  +",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat entry untuk memasukkan input berupa komponen sumbu y dari
        # kecepatan benda 1 sebelum tumbukan
        entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_jenistumbukan2dimensi_3.png"))
        entry_bg_3 = canvasjenistumbukan2dimensi.create_image(
            468.0,
            170.0,
            image=entry_image_3)
        
        entry_v1yawal = Entry(
            jenistumbukan2dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        entry_v1yawal.place(
            x=418.0,
            y=160.0,
            width=100.0,
            height=18.0)
        
        # Membuat text untuk unit vektor sumbu y (j) dan satuan kecepatan (m/s)
        canvasjenistumbukan2dimensi.create_text(
            538.0,
            163.0,
            anchor="nw",
            text="j   m/s",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat text untuk kecepatan benda 1 setelah tumbukan
        canvasjenistumbukan2dimensi.create_text(
            49.0,
            189.0,
            anchor="nw",
            text="Kecepatan setelah tumbukan",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        canvasjenistumbukan2dimensi.create_text(
            249.0,
            189.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat entry untuk memasukkan input berupa komponen sumbu x dari
        # kecepatan benda 1 setelah tumbukan
        entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_jenistumbukan2dimensi_4.png"))
        entry_bg_4 = canvasjenistumbukan2dimensi.create_image(
            317.0,
            196.0,
            image=entry_image_4)
        
        entry_v1xakhir = Entry(
            jenistumbukan2dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        entry_v1xakhir.place(
            x=267.0,
            y=186.0,
            width=100.0,
            height=18.0)
        
        # Membuat text untuk unit vektor sumbu x (i)
        canvasjenistumbukan2dimensi.create_text(
            384.0,
            186.0,
            anchor="nw",
            text="i  +",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat entry untuk memasukkan input berupa komponen sumbu y dari
        # kecepatan benda 1 setelah tumbukan
        entry_image_5 = PhotoImage(
            file=relative_to_assets("entry_jenistumbukan2dimensi_5.png"))
        entry_bg_5 = canvasjenistumbukan2dimensi.create_image(
            468.0,
            196.0,
            image=entry_image_5)
        
        entry_v1yakhir = Entry(
            jenistumbukan2dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        entry_v1yakhir.place(
            x=418.0,
            y=186.0,
            width=100.0,
            height=18.0)
        
        # Membuat text untuk unit vektor sumbu y (j) dan satuan kecepatan (m/s)
        canvasjenistumbukan2dimensi.create_text(
            538.0,
            189.0,
            anchor="nw",
            text="j   m/s",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Data Benda 2
        canvasjenistumbukan2dimensi.create_text(
            623.0,
            112.0,
            anchor="nw",
            text="Benda 2",
            fill="#000000",
            font=("Montserrat Medium", 16 * -1))
        
        # Membuat text untuk massa benda 2
        canvasjenistumbukan2dimensi.create_text(
            628.0,
            137.0,
            anchor="nw",
            text="Massa",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        canvasjenistumbukan2dimensi.create_text(
            828.0,
            137.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat entry untuk memasukkan input berupa massa benda 2
        entry_image_6 = PhotoImage(
            file=relative_to_assets("entry_jenistumbukan2dimensi_6.png"))
        entry_bg_6 = canvasjenistumbukan2dimensi.create_image(
            900.0,
            144.0,
            image=entry_image_6)
        
        entry_massa2 = Entry(
            jenistumbukan2dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        entry_massa2.place(
            x=850.0,
            y=134.0,
            width=100.0,
            height=18.0)
        
        # Membuat text untuk satuan massa (kg)
        canvasjenistumbukan2dimensi.create_text(
            965.0,
            137.0,
            anchor="nw",
            text="kg",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat text untuk kecepatan benda 2 sebelum tumbukan
        canvasjenistumbukan2dimensi.create_text(
            628.0,
            163.0,
            anchor="nw",
            text="Kecepatan sebelum tumbukan",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        canvasjenistumbukan2dimensi.create_text(
            828.0,
            163.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat entry untuk memasukkan input berupa komponen sumbu x dari
        # kecepatan benda 2 sebelum tumbukan
        entry_image_7 = PhotoImage(
            file=relative_to_assets("entry_jenistumbukan2dimensi_7.png"))
        entry_bg_7 = canvasjenistumbukan2dimensi.create_image(
            900.0,
            170.0,
            image=entry_image_7)
        
        entry_v2xawal = Entry(
            jenistumbukan2dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        entry_v2xawal.place(
            x=850.0,
            y=160.0,
            width=100.0,
            height=18.0)
        
        # Membuat text untuk unit vektor sumbu x (i)
        canvasjenistumbukan2dimensi.create_text(
            965.0,
            163.0,
            anchor="nw",
            text="i  +",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat entry untuk memasukkan input berupa komponen sumbu y dari
        # kecepatan benda 2 sebelum tumbukan
        entry_image_8 = PhotoImage(
            file=relative_to_assets("entry_jenistumbukan2dimensi_8.png"))
        entry_bg_8 = canvasjenistumbukan2dimensi.create_image(
            1051.0,
            170.0,
            image=entry_image_8)
        
        entry_v2yawal = Entry(
            jenistumbukan2dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        entry_v2yawal.place(
            x=1001.0,
            y=160.0,
            width=100.0,
            height=18.0)
        
        # Membuat text untuk unit vektor sumbu y (j) dan satuan kecepatan (m/s)
        canvasjenistumbukan2dimensi.create_text(
            1119.0,
            163.0,
            anchor="nw",
            text="j   m/s",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat text untuk kecepatan benda 2 setelah tumbukan
        canvasjenistumbukan2dimensi.create_text(
            628.0,
            189.0,
            anchor="nw",
            text="Kecepatan setelah tumbukan",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        canvasjenistumbukan2dimensi.create_text(
            828.0,
            189.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat entry untuk memasukkan input berupa komponen sumbu x dari
        # kecepatan benda 2 setelah tumbukan
        entry_image_9 = PhotoImage(
            file=relative_to_assets("entry_jenistumbukan2dimensi_9.png"))
        entry_bg_9 = canvasjenistumbukan2dimensi.create_image(
            900.0,
            196.0,
            image=entry_image_9)
        
        entry_v2xakhir = Entry(
            jenistumbukan2dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        entry_v2xakhir.place(
            x=850.0,
            y=186.0,
            width=100.0,
            height=18.0)
        
        # Membuat text untuk unit vektor sumbu x (i)
        canvasjenistumbukan2dimensi.create_text(
            965.0,
            186.0,
            anchor="nw",
            text="i  +",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat entry untuk memasukkan input berupa komponen sumbu y dari
        # kecepatan benda 2 setelah tumbukan
        entry_image_10 = PhotoImage(
            file=relative_to_assets("entry_jenistumbukan2dimensi_10.png"))
        entry_bg_10 = canvasjenistumbukan2dimensi.create_image(
            1051.0,
            196.0,
            image=entry_image_10)
        
        entry_v2yakhir = Entry(
            jenistumbukan2dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        entry_v2yakhir.place(
            x=1001.0,
            y=186.0,
            width=100.0,
            height=18.0)
        
        # Membuat text untuk unit vektor sumbu y (j) dan satuan kecepatan (m/s)
        canvasjenistumbukan2dimensi.create_text(
            1119.0,
            189.0,
            anchor="nw",
            text="j   m/s",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat text untuk catatan keakuratan
        canvasjenistumbukan2dimensi.create_text(
            439.0,
            218.0,
            anchor="nw",
            text="Catatan: Untuk hasil yang akurat, masukkan 4 angka di belakang koma ",
            fill="#000000",
            font=("Montserrat Regular", 9 * -1))
        
        # Membuat button Jalankan Program! yang bila ditekan akan menjalankan
        # perhitungan
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_jenistumbukan2dimensi.png"))
        button_jenistumbukan2dimensi = Button(
            jenistumbukan2dimensi,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: jenistumbukan_duadimensi(),
            relief="flat")
        button_jenistumbukan2dimensi.place(
            x=503.0,
            y=244.0,
            width=195.0,
            height=41.0)
        
        # Data Hasil
        canvasjenistumbukan2dimensi.create_text(
            215.0,
            293.0,
            anchor="nw",
            text="Hasil",
            fill="#000000",
            font=("Montserrat Medium", 16 * -1))
        
        # Membuat text untuk besar momentum sistem sebelum tumbukan
        canvasjenistumbukan2dimensi.create_text(
            219.0,
            318.0,
            anchor="nw",
            text="Besar momentum sistem sebelum tumbukan",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        canvasjenistumbukan2dimensi.create_text(
            521.0,
            318.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat TextArea untuk menampilkan output berupa komponen sumbu x 
        # dari momentum sistem sebelum tumbukan
        entry_image_11 = PhotoImage(
            file=relative_to_assets("text_jenistumbukan2dimensi_11.png"))
        entry_bg_11 = canvasjenistumbukan2dimensi.create_image(
            623.0,
            324.0,
            image=entry_image_11)
        
        text_momentumxawal = Text(
            jenistumbukan2dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        text_momentumxawal.place(
            x=543.0,
            y=314.0,
            width=160.0,
            height=18.0)
        text_momentumxawal.config(
            state='disabled')
        
        # Membuat text untuk unit vektor sumbu x (i)
        canvasjenistumbukan2dimensi.create_text(
            719.0,
            317.0,
            anchor="nw",
            text="i  +",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat TextArea untuk menampilkan output berupa komponen sumbu y 
        # dari momentum sistem sebelum tumbukan
        entry_image_12 = PhotoImage(
            file=relative_to_assets("text_jenistumbukan2dimensi_12.png"))
        entry_bg_12 = canvasjenistumbukan2dimensi.create_image(
            833.0,
            324.0,
            image=entry_image_12)
        
        text_momentumyawal = Text(
            jenistumbukan2dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        text_momentumyawal.place(
            x=753.0,
            y=314.0,
            width=160.0,
            height=18.0)
        text_momentumyawal.config(
            state='disabled')
        
        # Membuat text untuk unit vektor sumbu y (j) dan satuan kecepatan (m/s)
        canvasjenistumbukan2dimensi.create_text(
            931.0,
            317.0,
            anchor="nw",
            text="j   kg . m/s",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat text untuk besar momentum sistem setelah tumbukan
        canvasjenistumbukan2dimensi.create_text(
            219.0,
            344.0,
            anchor="nw",
            text="Besar momentum sistem setelah tumbukan",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        canvasjenistumbukan2dimensi.create_text(
            521.0,
            344.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat TextArea untuk menampilkan output berupa komponen sumbu x 
        # dari momentum sistem setelah tumbukan
        entry_image_13 = PhotoImage(
            file=relative_to_assets("text_jenistumbukan2dimensi_13.png"))
        entry_bg_13 = canvasjenistumbukan2dimensi.create_image(
            623.0,
            350.0,
            image=entry_image_13)
        
        text_momentumxakhir = Text(
            jenistumbukan2dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        text_momentumxakhir.place(
            x=543.0,
            y=340.0,
            width=160.0,
            height=18.0)
        text_momentumxakhir.config(
            state='disabled')
        
        # Membuat text untuk unit vektor sumbu x (i)
        canvasjenistumbukan2dimensi.create_text(
            719.0,
            342.0,
            anchor="nw",
            text="i  +",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat TextArea untuk menampilkan output berupa komponen sumbu y 
        # dari momentum sistem setelah
        entry_image_14 = PhotoImage(
            file=relative_to_assets("text_jenistumbukan2dimensi_14.png"))
        entry_bg_14 = canvasjenistumbukan2dimensi.create_image(
            833.0,
            350.0,
            image=entry_image_14)
       
        text_momentumyakhir = Text(
            jenistumbukan2dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        text_momentumyakhir.place(
            x=753.0,
            y=340.0,
            width=160.0,
            height=18.0)
        text_momentumyakhir.config(
            state='disabled')
        
        # Membuat text untuk unit vektor sumbu y(j) dan satuan kecepatan (m/s)
        canvasjenistumbukan2dimensi.create_text(
            931.0,
            342.0,
            anchor="nw",
            text="j   kg . m/s",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat text untuk besar energi kinetik sistem sebelum tumbukan
        canvasjenistumbukan2dimensi.create_text(
            219.0,
            370.0,
            anchor="nw",
            text="Besar energi kinetik sistem sebelum tumbukan",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        canvasjenistumbukan2dimensi.create_text(
            521.0,
            370.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat TextArea untuk menampilkan output berupa besar energi
        # kinetik sistem sebelum tumbukan
        entry_image_15 = PhotoImage(
            file=relative_to_assets("text_jenistumbukan2dimensi_15.png"))
        entry_bg_15 = canvasjenistumbukan2dimensi.create_image(
            623.0,
            376.0,
            image=entry_image_15)
        
        text_ekawal = Text(
            jenistumbukan2dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        text_ekawal.place(
            x=543.0,
            y=366.0,
            width=160.0,
            height=18.0)
        text_ekawal.config(
            state='disabled')
        
        # Membuat text untuk satuan energi kinetik (J)
        canvasjenistumbukan2dimensi.create_text(
            719.0,
            369.0,
            anchor="nw",
            text="J",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat text untuk besar energi kinetik sistem setelah tumbukan
        canvasjenistumbukan2dimensi.create_text(
            219.0,
            396.0,
            anchor="nw",
            text="Besar energi kinetik sistem setelah tumbukan",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        canvasjenistumbukan2dimensi.create_text(
            521.0,
            396.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat TextArea untuk menampilkan output berupa besar energi
        # kinetik sistem setelah tumbukan
        entry_image_16 = PhotoImage(
            file=relative_to_assets("text_jenistumbukan2dimensi_16.png"))
        entry_bg_16 = canvasjenistumbukan2dimensi.create_image(
            623.0,
            402.0,
            image=entry_image_16)
        
        text_ekakhir = Text(
            jenistumbukan2dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        text_ekakhir.place(
            x=543.0,
            y=392.0,
            width=160.0,
            height=18.0)
        text_ekakhir.config(
            state='disabled')
        
        # Membuat text untuk satuan energi kinetik (J)
        canvasjenistumbukan2dimensi.create_text(
            719.0,
            395.0,
            anchor="nw",
            text="J",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat text untuk jenis tumbukan
        canvasjenistumbukan2dimensi.create_text(
            219.0,
            422.0,
            anchor="nw",
            text="Jenis tumbukan",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        canvasjenistumbukan2dimensi.create_text(
            521.0,
            422.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat TextArea untuk menampilkan output berupa jenis tumbukan
        entry_image_17 = PhotoImage(
            file=relative_to_assets("text_jenistumbukan2dimensi_17.png"))
        entry_bg_17 = canvasjenistumbukan2dimensi.create_image(
            623.0,
            428.0,
            image=entry_image_17)
        text_jenistumbukan = Text(
            jenistumbukan2dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        text_jenistumbukan.place(
            x=543.0,
            y=418.0,
            width=160.0,
            height=18.0)
        text_jenistumbukan.config(
            state='disabled')
        
        # Membuat text untuk catatan pembulatan
        canvasjenistumbukan2dimensi.create_text(
            465.0,
            461.0,
            anchor="nw",
            text="Catatan: Hasil dibulatkan hingga 3 angka di belakang koma ",
            fill="#000000",
            font=("Montserrat Regular", 9 * -1))
        
        # Menjalankan aplikasi agar tetap berjalan sebelum di-close
        jenistumbukan2dimensi.mainloop()
