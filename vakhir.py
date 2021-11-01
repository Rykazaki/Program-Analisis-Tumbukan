# Tugas Besar Kelompok 3
# PROGRAM    : Subprogram Menentukan Kecepatan Akhir
# DESKRIPSI  : Program yang dapat menentukan kecepatan akhir dalam 1 dimensi 
#              & 2 dimensi berdasarkan data yang diinput oleh pengguna.

# CREDIT
# Pembuatan GUI dibantu dengan modul Tkinter Designer karya Parth Jadhav

# KAMUS LOKAL
# pilihandimensi        : string, nilai dari dimensi yang dipilih
# m1                    : float, nilai dari massa benda 1 
# v1_awal               : float, nilai dari kecepatan benda 1 sebelum tumbukan     
# v1x_awal              : float, nilai komponen sumbu x dari kecepatan benda 1 sebelum tumbukan
# v1y_awal              : float, nilai komponen sumbu y dari kecepatan benda 1 sebelum tumbukan
# v1_akhir              : float, nilai dari kecepatan benda 1 setelah tumbukan     
# v1x_akhir             : float, nilai komponen sumbu x dari kecepatan benda 1 setelah tumbukan
# v1y_akhir             : float, nilai komponen sumbu y dari kecepatan benda 1 setelah tumbukan
# m2                    : float, nilai dari massa benda 2 
# v2_awal               : float, nilai dari kecepatan benda 2 sebelum tumbukan     
# v2x_awal              : float, nilai komponen sumbu x dari kecepatan benda 2 sebelum tumbukan
# v2y_awal              : float, nilai komponen sumbu y dari kecepatan benda 2 sebelum tumbukan
# v2_akhir              : float, nilai dari kecepatan benda 2 setelah tumbukan     
# v2x_akhir             : float, nilai komponen sumbu x dari kecepatan benda 2 setelah tumbukan
# v2y_akhir             : float, nilai komponen sumbu y dari kecepatan benda 2 setelah tumbukan
# momentum_awal         : float, nilai dari momentum sistem sebelum tumbukan
# momentumx_awal        : float, nilai komponen sumbu x dari momentum sistem sebelum tumbukan
# momentumy_awal        : float, nilai komponen sumbu y dari momentum sistem sebelum tumbukan
# momentum_akhir        : float, nilai dari momentum sistem setelah tumbukan
# momentumx_akhir       : float, nilai komponen sumbu x dari momentum sistem setelah tumbukan
# momentumy_akhir       : float, nilai komponen sumbu y dari momentum sistem setelah tumbukan
# restitusi             : float, nilai koefisien restitusi dari tumbukan
# ek_awal               : float, nilai energi kinetik sistem sebelum tumbukan
# ek_akhir              : float, nilai energi kinetik sistem setelah tumbukan
# benda                 : array, berisi benda yang dapat dipilih untuk data kecepatan akhir
# nilai_pilihanbenda    : string, nilai dari benda yang dipilih untuk data kecepatan akhir



# ALGORITMA

# Import modul tkinter yang dibutuhkan
import tkinter as tk
from tkinter import ttk, Canvas, Entry, Text, Button, PhotoImage, messagebox

# Import pathlib untuk mengakses gambar dalam folder assets
from pathlib import Path     

# Inisialisasi path untuk mengakses folder assets yang berisi gambar  
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")
        
# Definisi fungsi relative_to_assets untuk mengakses path       
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
        
def program_vakhir(pilihandimensi): # Mendefinisikan program untuk menentukan kecepatan akhir

# =============================================================================
# Algoritma Bagian Pemrosesan Data
# Pada bagian ini, terdapat dua fungsi, yaitu vakhir_satudimensi dan vakhir_duadimensi 
# yang berguna untuk memproses input dan menampilkan output pada display.
# =============================================================================
    
    def vakhir_satudimensi():  # Mendefinisikan program untuk menentukan kecepatan dalam 1 dimensi
        try:
            m1 = float(entry_massa1.get())              # Input data berupa massa benda 1 dalam satuan kilogram
            v1_awal = float(entry_v1awal.get())         # Input data berupa kecepatan awal massa benda 1 dalam satuan meter per sekon
            
            m2 = float(entry_massa2.get())              # Input data berupa massa benda 2 dalam satuan kilogram
            v2_awal = float(entry_v2awal.get())         # Input data berupa kecepatan awal massa benda 1 dalam satuan meter per sekon
            
            restitusi = float(entry_restitusi.get())    # Input data berupa besar konstanta restitusi pada tumbukan

            if m1 < 0 or m2 < 0:
                # Memberikan pesan error jika input data massa benda 1 atau/dan massa benda 2 bernilai negatif
                messagebox.showerror('Error', 'Massa tidak boleh negatif',
                                     parent=vakhir1dimensi)
                return

            if v1_awal == 0 and v2_awal == 0:
                # Memberikan pesan error jika input data kecepatan awal benda 1 dan kecepatan awal benda 2 bernilai nol, maka tidak memungkinkan kedua benda bertumbukan
                messagebox.showerror('Error', 'Kedua benda diam dan tidak akan '    
                                     'bertumbukan', parent=vakhir1dimensi)
                return
            
            if v1_awal == v2_awal:
                # Memberikan pesan error jika input data kecepatan awal benda 1 dan kecepatan awal benda 2 bernilai sama besar, maka tidak memungkinkan kedua benda bertumbukan
                messagebox.showerror('Error', 'Kedua benda memiliki kecepatan '     
                                     'awal yang sama dan tidak akan bertumbukan.', 
                                     parent=vakhir1dimensi)
                return
            
            if restitusi < 0:
                # Memberikan pesan error jika input data nilai konstanta restitusi bernilai negatif karena nilai konstanta koefisien restitusi mungkin bernilai negatif
                messagebox.showerror('Error', 'Nilai koefisien restitusi tidak '    
                                     'boleh negatif.', parent=vakhir1dimensi)
                return

            v1_akhir = round((m1*v1_awal+m2*v2_awal+m2*restitusi*(v2_awal-v1_awal))/(m1+m2), 3) # Perhitungan (rumus) mencari nilai kecepatan akhir benda 1 dan pembulatannya sebanyak 3 angka
            v2_akhir = round((m1*v1_awal+m2*v2_awal+m1*restitusi*(v1_awal-v2_awal))/(m1+m2),3)  # Perhitungan (rumus) mencari nilai kecepatan akhir benda 2 dan pembulatannya sebanyak 3 angka
            momentum = round(m1*v1_awal+m2*v2_awal, 3)                                          # Perhitungan (rumus) mencari nilai momentum dan pembulatannya sebanyak 3 angka
            ek_awal = round((1/2)*m1*(v1_awal**2)+(1/2)*m2*(v2_awal**2), 3)                     # Perhitungan (rumus) mencari nilai energi kinetik sebelum tumbukan dan pembulatannya sebanyak 3 angka
            ek_akhir = round((1/2)*m1*(v1_akhir**2)+(1/2)*m2*(v2_akhir**2), 3)                  # Perhitungan (rumus) mencari nilai energi kinetik setelah tumbukan dan pembulatannya sebanyak 3 angka
        
        except ValueError:
            # Memberikan pesan error jika nilai yang diinput bukan merupakan bilangan real
            messagebox.showerror('Error', 'Masukkan bilangan real.',                    
                                 parent=vakhir1dimensi)
            return
        
        except:
            # Memberikan pesan error jika terjadi error selain error yang telah didefinisikan sebelumnya
            messagebox.showerror('Error', 'Terjadi error.', parent=vakhir1dimensi)  
            return
        
        if restitusi == 0:  
            # Jika input besar konstanta restitusi bernilai 0, maka akan memunculkan text berupa jenis tumbukan inelastis sempurna pada kolom jenis tumbukan
            text_jenistumbukan.config(state='normal')
            text_jenistumbukan.delete(1.0, 'end')
            text_jenistumbukan.insert(1.0, 'inelastis sempurna')
            text_jenistumbukan.tag_add('right', 1.0, 'end')
            text_jenistumbukan.config(state='disabled')
        
        elif restitusi > 0 and restitusi < 1:   
            # Jika input besar konstanta restitusi bernilai antara 0-1, maka akan memunculkan text berupa jenis tumbukan elastis sebagian pada kolom jenis tumbukan
            text_jenistumbukan.config(state='normal')
            text_jenistumbukan.delete(1.0, 'end')
            text_jenistumbukan.insert(1.0, 'elastis sebagian')
            text_jenistumbukan.tag_add('right', 1.0, 'end')
            text_jenistumbukan.config(state='disabled')
            
        elif restitusi == 1:    
            # Jika input besar konstanta restitusi bernilai 1, maka akan memunculkan text berupa jenis tumbukan elastis sempurna pada kolom jenis tumbukan
            text_jenistumbukan.config(state='normal')
            text_jenistumbukan.delete(1.0, 'end')
            text_jenistumbukan.insert(1.0, 'elastis sempurna')
            text_jenistumbukan.tag_add('right', 1.0, 'end')
            text_jenistumbukan.config(state='disabled')
            
        elif restitusi > 1:     
            # Jika input besar konstanta restitusi bernilai lebih besar dari 1, maka akan memunculkan text berupa jenis tumbukan superelastis pada kolom jenis tumbukan
            text_jenistumbukan.config(state='normal')
            text_jenistumbukan.delete(1.0, 'end')
            text_jenistumbukan.insert(1.0, 'superelastis')
            text_jenistumbukan.tag_add('right', 1.0, 'end')
            text_jenistumbukan.config(state='disabled')
    
        # Memunculkan hasil output nilai momentum yang dihasilkan
        text_momentum.config(state='normal')
        text_momentum.delete(1.0, 'end')
        text_momentum.insert(1.0, f'{momentum}')
        text_momentum.tag_add('right', 1.0, 'end')
        text_momentum.config(state='disabled')
        
        # Memunculkan hasil output kecepatan akhir benda 1 yang dihasilkan
        text_v1akhir.config(state='normal')
        text_v1akhir.delete(1.0, 'end')
        text_v1akhir.insert(1.0, f'{v1_akhir}')
        text_v1akhir.tag_add('right', 1.0, 'end')
        text_v1akhir.config(state='disabled')

        # Memunculkan hasil output kecepatan akhir benda 2 yang dihasilkan
        text_v2akhir.config(state='normal')
        text_v2akhir.delete(1.0, 'end')
        text_v2akhir.insert(1.0, f'{v2_akhir}')
        text_v2akhir.tag_add('right', 1.0, 'end')
        text_v2akhir.config(state='disabled')
        
        # Memunculkan hasil output nilai energi kinetik sebelum tumbukan
        text_ekawal.config(state='normal')
        text_ekawal.delete(1.0, 'end')
        text_ekawal.insert(1.0, f'{ek_awal}')
        text_ekawal.tag_add('right', 1.0, 'end')
        text_ekawal.config(state='disabled')

        # Memunculkan hasil output nilai energi kinetik setelah tumbukan
        text_ekakhir.config(state='normal')
        text_ekakhir.delete(1.0, 'end')
        text_ekakhir.insert(1.0, f'{ek_akhir}')
        text_ekakhir.tag_add('right', 1.0, 'end')
        text_ekakhir.config(state='disabled')
        
    def vakhir_duadimensi():  # Mendefinisikan program untuk menentukan kecepatan dengan 2 dimensi
        try:
            m1 = float(entry_massa1.get())              # Input data berupa massa benda 1 dalam satuan kilogram
            v1x_awal = float(entry_v1xawal.get())       # Input data berupa kecepatan awal (dalam komponen x) massa benda 1 dalam satuan meter per sekon
            v1y_awal = float(entry_v1yawal.get())       # Input data berupa kecepatan awal (dalam komponen y) massa benda 1 dalam satuan meter per sekon
            
            m2 = float(entry_massa2.get())              # Input data berupa massa benda 2 dalam satuan kilogram
            v2x_awal = float(entry_v2xawal.get())       # Input data berupa kecepatan awal (dalam komponen x) massa benda 2 dalam satuan meter per sekon
            v2y_awal = float(entry_v2yawal.get())       # Input data berupa kecepatan awal (dalam komponen y) massa benda 1 dalam satuan meter per sekon
            
            if m1 <= 0 or m2 <= 0:
                # Memberikan pesan error jika input data massa benda 1 atau massa benda 2 bernilai negatif
                messagebox.showerror('Error', 'Massa harus bernilai positif.',      
                                     parent=vakhir2dimensi)
                return
            
            if v1x_awal == 0 and v1y_awal == 0 and v2x_awal == 0 and v2y_awal == 0:
                # Memberikan pesan error jika input data kecepatan awal benda 1 (komponen x dan y) dan kecepatan awal benda 2 (komponen x dan y) bernilai nol, maka tidak memungkinkan kedua benda bertumbukan
                messagebox.showerror('Error', 'Kedua benda diam dan tidak akan '    
                                     'bertumbukan.', parent=vakhir2dimensi)
                return
            
            if v1x_awal == v2x_awal and v1y_awal == v2y_awal:
                # Memberikan pesan error jika input data kecepatan awal benda 1 (komponen x dan y) dan kecepatan awal benda 2 (komponen x dan y) bernilai sama besar, maka tidak memungkinkan kedua benda bertumbukan                       
                messagebox.showerror('Error', 'Kedua benda memiliki kecepatan '
                                     'awal yang sama dan tidak akan bertumbukan.', 
                                     parent=vakhir2dimensi)
                return
            
            if nilai_pilihanbenda.get() == 'Benda 1':   # Jika yang opsi yang dipilih benda 1
                
                # Input dan perhitungan kecepatan akhir pada benda 1 dalam masing-masing komponen x dan y
                v1x_akhir = float(entry_vxakhir.get())
                v1y_akhir = float(entry_vyakhir.get())
                v2x_akhir = (m1*(v1x_awal-v1x_akhir)+m2*v2x_awal)/m2
                v2y_akhir = (m1*(v1y_awal-v1y_akhir)+m2*v2y_awal)/m2
                
                # Memunculkan hasil output kecepatan akhir (komponen x) benda 1 yang dihasilkan
                text_vxakhirhasil.config(state='normal')
                text_vxakhirhasil.delete(1.0, 'end')
                text_vxakhirhasil.insert(1.0, f'{v2x_akhir}')
                text_vxakhirhasil.tag_add('right', 1.0, 'end')
                text_vxakhirhasil.config(state='disabled')
                
                # Memunculkan hasil output kecepatan akhir (sumbu y) benda 1 yang dihasilkan
                text_vyakhirhasil.config(state='normal')
                text_vyakhirhasil.delete(1.0, 'end')
                text_vyakhirhasil.insert(1.0, f'{v2y_akhir}')
                text_vyakhirhasil.tag_add('right', 1.0, 'end')
                text_vyakhirhasil.config(state='disabled')
                 
            elif nilai_pilihanbenda.get() == 'Benda 2':     # Jika yang opsi yang dipilih benda 2
                
                # Input dan perhitungan kecepatan akhir pada benda 2 dalam masing-masing komponen x dan y
                v2x_akhir = float(entry_vxakhir.get())
                v2y_akhir = float(entry_vyakhir.get())
                v1x_akhir = (m1*v1x_awal+m2*(v2x_awal-v2x_akhir))/m1
                v1y_akhir = (m1*v1y_awal+m2*(v2y_awal-v2y_akhir))/m1
            
                # Memunculkan hasil output kecepatan akhir (komponen x) benda 2 yang dihasilkan
                text_vxakhirhasil.config(state='normal')
                text_vxakhirhasil.delete(1.0, 'end')
                text_vxakhirhasil.insert(1.0, f'{v1x_akhir}')
                text_vxakhirhasil.tag_add('right', 1.0, 'end')
                text_vxakhirhasil.config(state='disabled')
                
                # Memunculkan hasil output kecepatan akhir (komponen y) benda 2 yang dihasilkan
                text_vyakhirhasil.config(state='normal')
                text_vyakhirhasil.delete(1.0, 'end')
                text_vyakhirhasil.insert(1.0, f'{v1y_akhir}')
                text_vyakhirhasil.tag_add('right', 1.0, 'end')
                text_vyakhirhasil.config(state='disabled')
                
            v1_awal = ((v1x_awal**2)+(v1y_awal**2))**(1/2)                      # Menghitung resultan kecepatan awal benda 1 dari komponen x dan y
            v2_awal = ((v2x_awal**2)+(v2y_awal**2))**(1/2)                      # Menghitung resultan kecepatan awal benda 2 dari komponen x dan y
            v1_akhir = ((v1x_akhir**2)+(v1y_akhir**2))**(1/2)                   # Menghitung resultan kecepatan akhir benda 1 dari komponen x dan y
            v2_akhir = ((v2x_akhir**2)+(v2y_akhir**2))**(1/2)                   # Menghitung resultan kecepatan akhir benda 2 dari komponen x dan y
            momentumx = round(m1*v1x_awal+m2*v2x_awal, 3)                       # Menghitung nilai momentum dalam komponen x
            momentumy = round(m1*v1y_awal+m2*v2y_awal, 3)                       # Menghitung nilai momentum dalam komponen y
            ek_awal = round((1/2)*m1*(v1_awal**2)+(1/2)*m2*(v2_awal**2), 3)     # Menghitung energi kinetik sebelum tumbukan dan pembulatannya dalam 3 angka
            ek_akhir = round((1/2)*m1*(v1_akhir**2)+(1/2)*m2*(v2_akhir**2), 3)  # Menghitung energi kinetik setelah tumbukan dan pembulatannya dalam 3 angka
        
        except ValueError:
            # Memberikan pesan error jika nilai yang diinput bukan merupakan bilangan real
            messagebox.showerror('Error', 'Masukkan bilangan real.',            
                                 parent=vakhir2dimensi)
            return
            
        except:
            # Memberikan pesan error jika terjadi error selain error yang telah didefinisikan sebelumnya
            messagebox.showerror('Error', 'Terjadi error.',                     
                                 parent=vakhir2dimensi)
            return
        
        if v1x_akhir == v2x_akhir and v1y_akhir == v2y_akhir:
            # Memunculkan ouput jenis tumbukan 'inelastis sempurna' jika kecepatan akhir komponen x dan y pada benda 1 dan 2 sama besar
            text_jenistumbukan.config(state='normal')
            text_jenistumbukan.delete(1.0, 'end')
            text_jenistumbukan.insert(1.0, 'inelastis sempurna')
            text_jenistumbukan.tag_add('right', 1.0, 'end')
            text_jenistumbukan.config(state='disabled')
        
        elif ek_awal == ek_akhir:
            # Memunculkan output jenis tumbukan 'elastis sempurna' jika besar energi kinetik sebelum dan sesudah tumbukan sama besar
            text_jenistumbukan.config(state='normal')
            text_jenistumbukan.delete(1.0, 'end')
            text_jenistumbukan.insert(1.0, 'elastis sempurna')
            text_jenistumbukan.tag_add('right', 1.0, 'end')
            text_jenistumbukan.config(state='disabled')
     
        elif ek_awal > ek_akhir:
            # Memunculkan output jenis tumbukan 'elastis sebagian' jika besar energi kinetik sebelum lebih besar dari energi kinetik sesudah tumbukan
            text_jenistumbukan.config(state='normal')
            text_jenistumbukan.delete(1.0, 'end')
            text_jenistumbukan.insert(1.0, 'elastis sebagian')
            text_jenistumbukan.tag_add('right', 1.0, 'end')
            text_jenistumbukan.config(state='disabled')
       
        elif ek_awal < ek_akhir:
            # Memunculkan output jenis tumbukan 'superelastis' jika besar energi kinetik sesudah lebih besar dari energi kinetik sebelum tumbukan
            text_jenistumbukan.config(state='normal')
            text_jenistumbukan.delete(1.0, 'end')
            text_jenistumbukan.insert(1.0, 'superelastis')
            text_jenistumbukan.tag_add('right', 1.0, 'end')
            text_jenistumbukan.config(state='disabled')
       
        else:
            # Memunculkan output jenis tumbukan 'N/A' jika terdapat input yang tidak sesuai
            text_jenistumbukan.config(state='normal')
            text_jenistumbukan.delete(1.0, 'end')
            text_jenistumbukan.insert(1.0, 'N/A')
            text_jenistumbukan.tag_add('right', 1.0, 'end')
            text_jenistumbukan.config(state='disabled')
        
        # Memunculkan hasil output nilai momentum komponen x yang dihasilkan
        text_momentumx.config(state='normal')
        text_momentumx.delete(1.0, 'end')
        text_momentumx.insert(1.0, f'{momentumx}')
        text_momentumx.tag_add('right', 1.0, 'end')
        text_momentumx.config(state='disabled')
    
        # Memunculkan hasil output nilai momentum komponen y yang dihasilkan
        text_momentumy.config(state='normal')
        text_momentumy.delete(1.0, 'end')
        text_momentumy.insert(1.0, f'{momentumy}')
        text_momentumy.tag_add('right', 1.0, 'end')
        text_momentumy.config(state='disabled')
    
        # Memunculkan hasil output nilai energi kinetik sebelum tumbukan
        text_ekawal.config(state='normal')
        text_ekawal.delete(1.0, 'end')
        text_ekawal.insert(1.0, f'{ek_awal}')
        text_ekawal.tag_add('right', 1.0, 'end')
        text_ekawal.config(state='disabled')
    
        # Memunculkan hasil output nilai energi kinetik setelah tumbukan
        text_ekakhir.config(state='normal')
        text_ekakhir.delete(1.0, 'end')
        text_ekakhir.insert(1.0, f'{ek_akhir}')
        text_ekakhir.tag_add('right', 1.0, 'end')
        text_ekakhir.config(state='disabled') 
        
# =============================================================================
# Algoritma Bagian Display
# Pada bagian ini, terdapat dua cabang sesuai dengan dimensi yang dipilih pengguna.
# Kedua cabang ini  berisi perintah-perintah tkinter untuk membuat display yang
# akan menerima input dan menampilkan output sesuai dengan dimensi yang dipilih.
# =============================================================================

    if pilihandimensi=='1 Dimensi': # Jika opsi yang dipilih adalah 1 dimensi
        
        # Set-up window dan menempatkannya di tengah layar
        vakhir1dimensi = tk.Toplevel()
        vakhir1dimensi.geometry("820x560")
        windowWidth = 820
        windowHeight = 560
        positionRight = int(vakhir1dimensi.winfo_screenwidth()/2 - windowWidth/2)
        positionDown = int(vakhir1dimensi.winfo_screenheight()/2.2 - windowHeight/2)
        vakhir1dimensi.geometry("+{}+{}".format(positionRight, positionDown))
        vakhir1dimensi.configure(bg = "#FFFFFF")
        vakhir1dimensi.resizable(False, False)
        
        # Membuat canvas sebagai tempat bagi seluruh text dan rectangle
        canvas = Canvas(
            vakhir1dimensi,
            bg = "#FFFFFF",
            height = 560,
            width = 820,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)
        
        # Membuat dua rectangle dan text sebagai header dan judul subprogram
        # menentukan kecepatan akhir 1 dimensi
        canvas.create_rectangle(
            0.0,
            0.0,
            820.0,
            100.0,
            fill="#000000",
            outline="")
        
        canvas.create_text(
            23.0,
            10.0,
            anchor="nw",
            text="Menentukan\nKecepatan\nAkhir",
            fill="#FCA311",
            font=("Montserrat Bold", 18 * -1))
        
        canvas.create_text(
            189.0,
            35.0,
            anchor="nw",
            text="1 Dimensi",
            fill="#FCA311",
            font=("Montserrat Bold", 18 * -1))
        
        canvas.create_rectangle(
            165.0,
            19.0,
            168.0,
            81.0,
            fill="#FCA311",
            outline="")
        
        # Membuat empat rectangle sebagai frame untuk data benda 1, benda 2, 
        # koefisien restitusi, dan hasil
        canvas.create_rectangle(
            421.0,
            123.0,
            801.0,
            190.0,
            fill="#E5E5E5",
            outline="")
        
        canvas.create_rectangle(
            20.0,
            123.0,
            400.0,
            190.0,
            fill="#E5E5E5",
            outline="")
        
        canvas.create_rectangle(
            122.0,
            355.0,
            698.0,
            528.0,
            fill="#E5E5E5",
            outline="")
        
        canvas.create_rectangle(
            233.0,
            212.0,
            588.0,
            253.0,
            fill="#E5E5E5",
            outline="")
        
        # Data Benda 1
        canvas.create_text(
            29.0,
            112.0,
            anchor="nw",
            text="Benda 1",
            fill="#000000",
            font=("Montserrat Medium", 16 * -1))
        
        # Membuat text untuk massa benda 1
        canvas.create_text(
            34.0,
            137.0,
            anchor="nw",
            text="Massa",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        canvas.create_text(
            234.0,
            137.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat entry untuk memasukkan input massa benda 1
        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_vakhir1dimensi_1.png"))
        entry_bg_1 = canvas.create_image(
            302.0,
            144.0,
            image=entry_image_1)
        
        entry_massa1 = Entry(
            vakhir1dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        entry_massa1.place(
            x=252.0,
            y=134.0,
            width=100.0,
            height=18.0)
        
        # Membuat text untuk satuan dari massa benda 1
        canvas.create_text(
            370.0,
            137.0,
            anchor="nw",
            text="kg",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat text untuk kecepatan benda 1 sebelum tumbukan
        canvas.create_text(
            34.0,
            163.0,
            anchor="nw",
            text="Kecepatan sebelum tumbukan",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        canvas.create_text(
            234.0,
            163.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat entry untuk memasukkan input kecepatan benda 1 sebelum 
        # tumbukan
        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_vakhir1dimensi_2.png"))
        entry_bg_2 = canvas.create_image(
            302.0,
            170.0,
            image=entry_image_2)
        
        entry_v1awal = Entry(
            vakhir1dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        entry_v1awal.place(
            x=252.0,
            y=160.0,
            width=100.0,
            height=18.0)
        
        # Membuat text untuk satuan dari kecepatan
        canvas.create_text(
            370.0,
            163.0,
            anchor="nw",
            text="m/s",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Data Benda 2
        canvas.create_text(
            429.0,
            112.0,
            anchor="nw",
            text="Benda 2",
            fill="#000000",
            font=("Montserrat Medium", 16 * -1))
        
        # Membuat text untuk massa benda 2
        canvas.create_text(
            434.0,
            137.0,
            anchor="nw",
            text="Massa",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        canvas.create_text(
            634.0,
            137.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat entry untuk memasukkan input massa dari benda 1
        entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_vakhir1dimensi_3.png"))
        entry_bg_3 = canvas.create_image(
            706.0,
            144.0,
            image=entry_image_3)
        
        entry_massa2 = Entry(
            vakhir1dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        entry_massa2.place(
            x=656.0,
            y=134.0,
            width=100.0,
            height=18.0)
        
        # Membuat text untuk satuan dari massa benda 2
        canvas.create_text(
            772.0,
            137.0,
            anchor="nw",
            text="kg",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat text untuk kecepatan benda 2 sebelum tumbukan
        canvas.create_text(
            434.0,
            163.0,
            anchor="nw",
            text="Kecepatan sebelum tumbukan",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        canvas.create_text(
            634.0,
            163.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat entry untuk memasukkan input kecepatan benda 2 sebelum tumbukan
        entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_vakhir1dimensi_4.png"))
        entry_bg_4 = canvas.create_image(
            706.0,
            170.0,
            image=entry_image_4)
        
        entry_v2awal = Entry(
            vakhir1dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        entry_v2awal.place(
            x=656.0,
            y=160.0,
            width=100.0,
            height=18.0)
        
        # Membuat text untuk satuan dari kecepatan
        canvas.create_text(
            772.0,
            163.0,
            anchor="nw",
            text="m/s",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Data Koefisien Restitusi
        canvas.create_text(
            242.0,
            201.0,
            anchor="nw",
            text="Koefisien Restitusi",
            fill="#000000",
            font=("Montserrat Medium", 16 * -1))
        
        # Membuat text untuk nilai koefisien restitusi
        canvas.create_text(
            247.0,
            226.0,
            anchor="nw",
            text="Nilai koefisien restitusi",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        canvas.create_text(
            447.0,
            226.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat entry untuk memasukkan input nilai koefisien restitusi
        entry_image_5 = PhotoImage(
            file=relative_to_assets("entry_vakhir1dimensi_5.png"))
        entry_bg_5 = canvas.create_image(
            515.0,
            233.0,
            image=entry_image_5)
        
        entry_restitusi = Entry(
            vakhir1dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        entry_restitusi.place(
            x=465.0,
            y=223.0,
            width=100.0,
            height=18.0)
        
        # Membuat text untuk catatan keakuratan
        canvas.create_text(
            249.0,
            260.0,
            anchor="nw",
            text="Catatan: Untuk hasil yang akurat, masukkan 4 angka di belakang koma ",
            fill="#000000",
            font=("Montserrat Regular", 9 * -1))
        
        # Membuat button Jalankan Program! yang bila ditekan akan menjalankan
        # perhitungan
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_vakhir1dimensi.png"))
        
        button_1 = Button(
            vakhir1dimensi,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: vakhir_satudimensi(),
            relief="flat")
        button_1.place(
            x=313.0,
            y=294.0,
            width=195.0,
            height=41.0)
        
        # Data Hasil
        canvas.create_text(
            135.0,
            343.0,
            anchor="nw",
            text="Hasil",
            fill="#000000",
            font=("Montserrat Medium", 16 * -1))
        
        # Membuat text untuk besar momentum dari sistem
        canvas.create_text(
            139.0,
            368.0,
            anchor="nw",
            text="Besar momentum sistem",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        canvas.create_text(
            441.0,
            368.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat TextArea untuk menampilkan output besar momentum dari sistem
        entry_image_6 = PhotoImage(
            file=relative_to_assets("text_vakhir1dimensi_6.png"))
        entry_bg_6 = canvas.create_image(
            543.0,
            374.0,
            image=entry_image_6)
        
        text_momentum = Text(
            vakhir1dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        text_momentum.place(
            x=463.0,
            y=364.0,
            width=160.0,
            height=18.0)
        text_momentum.config(
            state='disabled')
        
        # Membuat text untuk satuan dari momentum
        canvas.create_text(
            642.0,
            367.0,
            anchor="nw",
            text="kg . m/s",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat text untuk kecepatan benda 1 setelah tumbukan
        canvas.create_text(
            139.0,
            394.0,
            anchor="nw",
            text="Kecepatan benda 1 setelah tumbukan",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        canvas.create_text(
            441.0,
            394.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat TextArea untuk menampilkan output kecepatan benda 1 
        # setelah tumbukan
        entry_image_7 = PhotoImage(
            file=relative_to_assets("text_vakhir1dimensi_7.png"))
        entry_bg_7 = canvas.create_image(
            543.0,
            400.0,
            image=entry_image_7)
        
        text_v1akhir = Text(
            vakhir1dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        text_v1akhir.place(
            x=463.0,
            y=390.0,
            width=160.0,
            height=18.0)
        text_v1akhir.config(
            state='disabled')
        
        # Membuat text untuk satuan dari kecepatan
        canvas.create_text(
            642.0,
            393.0,
            anchor="nw",
            text="m/s",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat text untuk kecepatan benda 2 setelah tumbukan
        canvas.create_text(
            139.0,
            420.0,
            anchor="nw",
            text="Kecepatan benda 2 setelah tumbukan",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        canvas.create_text(
            441.0,
            420.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat TextArea untuk menampilkan output kecepatan benda 2 setelah
        # tumbukan
        entry_image_8 = PhotoImage(
            file=relative_to_assets("text_vakhir1dimensi_8.png"))
        entry_bg_8 = canvas.create_image(
            543.0,
            426.0,
            image=entry_image_8)
        
        text_v2akhir = Text(
            vakhir1dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        text_v2akhir.place(
            x=463.0,
            y=416.0,
            width=160.0,
            height=18.0)
        text_v2akhir.config(
            state='disabled')
        
        # Membuat text untuk satuan kecepatan
        canvas.create_text(
            642.0,
            419.0,
            anchor="nw",
            text="m/s",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat text untuk besar energi kinetik sistem sebelum tumbukan
        canvas.create_text(
            139.0,
            446.0,
            anchor="nw",
            text="Besar energi kinetik sistem sebelum tumbukan",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        canvas.create_text(
            441.0,
            446.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat TextArea untuk menampilkan output besar energi kinetik
        # sistem sebelum tumbukan
        entry_image_9 = PhotoImage(
            file=relative_to_assets("text_vakhir1dimensi_9.png"))
        entry_bg_9 = canvas.create_image(
            543.0,
            452.0,
            image=entry_image_9)
        
        text_ekawal = Text(
            vakhir1dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        text_ekawal.place(
            x=463.0,
            y=442.0,
            width=160.0,
            height=18.0)
        text_ekawal.config(
            state='disabled')
        
        # Membuat text untuk satuan dari energi kinetik
        canvas.create_text(
            642.0,
            445.0,
            anchor="nw",
            text="J",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat text untuk besar energi kinetik setelah tumbukan
        canvas.create_text(
            139.0,
            472.0,
            anchor="nw",
            text="Besar energi kinetik sistem setelah tumbukan",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        canvas.create_text(
            441.0,
            472.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat TextArea untuk menampilkan output besar energi kinetik
        # setelah tumbukan
        entry_image_10 = PhotoImage(
            file=relative_to_assets("text_vakhir1dimensi_10.png"))
        entry_bg_10 = canvas.create_image(
            543.0,
            478.0,
            image=entry_image_10)
        
        text_ekakhir = Text(
            vakhir1dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        text_ekakhir.place(
            x=463.0,
            y=468.0,
            width=160.0,
            height=18.0)
        text_ekakhir.config(
            state='disabled')
        
        # Membuat text untuk satuan dari energi kinetik
        canvas.create_text(
            642.0,
            471.0,
            anchor="nw",
            text="J",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat text untuk jenis tumbukan
        canvas.create_text(
            139.0,
            498.0,
            anchor="nw",
            text="Jenis tumbukan",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        canvas.create_text(
            441.0,
            498.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat TextArea untuk menampilkan output jenis tumbukan
        entry_image_11 = PhotoImage(
            file=relative_to_assets("text_vakhir1dimensi_11.png"))
        entry_bg_11 = canvas.create_image(
            543.0,
            504.0,
            image=entry_image_11)
        
        text_jenistumbukan = Text(
            vakhir1dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        text_jenistumbukan.place(
            x=463.0,
            y=494.0,
            width=160.0,
            height=18.0)
        text_jenistumbukan.config(
            state='disabled')
        
        # Membuat text untuk catatan pembulatan
        canvas.create_text(
            275.0,
            535.0,
            anchor="nw",
            text="Catatan: Hasil dibulatkan hingga 3 angka di belakang koma ",
            fill="#000000",
            font=("Montserrat Regular", 9 * -1))
        
        # Menjalankan aplikasi agar tetap berjalan sebelum di-close
        vakhir1dimensi.mainloop()
        
    elif pilihandimensi =='2 Dimensi':   # Jika opsi yang dipilih adalah 2 dimensi
        
        def gantibenda(option_benda): # Mendefinisikan fungsi untuk mengubah label sesuai dengan benda yang dipilih
            
            if option_benda == 'Benda 1':
                canvas.itemconfigure(text_vakhir, text='Kecepatan benda 1 setelah tumbukan')
                canvas.itemconfigure(text_vakhirhasil, text='Kecepatan benda 2 setelah tumbukan')
            elif option_benda == 'Benda 2':
                canvas.itemconfigure(text_vakhir, text='Kecepatan benda 2 setelah tumbukan')
                canvas.itemconfigure(text_vakhirhasil, text='Kecepatan benda 1 setelah tumbukan')

        # Set-up window dan menempatkannya di tengah layar
        vakhir2dimensi = tk.Toplevel()
        vakhir2dimensi.geometry("1200x570")
        windowWidth = 1200
        windowHeight = 570
        positionRight = int(vakhir2dimensi.winfo_screenwidth()/2 - windowWidth/2)
        positionDown = int(vakhir2dimensi.winfo_screenheight()/2.2 - windowHeight/2)
        vakhir2dimensi.geometry("+{}+{}".format(positionRight, positionDown))
        vakhir2dimensi.configure(bg = "#FFFFFF")
        vakhir2dimensi.resizable(False, False)
        
        # Membuat array yang berisi pilihan dimensi yang bisa dipilih dan
        # menginisialisasi variabel nilai_pilihandimensi 
        benda = ['Benda 1', 'Benda 2']
        nilai_pilihanbenda = tk.StringVar()
        
        # Membuat canvas sebagai tempat bagi seluruh text dan rectangle
        canvas = Canvas(
            vakhir2dimensi,
            bg = "#FFFFFF",
            height = 570,
            width = 1200,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)
        
        # Membuat dua rectangle dan text sebagai header dan judul subprogram
        # menentukan kecepatan akhir 2 dimensi
        canvas.create_rectangle(
            0.0,
            0.0,
            1200.0,
            100.0,
            fill="#000000",
            outline="")
        
        canvas.create_text(
            23,
            10.0,
            anchor="nw",
            text="Menentukan\nKecepatan\nAkhir",
            fill="#FCA311",
            font=("Montserrat Bold", 18 * -1))
        
        canvas.create_text(
            189.0,
            35.0,
            anchor="nw",
            text="2 Dimensi",
            fill="#FCA311",
            font=("Montserrat Bold", 18 * -1))
        
        canvas.create_rectangle(
            165.0,
            19.0,
            168.0,
            81.0,
            fill="#FCA311",
            outline="")
        
        # Membuat empat rectangle sebagai frame untuk data benda 1, benda 2, 
        # kecepatan akhir salah satu benda, dan hasil
        canvas.create_rectangle(
            35.0,
            123.0,
            585.0,
            190.0,
            fill="#E5E5E5",
            outline="")
        
        canvas.create_rectangle(
            615.0,
            123.0,
            1165.0,
            190.0,
            fill="#E5E5E5",
            outline="")
        
        canvas.create_rectangle(
            290.0,
            215.0,
            876.0,
            286.0,
            fill="#E5E5E5",
            outline="")
        
        canvas.create_rectangle(
            202.0,
            385.0,
            999.0,
            529.0,
            fill="#E5E5E5",
            outline="")
        
        # Data Benda 1
        canvas.create_text(
            44.0,
            112.0,
            anchor="nw",
            text="Benda 1",
            fill="#000000",
            font=("Montserrat Medium", 16 * -1))
        
        # Membuat text untuk massa benda 1
        canvas.create_text(
            49.0,
            137.0,
            anchor="nw",
            text="Massa",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        canvas.create_text(
            249.0,
            137.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat entry untuk memasukkan input massa benda 1
        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_vakhir2dimensi_1.png"))
        entry_bg_1 = canvas.create_image(
            317.0,
            144.0,
            image=entry_image_1)
        
        entry_massa1 = Entry(
            vakhir2dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        entry_massa1.place(
            x=267.0,
            y=134.0,
            width=100.0,
            height=18.0)
        
        # Membuat text untuk satuan massa
        canvas.create_text(
            384.0,
            137.0,
            anchor="nw",
            text="kg",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat text untuk kecepatan benda 1 sebelum tumbukan
        canvas.create_text(
            49.0,
            163.0,
            anchor="nw",
            text="Kecepatan sebelum tumbukan",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        canvas.create_text(
            249.0,
            163.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat entry untuk memasukkan input besar komponen sumbu x dari 
        # kecepatan benda 1 sebelum tumbukan
        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_vakhir2dimensi_2.png"))
        entry_bg_2 = canvas.create_image(
            317.0,
            170.0,
            image=entry_image_2)
        
        entry_v1xawal = Entry(
            vakhir2dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        entry_v1xawal.place(
            x=267.0,
            y=160.0,
            width=100.0,
            height=18.0)
        
        # Membuat text untuk unit vektor sumbu x (i)
        canvas.create_text(
            384.0,
            163.0,
            anchor="nw",
            text="i  +",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat entry untuk memasukkan input besar komponen sumbu y dari
        # kecepatan benda 1 sebelum tumbukan
        entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_vakhir2dimensi_3.png"))
        entry_bg_3 = canvas.create_image(
            468.0,
            170.0,
            image=entry_image_3)
        
        entry_v1yawal = Entry(
            vakhir2dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        entry_v1yawal.place(
            x=418.0,
            y=160.0,
            width=100.0,
            height=18.0)
        
        # Membuat text untuk unit vektor sumbu y (j) dan satuan kecepatan
        canvas.create_text(
            538.0,
            163.0,
            anchor="nw",
            text="j   m/s",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Data Benda 2
        canvas.create_text(
            623.0,
            112.0,
            anchor="nw",
            text="Benda 2",
            fill="#000000",
            font=("Montserrat Medium", 16 * -1))

        # Membuat text untuk massa benda 2
        canvas.create_text(
            628.0,
            137.0,
            anchor="nw",
            text="Massa",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        canvas.create_text(
            828.0,
            137.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat entry untuk memasukkan input massa benda 2
        entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_vakhir2dimensi_4.png"))
        entry_bg_4 = canvas.create_image(
            900.0,
            144.0,
            image=entry_image_4)
        
        entry_massa2 = Entry(
            vakhir2dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        entry_massa2.place(
            x=850.0,
            y=134.0,
            width=100.0,
            height=18.0)
        
        # Membuat text untuk satuan massa
        canvas.create_text(
            965.0,
            137.0,
            anchor="nw",
            text="kg",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat text untuk kecepatan benda 2 sebelum tumbukan
        canvas.create_text(
            628.0,
            163.0,
            anchor="nw",
            text="Kecepatan sebelum tumbukan",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        canvas.create_text(
            828.0,
            163.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat entry untuk memasukkan input besar komponen sumbu x dari
        # kecepatan benda 2 sebelum tumbukan
        entry_image_5 = PhotoImage(
            file=relative_to_assets("entry_vakhir2dimensi_5.png"))
        entry_bg_5 = canvas.create_image(
            900.0,
            170.0,
            image=entry_image_5)
        
        entry_v2xawal = Entry(
            vakhir2dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        entry_v2xawal.place(
            x=850.0,
            y=160.0,
            width=100.0,
            height=18.0)
        
        # Membuat text untuk unit vektor sumbu x (i)
        canvas.create_text(
            965.0,
            163.0,
            anchor="nw",
            text="i  +",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat entry untuk memasukkan input besar komponen sumbu y dari 
        # kecepatan benda 2 sebelum tumbukan
        entry_image_6 = PhotoImage(
            file=relative_to_assets("entry_vakhir2dimensi_6.png"))
        entry_bg_6 = canvas.create_image(
            1051.0,
            170.0,
            image=entry_image_6)
        
        entry_v2yawal = Entry(
            vakhir2dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        entry_v2yawal.place(
            x=1001.0,
            y=160.0,
            width=100.0,
            height=18.0)
        
        # Membuat text untuk unit vektor sumbu y (j) dan satuan kecepatan
        canvas.create_text(
            1119.0,
            163.0,
            anchor="nw",
            text="j   m/s",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Data Kecepatan Akhir Salah Satu Benda
        canvas.create_text(
            304.0,
            204.0,
            anchor="nw",
            text="Kecepatan Akhir Salah Satu Benda",
            fill="#000000",
            font=("Montserrat Medium", 16 * -1))
        
        # Membuat text pilih benda
        canvas.create_text(
            519.0,
            230.0,
            anchor="nw",
            text="Pilih benda :",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat style untuk mengganti font dan size font dari OptionMenu
        # Pilihan Benda
        ttk.Style().configure('Mini.TMenubutton',font=("Montserrat Regular", 12 * -1))
        
        # Membuat OptionMenu Pilihan Benda sebagai pilihan dari salah satu
        # benda yang akan diinput kecepatannya setelah tumbukan
        pilihanbenda = ttk.OptionMenu(vakhir2dimensi, nilai_pilihanbenda, benda[0], *benda, 
                                      style='Mini.TMenubutton', command=gantibenda)
        pilihanbenda['menu'].configure(font=("Montserrat Regular", 12 * -1))
        pilihanbenda.place(x=599, y=225, anchor="nw")
        
        # Membuat text untuk kecepatan salah satu benda setelah tumbukan (pilihan
        # default adalah benda 1)
        text_vakhir = canvas.create_text(
            301.0,
            259.0,
            anchor="nw",
            text="Kecepatan benda 1 setelah tumbukan",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        canvas.create_text(
            541.0,
            259.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat entry untuk memasukkan input besar komponen x dari kecepatan
        # salah satu benda setelah tumbukan (pilihan default adalah benda 1)
        entry_image_7 = PhotoImage(
            file=relative_to_assets("entry_vakhir2dimensi_7.png"))
        entry_bg_7 = canvas.create_image(
            609.0,
            266.0,
            image=entry_image_7)
        
        entry_vxakhir = Entry(
            vakhir2dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        entry_vxakhir.place(
            x=559.0,
            y=256.0,
            width=100.0,
            height=18.0)
        
        # Membuat text untuk unit vektor sumbu x (i)
        canvas.create_text(
            676.0,
            259.0,
            anchor="nw",
            text="i  +",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat entry untuk memasukkan input besar komponen y dari kecepatan
        # salah satu benda setelah tumbukan (pilihan default adalah benda 1)
        entry_image_8 = PhotoImage(
            file=relative_to_assets("entry_vakhir2dimensi_8.png"))
        entry_bg_8 = canvas.create_image(
            760.0,
            266.0,
            image=entry_image_8)
        
        entry_vyakhir = Entry(
            vakhir2dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        entry_vyakhir.place(
            x=710.0,
            y=256.0,
            width=100.0,
            height=18.0)
        
        # Membuat text untuk unit vektor sumbu x (i) dan satuan kecepatan
        canvas.create_text(
            830.0,
            252.0,
            anchor="nw",
            text="j   m/s",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat text untuk catatan keakuratan
        canvas.create_text(
            439.0,
            295.0,
            anchor="nw",
            text="Catatan: Untuk hasil yang akurat, masukkan 4 angka di belakang koma ",
            fill="#000000",
            font=("Montserrat Regular", 9 * -1))       
        
        # Membuat button Jalankan Program! yang bila ditekan akan menjalankan
        # perhitungan
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_vakhir2dimensi.png"))
        button_vakhir2dimensi = Button(
            vakhir2dimensi,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: vakhir_duadimensi(),
            relief="flat")
        button_vakhir2dimensi.place(
            x=503.0,
            y=324.0,
            width=195.0,
            height=41.0)
        
        # Data Hasil
        canvas.create_text(
            215.0,
            373.0,
            anchor="nw",
            text="Hasil",
            fill="#000000",
            font=("Montserrat Medium", 16 * -1))
        
        # Membuat text untuk besar momentum sistem
        canvas.create_text(
            219.0,
            398.0,
            anchor="nw",
            text="Besar momentum sistem",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        canvas.create_text(
            521.0,
            398.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat TextArea untuk menampilkan output berupa komponen sumbu x dari
        # momentum sistem
        entry_image_9 = PhotoImage(
            file=relative_to_assets("text_vakhir2dimensi_9.png"))
        entry_bg_9 = canvas.create_image(
            623.0,
            404.0,
            image=entry_image_9)
        
        text_momentumx = Text(
            vakhir2dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        text_momentumx.place(
            x=543.0,
            y=394.0,
            width=160.0,
            height=18.0)
        text_momentumx.config(
            state='disabled')
        
        # Membuat text untuk unit vektor sumbu x (i)
        canvas.create_text(
            719.0,
            397.0,
            anchor="nw",
            text="i  +",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat TextArea untuk menampilkan output berupa komponen sumbu y dari
        # momentum sistem
        entry_image_10 = PhotoImage(
            file=relative_to_assets("text_vakhir2dimensi_10.png"))
        entry_bg_10 = canvas.create_image(
            833.0,
            404.0,
            image=entry_image_10)
        
        text_momentumy = Text(
            vakhir2dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        text_momentumy.place(
            x=753.0,
            y=394.0,
            width=160.0,
            height=18.0)
        text_momentumy.config(
            state='disabled')
        
        # Membuat text untuk unit vektor sumbu y (j) dan satuan momentum
        canvas.create_text(
            931.0,
            397.0,
            anchor="nw",
            text="j   kg . m/s",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat text untuk kecepatan benda lain setelah tumbukan (default
        # adalah benda 2)
        text_vakhirhasil = canvas.create_text(
            219.0,
            424.0,
            anchor="nw",
            text="Kecepatan benda 2 setelah tumbukan",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        canvas.create_text(
            521.0,
            424.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat TextArea untuk menampilkan output berupa komponen sumbu x
        # dari kecepatan benda lain setelah tumbukan (default adalah benda 2)
        entry_image_11 = PhotoImage(
            file=relative_to_assets("text_vakhir2dimensi_11.png"))
        entry_bg_11 = canvas.create_image(
            623.0,
            430.0,
            image=entry_image_11)
        
        text_vxakhirhasil = Text(
            vakhir2dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        text_vxakhirhasil.place(
            x=543.0,
            y=420.0,
            width=160.0,
            height=18.0)
        text_vxakhirhasil.config(
            state='disabled')
        
        # Membuat text untuk unit vektor sumbu x (i)
        canvas.create_text(
            719.0,
            422.0,
            anchor="nw",
            text="i  +",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat TextArea untuk menampilkan output berupa komponen sumbu y
        # dari kecepatan benda lain setelah tumbukan (default adalah benda 2)
        entry_image_12 = PhotoImage(
            file=relative_to_assets("text_vakhir2dimensi_12.png"))
        entry_bg_12 = canvas.create_image(
            833.0,
            430.0,
            image=entry_image_12)
        
        text_vyakhirhasil = Text(
            vakhir2dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        text_vyakhirhasil.place(
            x=753.0,
            y=420.0,
            width=160.0,
            height=18.0)
        text_vyakhirhasil.config(
            state='disabled')
        
        # Membuat text untuk unit vektor sumbu y (j) dan satuan kecepatan
        canvas.create_text(
            931.0,
            422.0,
            anchor="nw",
            text="j   m/s",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat text untuk besar energi kinetik sistem sebelum tumbukan
        canvas.create_text(
            219.0,
            450.0,
            anchor="nw",
            text="Besar energi kinetik sistem sebelum tumbukan",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        canvas.create_text(
            521.0,
            450.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat TextArea untuk menampilkan output berupa energi kinetik 
        # sistem sebelum tumbukan
        entry_image_13 = PhotoImage(
            file=relative_to_assets("text_vakhir2dimensi_13.png"))
        entry_bg_13 = canvas.create_image(
            623.0,
            456.0,
            image=entry_image_13)
        
        text_ekawal = Text(
            vakhir2dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        text_ekawal.place(
            x=543.0,
            y=446.0,
            width=160.0,
            height=18.0)
        text_ekawal.config(
            state='disabled')
        
        # Membuat text untuk satuan energi kinetik (J)
        canvas.create_text(
            719.0,
            449.0,
            anchor="nw",
            text="J",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat text untuk besar energi kinetik sistem setelah tumbukan
        canvas.create_text(
            219.0,
            476.0,
            anchor="nw",
            text="Besar energi kinetik sistem setelah tumbukan",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        canvas.create_text(
            521.0,
            476.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat TextArea untuk menampilkan output berupa besar energi kinetik
        # sistem setelah tumbukan
        entry_image_14 = PhotoImage(
            file=relative_to_assets("text_vakhir2dimensi_14.png"))
        entry_bg_14 = canvas.create_image(
            623.0,
            482.0,
            image=entry_image_14)
        
        text_ekakhir = Text(
            vakhir2dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        text_ekakhir.place(
            x=543.0,
            y=472.0,
            width=160.0,
            height=18.0)
        text_ekakhir.config(
            state='disabled')
        
        # Membuat text untuk satuan energi kinetik (J)
        canvas.create_text(
            719.0,
            475.0,
            anchor="nw",
            text="J",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat text untuk jenis tumbukan
        canvas.create_text(
            219.0,
            502.0,
            anchor="nw",
            text="Jenis tumbukan",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        canvas.create_text(
            521.0,
            502.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Montserrat Regular", 12 * -1))
        
        # Membuat TextArea untuk menampilkan output berupa jenis tumbukan
        entry_image_15 = PhotoImage(
            file=relative_to_assets("text_vakhir2dimensi_15.png"))
        entry_bg_15 = canvas.create_image(
            623.0,
            508.0,
            image=entry_image_15)
        
        text_jenistumbukan = Text(
            vakhir2dimensi,
            bd=0,
            bg="#F5F3F3",
            highlightthickness=0)
        text_jenistumbukan.place(
            x=543.0,
            y=498.0,
            width=160.0,
            height=18.0)
        text_jenistumbukan.config(
            state='disabled')
        
        # Membuat text untuk catatan pembulatan
        canvas.create_text(
            465.0,
            541.0,
            anchor="nw",
            text="Catatan: Hasil dibulatkan hingga 3 angka di belakang koma ",
            fill="#000000",
            font=("Montserrat Regular", 9 * -1))
        
        # Menjalankan aplikasi agar tetap berjalan sebelum di-close
        vakhir2dimensi.mainloop()
      
