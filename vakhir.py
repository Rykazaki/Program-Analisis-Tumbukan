# Tugas Besar Kelompok 3
# PROGRAM    : Subprogram Menentukan Kecepatan Akhir
# DESKRIPSI  : Program yang dapat menentukan kecepatan akhir dalam 1 dimensi 
#              & 2 dimensi berdasarkan data yang diinput oleh pengguna.

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
from tkinter import ttk
from tkinter import messagebox

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
                                     parent=kecepatan_1dimensi)
                return

            if v1_awal == 0 and v2_awal == 0:
                # Memberikan pesan error jika input data kecepatan awal benda 1 dan kecepatan awal benda 2 bernilai nol, maka tidak memungkinkan kedua benda bertumbukan
                messagebox.showerror('Error', 'Kedua benda diam dan tidak akan '    
                                     'bertumbukan', parent=kecepatan_1dimensi)
                return
            
            if v1_awal == v2_awal:
                # Memberikan pesan error jika input data kecepatan awal benda 1 dan kecepatan awal benda 2 bernilai sama besar, maka tidak memungkinkan kedua benda bertumbukan
                messagebox.showerror('Error', 'Kedua benda memiliki kecepatan '     
                                     'awal yang sama dan tidak akan bertumbukan.', 
                                     parent=kecepatan_1dimensi)
                return
            
            if restitusi < 0:
                # Memberikan pesan error jika input data nilai konstanta restitusi bernilai negatif karena nilai konstanta koefisien restitusi mungkin bernilai negatif
                messagebox.showerror('Error', 'Nilai koefisien restitusi tidak '    
                                     'boleh negatif.', parent=kecepatan_1dimensi)
                return

            v1_akhir = round((m1*v1_awal+m2*v2_awal+m2*restitusi*(v2_awal-v1_awal))/(m1+m2), 3) # Perhitungan (rumus) mencari nilai kecepatan akhir benda 1 dan pembulatannya sebanyak 3 angka
            v2_akhir = round((m1*v1_awal+m2*v2_awal+m1*restitusi*(v1_awal-v2_awal))/(m1+m2),3)  # Perhitungan (rumus) mencari nilai kecepatan akhir benda 2 dan pembulatannya sebanyak 3 angka
            momentum = round(m1*v1_awal+m2*v2_awal, 3)                                          # Perhitungan (rumus) mencari nilai momentum dan pembulatannya sebanyak 3 angka
            ek_awal = round((1/2)*m1*(v1_awal**2)+(1/2)*m2*(v2_awal**2), 3)                     # Perhitungan (rumus) mencari nilai energi kinetik sebelum tumbukan dan pembulatannya sebanyak 3 angka
            ek_akhir = round((1/2)*m1*(v1_akhir**2)+(1/2)*m2*(v2_akhir**2), 3)                  # Perhitungan (rumus) mencari nilai energi kinetik setelah tumbukan dan pembulatannya sebanyak 3 angka
        
        except ValueError:
            # Memberikan pesan error jika nilai yang diinput bukan merupakan bilangan real
            messagebox.showerror('Error', 'Masukkan bilangan real.',                    
                                 parent=kecepatan_1dimensi)
            return
        
        except:
            # Memberikan pesan error jika terjadi error selain error yang telah didefinisikan sebelumnya
            messagebox.showerror('Error', 'Terjadi error.', parent=kecepatan_1dimensi)  
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
                                     parent=kecepatan_2dimensi)
                return
            
            if v1x_awal == 0 and v1y_awal == 0 and v2x_awal == 0 and v2y_awal == 0:
                # Memberikan pesan error jika input data kecepatan awal benda 1 (komponen x dan y) dan kecepatan awal benda 2 (komponen x dan y) bernilai nol, maka tidak memungkinkan kedua benda bertumbukan
                messagebox.showerror('Error', 'Kedua benda diam dan tidak akan '    
                                     'bertumbukan.', parent=kecepatan_2dimensi)
                return
            
            if v1x_awal == v2x_awal and v1y_awal == v2y_awal:
                # Memberikan pesan error jika input data kecepatan awal benda 1 (komponen x dan y) dan kecepatan awal benda 2 (komponen x dan y) bernilai sama besar, maka tidak memungkinkan kedua benda bertumbukan                       
                messagebox.showerror('Error', 'Kedua benda memiliki kecepatan '
                                     'awal yang sama dan tidak akan bertumbukan.', 
                                     parent=kecepatan_2dimensi)
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
                                 parent=kecepatan_2dimensi)
            return
            
        except:
            # Memberikan pesan error jika terjadi error selain error yang telah didefinisikan sebelumnya
            messagebox.showerror('Error', 'Terjadi error.',                     
                                 parent=kecepatan_2dimensi)
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
            # Memunculkan output jenis tumbukan tidak dapat ditentukan jika terdapat input yang tidak sesuai
            text_jenistumbukan.config(state='normal')
            text_jenistumbukan.delete(1.0, 'end')
            text_jenistumbukan.insert(1.0, 'tidak dapat ditentukan')
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
        
        # Set-up window
        kecepatan_1dimensi = tk.Toplevel()
        kecepatan_1dimensi.resizable(width=False, height=False)
        
        # Menampilkan judul menggunakan fungsi Label
        judul1_kecepatan_1dimensi = ttk.Label(kecepatan_1dimensi, text='Menentukan '
                                              'Kecepatan Akhir', font=('Helvetica', 20))
        judul1_kecepatan_1dimensi.grid(row=0, column=0, columnspan=2, sticky='n', pady=10)
        judul2_kecepatan_1dimensi = ttk.Label(kecepatan_1dimensi, text='1 Dimensi', 
                                              font=('Helvetica', 20))
        judul2_kecepatan_1dimensi.grid(row=1, column=0, columnspan=2, sticky='n')
        
        # Membuat frame benda 1 menggunakan fungsi LabelFrame
        frame_benda1 = ttk.LabelFrame(kecepatan_1dimensi, text='Benda 1 Sebelum Tumbukan')
        frame_benda1.grid(row=2, column=0,ipadx=5, ipady=5, padx=(20,10), pady=10)
        
        # Isi dari frame benda 1
        # Frame 1 : Massa
        label_massa1 = ttk.Label(frame_benda1, text='Massa')                            # Membuat Label massa
        label_massa1.grid(row=0, column=0, sticky='w')
        titikdua = ttk.Label(frame_benda1, text=' : ')                                  # Membuat Label titik dua
        titikdua.grid(row=0, column=1)
        entry_massa1 = ttk.Entry(frame_benda1)                                          # Menggunakan fungsi Entry untuk menerima input massa benda 1
        entry_massa1.grid(row=0, column=2)
        label_unitmassa1 = ttk.Label(frame_benda1, text=' kg')
        label_unitmassa1.grid(row=0, column=3, sticky='W')
        
        # Frame 1 : Kecepatan awal
        label_v1awal = ttk.Label(frame_benda1, text='Kecepatan sebelum tumbukan')       # Membuat Label kecepatan awal
        label_v1awal.grid(row=1, column=0, sticky='w')
        titikdua = ttk.Label(frame_benda1, text=' : ')                                  # Membuat Label titik dua
        titikdua.grid(row=1, column=1)
        entry_v1awal = ttk.Entry(frame_benda1)                                          # Menggunakan fungsi Entry untuk menerima input kecepatan awal
        entry_v1awal.grid(row=1, column=2)
        label_unitv1awal = ttk.Label(frame_benda1, text=' m/s')
        label_unitv1awal.grid(row=1, column=3, sticky='W')
        
        # Membuat frame benda 2 menggunakan fungsi LabelFrame
        frame_benda2 = ttk.LabelFrame(kecepatan_1dimensi, text='Benda 2 Sebelum Tumbukan')
        frame_benda2.grid(row=2, column=1,ipadx=5, ipady=5, padx=(10,20), pady=10)
        
        # Isi dari frame benda 2
        # Frame 2 : Massa
        label_massa2 = ttk.Label(frame_benda2, text='Massa')                            # Membuat Label massa
        label_massa2.grid(row=0, column=0, sticky='w')
        titikdua = ttk.Label(frame_benda2, text=' : ')                                  # Membuat Label titik dua
        titikdua.grid(row=0, column=1)
        entry_massa2 = ttk.Entry(frame_benda2)                                          # Menggunakan fungsi Entry untuk menerima input massa benda 2
        entry_massa2.grid(row=0, column=2)
        label_unitmassa2 = ttk.Label(frame_benda2, text=' kg')
        label_unitmassa2.grid(row=0, column=3, sticky='W')

        # Frame 2 : Kecepatan awal
        label_v2awal = ttk.Label(frame_benda2, text='Kecepatan sebelum tumbukan')       # Membuat Label kecepatan awal
        label_v2awal.grid(row=1, column=0, sticky='w')
        titikdua = ttk.Label(frame_benda2, text=' : ')                                  # Membuat Label titik dua
        titikdua.grid(row=1, column=1)
        entry_v2awal = ttk.Entry(frame_benda2)                                          # Menggunakan fungsi Entry untuk menerima input kecepatan awal
        entry_v2awal.grid(row=1, column=2)
        label_unitv2awal = ttk.Label(frame_benda2, text=' m/s')
        label_unitv2awal.grid(row=1, column=3, sticky='W')
        
        # Membuat frame koefisien restitusi menggunakan Labelframe
        frame_restitusi = ttk.LabelFrame(kecepatan_1dimensi, text='Koefisien Restitusi')
        frame_restitusi.grid(row=3, columnspan=2,ipadx=5, ipady=5, padx=(10,20))
        
        # Isi dari frame koefisien restitusi
        label_restitusi = ttk.Label(frame_restitusi, text='Nilai koefisien restitusi')  # Membuat Label nilai koefisien restitusi
        label_restitusi.grid(row=0, column=0, sticky='w')
        titikdua = ttk.Label(frame_restitusi, text=' : ')                               # Membuat Label titik dua
        titikdua.grid(row=0, column=1)
        entry_restitusi = ttk.Entry(frame_restitusi)                                    # Menggunakan fungsi Entry untuk menerima input nilai koefisien restitusi
        entry_restitusi.grid(row=0, column=2)
        
        # Membuat Label catatan keakuratan
        note_input = ttk.Label(kecepatan_1dimensi, text='Catatan: Untuk hasil yang '    # Menampilkan catatan untuk pengguna dengan fungsi Label
                               'akurat, masukkan nilai hingga 4 angka desimal '
                               'di belakang koma.', font=('Segoe UI', 7))
        note_input.grid(row=4, columnspan=2, padx=10, pady=(0,10))
        
        # Membuat Button/tombol 'Jalankan Program!' dan Label tampilan hasil
        button_jalankan = ttk.Button(kecepatan_1dimensi, text='Jalankan Program!',      # Membuat Button/tombol 'Jalankan Program!' dan Label tampilan hasil
                                     command=vakhir_satudimensi)
        button_jalankan.grid(row=5, columnspan=2, padx=10, pady=10)
        
        # Membuat frame hasil menggunakan fungsi LabelFrame
        frame_hasil = ttk.LabelFrame(kecepatan_1dimensi, text='Hasil')
        frame_hasil.grid(row=6, columnspan=2,ipadx=5, ipady=5, padx=10, pady=(10,0))
        
        # Isi frame hasil
        # Frame hasil : Momentum sistem
        label_momentum = ttk.Label(frame_hasil, text='Besar momentum sistem')           # Membuat Label momentum sistem
        label_momentum.grid(row=0, column=0, sticky='w')
        titikdua = ttk.Label(frame_hasil, text=' : ')                                   # Membuat Label titik dua
        titikdua.grid(row=0, column=1)
        text_momentum = tk.Text(frame_hasil, height=1, width=25)                        # Membuat Text momentum sistem
        text_momentum.grid(row=0, column=2)
        text_momentum.insert(1.0, '0.0')
        text_momentum.tag_config('right', justify='right')
        text_momentum.tag_add('right',1.0,'end')
        text_momentum.config(state='disabled')
        label_unitmomentum = ttk.Label(frame_hasil, text=' kg.m/s')
        label_unitmomentum.grid(row=0, column=3, sticky='w')

        # Frame hasil : Kecepatan akhir benda 1
        label_v1akhir = ttk.Label(frame_hasil, text='Kecepatan akhir benda 1')      # Membuat Label kecepatan akhir benda 1
        label_v1akhir.grid(row=1,column=0, sticky='w')
        titikdua = ttk.Label(frame_hasil, text=' : ')                               # Membuat Label titik dua
        titikdua.grid(row=1, column=1)
        text_v1akhir = tk.Text(frame_hasil, height=1, width=25)                     # Membuat Text kecepatan akhir benda 1
        text_v1akhir.grid(row=1, column=2)
        text_v1akhir.insert(1.0, '0.0')
        text_v1akhir.tag_config('right', justify='right')
        text_v1akhir.tag_add('right',1.0,'end')
        text_v1akhir.config(state='disabled')
        label_unitv1akhir = ttk.Label(frame_hasil, text=' kg.m/s')
        label_unitv1akhir.grid(row=1, column=3, sticky='w')

        # Frame hasil : Kecepatan benda 2
        label_v2akhir = ttk.Label(frame_hasil, text='Kecepatan akhir benda 2')      # Membuat Label kecepatan akhir benda 2
        label_v2akhir.grid(row=2,column=0, sticky='w')
        titikdua = ttk.Label(frame_hasil, text=' : ')                               # Membuat Label titik dua 
        titikdua.grid(row=2, column=1)
        text_v2akhir = tk.Text(frame_hasil, height=1, width=25)                     # Membuat Text kecepatan akhir benda 2
        text_v2akhir.grid(row=2, column=2)
        text_v2akhir.insert(1.0, '0.0')
        text_v2akhir.tag_config('right', justify='right')
        text_v2akhir.tag_add('right',1.0,'end')
        text_v2akhir.config(state='disabled')
        label_unitv2akhir = ttk.Label(frame_hasil, text=' kg.m/s')
        label_unitv2akhir.grid(row=2, column=3, sticky='w')

        # Frame hasil : Energi kinetik sistem sebelum tumbukan
        label_ekawal = ttk.Label(frame_hasil, text='Besar energi kinetik sistem '   # Membuat Label energi kinetik sistem sebelum tumbukan
                                 'sebelum tumbukan')
        label_ekawal.grid(row=3,column=0, sticky='w')
        titikdua0 = ttk.Label(frame_hasil, text=' : ')                              # Membuat Label titik dua
        titikdua0.grid(row=3, column=1)
        text_ekawal = tk.Text(frame_hasil, height=1, width=25)                      # Membuat Text energi kinetik sistem sebelum tumbukan
        text_ekawal.grid(row=3, column=2)
        text_ekawal.insert(1.0, '0.0')
        text_ekawal.tag_config('right', justify='right')
        text_ekawal.tag_add('right',1.0,'end')
        text_ekawal.config(state='disabled')
        label_unitekawal = ttk.Label(frame_hasil, text=' J')
        label_unitekawal.grid(row=3, column=3, sticky='w')
        
        # Frame hasil : Energi kinetik sistem setelah tumbukan
        label_ekakhir = ttk.Label(frame_hasil, text='Besar energi kinetik sistem '  # Membuat Label energi kinetik sistem setelah tumbukan
                                  'setelah tumbukan')
        label_ekakhir.grid(row=4,column=0, sticky='w')
        titikdua = ttk.Label(frame_hasil, text=' : ')                               # Membuat Label titik dua
        titikdua.grid(row=4, column=1)
        text_ekakhir = tk.Text(frame_hasil, height=1, width=25)                     # Membuat Text energi kinetik sistem setelah tumbukan
        text_ekakhir.grid(row=4, column=2)
        text_ekakhir.insert(1.0, '0.0')
        text_ekakhir.tag_config('right', justify='right')
        text_ekakhir.tag_add('right',1.0,'end')
        text_ekakhir.config(state='disabled')
        label_unitekakhir = ttk.Label(frame_hasil, text=' J')
        label_unitekakhir.grid(row=4, column=3, sticky='w')
        
        # Frame hasil : Jenis tumbukan
        label_jenistumbukan = ttk.Label(frame_hasil, text='Jenis tumbukan')     # Membuat Label jenis tumbukan
        label_jenistumbukan.grid(row=5, column=0, sticky='w')
        titikdua = ttk.Label(frame_hasil, text=' : ')                           # Membuat Label titik dua
        titikdua.grid(row=5, column=1)
        text_jenistumbukan = tk.Text(frame_hasil,height=1, width=25)            # Membuat Text jenis tumbukan
        text_jenistumbukan.grid(row=5, column=2)
        text_jenistumbukan.tag_config('right', justify='right')
        text_jenistumbukan.tag_add('right',1.0,'end')
        text_jenistumbukan.config(state='disabled')
        
        # Membuat Label catatan pembulatan
        note_hasil = ttk.Label(kecepatan_1dimensi, text='Catatan: Hasil dibulatkan '    # Menampilkan catatan untuk pengguna dengan fungsi Label
                               'hingga tiga angka di belakang koma.', 
                               font=('Segoe UI', 7))
        note_hasil.grid(row=7, columnspan=2, pady=(0,20))
        
    elif pilihandimensi =='2 Dimensi':   # Jika opsi yang dipilih adalah 2 dimensi
        
        def gantibenda(option_benda): # Mendefinisikan fungsi untuk mengubah label sesuai dengan benda yang dipilih
            
            if option_benda == 'Benda 1':
                label_vakhir.config(text='Kecepatan akhir benda 1')
                label_vakhirhasil.config(text='Kecepatan akhir benda 2')
            elif option_benda == 'Benda 2':
                label_vakhir.config(text='Kecepatan akhir benda 2')
                label_vakhirhasil.config(text='Kecepatan akhir benda 1')
        
        # Set-up window        
        kecepatan_2dimensi = tk.Toplevel()
        kecepatan_2dimensi.resizable(width=False, height=False)
        
        # Membuat array yang berisi pilihan dimensi yang bisa dipilih dan
        # menginisialisasi variabel nilai_pilihandimensi 
        benda = ['Benda 1', 'Benda 2']
        nilai_pilihanbenda = tk.StringVar()
        
        # Menampilkan judul menggunakan fungsi Label
        judul1_kecepatan_2dimensi = ttk.Label(kecepatan_2dimensi, text='Menentukan '
                                              'Kecepatan Akhir', font=('Helvetica', 20))
        judul1_kecepatan_2dimensi.grid(row=0, column=0, columnspan=2, sticky='n', pady=10)
        judul2_kecepatan_2dimensi = ttk.Label(kecepatan_2dimensi, text='2 Dimensi', 
                                              font=('Helvetica', 20))
        judul2_kecepatan_2dimensi.grid(row=1, column=0, columnspan=2, sticky='n')
        
        # Membuat frame benda 1 menggunakan LabelFrame
        frame_benda1 = ttk.LabelFrame(kecepatan_2dimensi, text='Benda 1 Sebelum Tumbukan')
        frame_benda1.grid(row=2, column=0,ipadx=5, ipady=5, padx=(20,10), pady=10)
        
        # Isi dari frame benda 1
        # Frame 1 : Massa
        label_massa1 = ttk.Label(frame_benda1, text='Massa')                            # Membuat Label massa
        label_massa1.grid(row=0, column=0, sticky='w')
        titikdua = ttk.Label(frame_benda1, text=' : ')                                  # Membuat Label titik dua
        titikdua.grid(row=0, column=1)
        entry_massa1 = ttk.Entry(frame_benda1)                                          # Menggunakan fungsi Entry untuk menerima input massa benda 1
        entry_massa1.grid(row=0, column=2)
        label_unitmassa1 = ttk.Label(frame_benda1, text=' kg')
        label_unitmassa1.grid(row=0, column=3, sticky='W')

        # Frame 1 : Kecepatan awal
        label_v1awal = ttk.Label(frame_benda1, text='Kecepatan sebelum tumbukan')       # Membuat Label kecepatan awal
        label_v1awal.grid(row=1, column=0, sticky='w')
        titikdua = ttk.Label(frame_benda1, text=' : ')                                  # Membuat Label titik dua
        titikdua.grid(row=1, column=1)
        entry_v1xawal = ttk.Entry(frame_benda1)                                         # Menggunakan fungsi Entry untuk menerima input kecepatan awal
        entry_v1xawal.grid(row=1, column=2)
        label_v1awalvektor1 = ttk.Label(frame_benda1,                                   # Komponen x
                                        text=' \N{LATIN SMALL LETTER I WITH CIRCUMFLEX}  + ')
        label_v1awalvektor1.grid(row=1, column=3)
        entry_v1yawal = ttk.Entry(frame_benda1)
        entry_v1yawal.grid(row=1,column=4)
        label_v1awalvektor2 = ttk.Label(frame_benda1,                                   # Komponen y
                                        text=' \N{LATIN SMALL LETTER J WITH CIRCUMFLEX}  m/s')
        label_v1awalvektor2.grid(row=1, column=5, sticky='W')
        
        # Membuat frame benda 2 menggunakan LabelFrame
        frame_benda2 = ttk.LabelFrame(kecepatan_2dimensi, text='Benda 2 Sebelum Tumbukan')
        frame_benda2.grid(row=2, column=1,ipadx=5, ipady=5, padx=(10,20), pady=10)
        
        # Isi dari frame benda 2
        # Frame 2 : Massa
        label_massa2 = ttk.Label(frame_benda2, text='Massa')                            # Membuat Label massa
        label_massa2.grid(row=0, column=0, sticky='w')
        titikdua = ttk.Label(frame_benda2, text=' : ')                                  # Membuta Label titik dua
        titikdua.grid(row=0, column=1)
        entry_massa2 = ttk.Entry(frame_benda2)                                          # Menggunakan fungsi Entry untuk menerima input massa benda 2
        entry_massa2.grid(row=0, column=2)
        label_unitmassa2 = ttk.Label(frame_benda2, text=' kg')
        label_unitmassa2.grid(row=0, column=3, sticky='W')

        # Frame 2 : Kecepatan awal
        label_v2awal = ttk.Label(frame_benda2, text='Kecepatan sebelum tumbukan')       # Membuat Label kecepatan awal
        label_v2awal.grid(row=1, column=0, sticky='w')
        titikdua = ttk.Label(frame_benda2, text=' : ')                                  # Membuat Label titik dua
        titikdua.grid(row=1, column=1)
        entry_v2xawal = ttk.Entry(frame_benda2)                                         # Menggunakan fungsi Entry untuk menerima input kecepatan awal
        entry_v2xawal.grid(row=1, column=2)
        label_v2awalvektor1 = ttk.Label(frame_benda2,                                   # Komponen x
                                        text=' \N{LATIN SMALL LETTER I WITH CIRCUMFLEX}  + ')
        label_v2awalvektor1.grid(row=1, column=3)
        entry_v2yawal = ttk.Entry(frame_benda2)
        entry_v2yawal.grid(row=1,column=4)
        label_v2awalvektor2 = ttk.Label(frame_benda2,                                   # Komponen y
                                        text=' \N{LATIN SMALL LETTER J WITH CIRCUMFLEX}  m/s')
        label_v2awalvektor2.grid(row=1, column=5, sticky='W')
        
        # Membuat frame kecepatan akhir untuk salah satu benda
        frame_vakhir = ttk.LabelFrame(kecepatan_2dimensi, text='Kecepatan Akhir Salah Satu Benda')
        frame_vakhir.grid(row=3, columnspan=2,ipadx=5, ipady=5, padx=(10,20))
        
        # Membuat frame opsi benda yang akan dipilih beserta isinya
        frame_pilihanbenda = ttk.Frame(frame_vakhir)
        frame_pilihanbenda.grid(row=0, columnspan=6)
        label_pilihanbenda = ttk.Label(frame_pilihanbenda, text='Pilih benda:', font=('Segoe UI', 8))
        label_pilihanbenda.grid(row=0, column=0, pady=5, sticky='e')
        ttk.Style().configure('Mini.TMenubutton',font=('Segoe UI', 8), padding=0)
        pilihanbenda = ttk.OptionMenu(frame_pilihanbenda, nilai_pilihanbenda, benda[0], *benda, 
                                      style='Mini.TMenubutton', command=gantibenda)
        pilihanbenda.grid(row=0, column=1, pady=5, sticky='w')
        
        # Membuat frame kecepatan akhir salah satu benda
        label_vakhir = ttk.Label(frame_vakhir, text='Kecepatan akhir benda 1')                  # Membuat Label kecepetan akhir benda 1
        label_vakhir.grid(row=1, column=0, sticky='w')
        titikdua = ttk.Label(frame_vakhir, text=' : ')                                          # Membuat Label titik dua
        titikdua.grid(row=1, column=1)
        entry_vxakhir = ttk.Entry(frame_vakhir)                                                 # Menggunakan fungsi Entry untuk menerima input kecepatan akhir
        entry_vxakhir.grid(row=1, column=2)
        label_vakhirvektor1 = ttk.Label(frame_vakhir,                                           # Komponen x
                                        text=' \N{LATIN SMALL LETTER I WITH CIRCUMFLEX}  + ')
        label_vakhirvektor1.grid(row=1, column=3)
        entry_vyakhir = ttk.Entry(frame_vakhir)
        entry_vyakhir.grid(row=1,column=4)
        label_vakhirvektor2 = ttk.Label(frame_vakhir,                                           # Komponen y
                                        text=' \N{LATIN SMALL LETTER J WITH CIRCUMFLEX}  m/s')
        label_vakhirvektor2.grid(row=1, column=5, sticky='W')
        
        # Membuat Label catatan keakuratan
        note_input = ttk.Label(kecepatan_2dimensi, text='Catatan: Untuk hasil yang akurat, '    # Menampilkan catatan untuk pengguna dengan fungsi Label
                               'masukkan nilai hingga 4 angka desimal di belakang koma.', 
                               font=('Segoe UI', 7))
        note_input.grid(row=4, columnspan=2, padx=10, pady=(0,10))
        
        # Membuat Button/tombol 'Jalankan Program!'
        button_jalankan = ttk.Button(kecepatan_2dimensi, text='Jalankan Program!',              # Membuat Button/tombol 'Jalankan Program!' dan Label tampilan hasil
                                     command=vakhir_duadimensi)
        button_jalankan.grid(row=5, columnspan=2, padx=10, pady=10)
        
        # Membuat frame hasil menggunakan fungsi LabelFrame
        frame_hasil = ttk.LabelFrame(kecepatan_2dimensi, text='Hasil')
        frame_hasil.grid(row=6, columnspan=2,ipadx=5, ipady=5, padx=10, pady=(10,0))
        
        # Isi frame hasil
        # Frame hasil : Momentum sistem
        label_momentum = ttk.Label(frame_hasil, text='Besar momentum sistem')           # Membuat Label momentum sistem
        label_momentum.grid(row=0, column=0, sticky='w')
        titikdua = ttk.Label(frame_hasil, text=' : ')                                   # Membuat Label titik dua
        titikdua.grid(row=0, column=1)
        text_momentumx = tk.Text(frame_hasil, height=1, width=25)                       # Membuat Text momentum sistem
        text_momentumx.grid(row=0, column=2)
        text_momentumx.insert(1.0, '0.0')
        text_momentumx.tag_config('right', justify='right')
        text_momentumx.tag_add('right',1.0,'end')
        text_momentumx.config(state='disabled')
        label_momentumvektor1 = ttk.Label(frame_hasil,                                  # Komponen x
                                          text=' \N{LATIN SMALL LETTER I WITH CIRCUMFLEX}  + ')
        label_momentumvektor1.grid(row=0, column=3)
        text_momentumy = tk.Text(frame_hasil, height=1, width=25)
        text_momentumy.grid(row=0, column=4)
        text_momentumy.insert(1.0, '0.0')
        text_momentumy.tag_config('right', justify='right')
        text_momentumy.tag_add('right',1.0,'end')
        text_momentumy.config(state='disabled')
        label_momentumvektor2 = ttk.Label(frame_hasil,                                  # Komponen y
                                          text=' \N{LATIN SMALL LETTER J WITH CIRCUMFLEX}  kg.m/s')
        label_momentumvektor2.grid(row=0, column=5, sticky='w')

        # Frame hasil : Kecepatan akhir benda selain yang dipilih
        label_vakhirhasil = ttk.Label(frame_hasil, text='Kecepatan akhir benda 2')  # Membuat Label kecepatan akhir benda
        label_vakhirhasil.grid(row=1,column=0, sticky='w')
        titikdua = ttk.Label(frame_hasil, text=' : ')                               # Membuat Label titik dua
        titikdua.grid(row=1, column=1)
        text_vxakhirhasil = tk.Text(frame_hasil, height=1, width=25)                # Membuat Text kecepatan akhir benda 
        text_vxakhirhasil.grid(row=1, column=2)
        text_vxakhirhasil.insert(1.0, '0.0')
        text_vxakhirhasil.tag_config('right', justify='right')
        text_vxakhirhasil.tag_add('right',1.0,'end')
        text_vxakhirhasil.config(state='disabled')
        label_vakhirhasilvektor1 = ttk.Label(frame_hasil,                           # Komponen x
                                             text=' \N{LATIN SMALL LETTER I WITH CIRCUMFLEX}  + ')
        label_vakhirhasilvektor1.grid(row=1, column=3, sticky='w')
        text_vyakhirhasil = tk.Text(frame_hasil, height=1, width=25)
        text_vyakhirhasil.grid(row=1, column=4)
        text_vyakhirhasil.insert(1.0, '0.0')
        text_vyakhirhasil.tag_config('right', justify='right')
        text_vyakhirhasil.tag_add('right',1.0,'end')
        text_vyakhirhasil.config(state='disabled')
        label_vakhirhasilvektor2 = ttk.Label(frame_hasil,text=                      # Komponen y
                                             ' \N{LATIN SMALL LETTER J WITH CIRCUMFLEX}  m/s')
        label_vakhirhasilvektor2.grid(row=1, column=5, sticky='w')

        # Frame hasil : Energi kinetik sistem awal
        label_ekawal = ttk.Label(frame_hasil, text='Besar energi kinetik sistem '   # Membuat Label energi kinetik sistem sebelum tumbukan
                                 'sebelum tumbukan')
        label_ekawal.grid(row=2,column=0, sticky='w')
        titikdua0 = ttk.Label(frame_hasil, text=' : ')                              # Membuat Label titik dua
        titikdua0.grid(row=2, column=1)
        text_ekawal = tk.Text(frame_hasil, height=1, width=25)                      # Membuat Text energi kinetik sistem sebelum tumbukan
        text_ekawal.grid(row=2, column=2)
        text_ekawal.insert(1.0, '0.0')
        text_ekawal.tag_config('right', justify='right')
        text_ekawal.tag_add('right',1.0,'end')
        text_ekawal.config(state='disabled')
        label_unitekawal = ttk.Label(frame_hasil, text=' J')
        label_unitekawal.grid(row=2, column=3, sticky='w')

        # Frame hasil : Energi kinetik sistem akhir
        label_ekakhir = ttk.Label(frame_hasil, text='Besar energi kinetik '         # Membuat Label energi kinetik sistem setelah tumbukan
                                  'sistem setelah tumbukan')
        label_ekakhir.grid(row=3,column=0, sticky='w')                              
        titikdua = ttk.Label(frame_hasil, text=' : ')                               # Membuat Label titik dua
        titikdua.grid(row=3, column=1)
        text_ekakhir = tk.Text(frame_hasil, height=1, width=25)                     # Membuat Text energi kinetik sistem setelah tumbukan
        text_ekakhir.grid(row=3, column=2)
        text_ekakhir.insert(1.0, '0.0')
        text_ekakhir.tag_config('right', justify='right')
        text_ekakhir.tag_add('right',1.0,'end')
        text_ekakhir.config(state='disabled')
        label_unitekakhir = ttk.Label(frame_hasil, text=' J')
        label_unitekakhir.grid(row=3, column=3, sticky='w')

        # Frame hasil : Jenis tumbukan
        label_jenistumbukan = ttk.Label(frame_hasil, text='Jenis tumbukan')         # Membuat Label jenis tumbukan
        label_jenistumbukan.grid(row=4, column=0, sticky='w')
        titikdua = ttk.Label(frame_hasil, text=' : ')                               # Membuat Label titik dua
        titikdua.grid(row=4, column=1)
        text_jenistumbukan = tk.Text(frame_hasil,height=1, width=25)                # Membuat Text jenis tumbukan
        text_jenistumbukan.grid(row=4, column=2)
        text_jenistumbukan.tag_config('right', justify='right')
        text_jenistumbukan.tag_add('right',1.0,'end')
        text_jenistumbukan.config(state='disabled')
        
        # Membuat Label catatan pembulatan
        note_hasil = ttk.Label(kecepatan_2dimensi, text='Catatan: Hasil dibulatkan '    # Menampilkan catatan untuk pengguna dengan fungsi Label
                               'hingga tiga angka di belakang koma.', 
                               font=('Segoe UI', 7))
        note_hasil.grid(row=7, columnspan=2, pady=(0,20))