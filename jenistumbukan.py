# Tugas Besar Kelompok 3
# PROGRAM    : Subprogram Menentukan Jenis Tumbukan
# DESKRIPSI  : Program yang dapat menentukan jenis tumbukan dalam 1 dimensi 
#              & 2 dimensi berdasarkan data yang diinput oleh pengguna.

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
from tkinter import ttk
from tkinter import messagebox

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
                                     parent=jenis_1dimensi)
                return
            
            if v1_awal == 0 and v2_awal == 0:                                       # Memunculkan messagebox Error jika kecepatan awal kedua benda nol
                messagebox.showerror('Error', 
                                     'Kedua benda diam dan tidak akan bertumbukan.', 
                                     parent=jenis_1dimensi)
                return
            
            if v1_awal == v2_awal:                                                  # Memunculkan messagebox Error jika kecepatan awal kedua benda sama
                messagebox.showerror('Error', 
                                     'Kedua benda memiliki kecepatan awal yang sama '
                                     'dan tidak akan bertumbukan.', 
                                     parent=jenis_1dimensi)
                return
                
            momentum_awal = round(m1*v1_awal + m2*v2_awal, 3)                       # Rumus perhitungan untuk menentukan momentum awal
            momentum_akhir = round(m1*v1_akhir + m2*v2_akhir,3)                     # Rumus perhitungan untuk menentukan momentum akhir
            restitusi = round((v1_akhir-v2_akhir)/(v2_awal-v1_awal), 3)             # Rumus perhitungan untuk menentukan koefisien restitusi
            ek_awal = round((1/2)*m1*(v1_awal**2)+(1/2)*m2*(v2_awal**2), 3)         # Rumus perhitungan untuk menentukan energi kinetik awal sistem
            ek_akhir = round((1/2)*m1*(v1_akhir**2)+(1/2)*m2*(v2_akhir**2), 3)      # Rumus perhitungan untuk menentukan energi kinetik akhir sistem
            
        except ValueError:
            # Memberikan pesan error jika nilai yang diinput bukan merupakan bilangan real
            messagebox.showerror('Error', 'Masukkan bilangan real.',                
                             parent=jenis_1dimensi)
            return
            
        except:
            # Memberikan pesan error jika terjadi error selain error yang telah didefinisikan sebelumnya
            messagebox.showerror('Error', 'Terjadi error.', parent=jenis_1dimensi)  
            return
            
        if momentum_awal != momentum_akhir:
            # Ketika input tidak sesuai dengan Hukum Kekekalan Momentum, maka jenis tumbukan tidak dapat ditentukan
            messagebox.showwarning('Peringatan',
                                   'Nilai yang anda masukkan tidak sesuai dengan '
                                   'Hukum Kekekalan Momentum, sehingga jenis '
                                   'tumbukan tidak dapat ditentukan.', 
                                   parent=jenis_1dimensi)
            text_jenistumbukan.config(state='normal')
            text_jenistumbukan.delete(1.0, 'end')
            text_jenistumbukan.insert(1.0, 'tidak dapat ditentukan')
            text_jenistumbukan.tag_add('right', 1.0, 'end')
            text_jenistumbukan.config(state='disabled')
            
        elif restitusi == 0:    
            # Memunculkan output jenis tumbukan 'inelastis sempurna' jika koefisien restitusi bernilai 0
            text_jenistumbukan.config(state='normal')
            text_jenistumbukan.delete(1.0, 'end')
            text_jenistumbukan.insert(1.0, 'inelastis sempurna')
            text_jenistumbukan.tag_add('right', 1.0, 'end')
            text_jenistumbukan.config(state='disabled')
      
        elif restitusi > 0 and restitusi < 1:   
            # Memunculkan output jenis tumbukan 'elastis sebagian' jika koefisien restitusi bernilai 0<e<1
            text_jenistumbukan.config(state='normal')
            text_jenistumbukan.delete(1.0, 'end')
            text_jenistumbukan.insert(1.0, 'elastis sebagian')
            text_jenistumbukan.tag_add('right', 1.0, 'end')
            text_jenistumbukan.config(state='disabled')
    
        elif restitusi == 1:    
            # Memunculkan output jenis tumbukan 'elastis sempurna' jika koefisien restitusi bernilai 1
            text_jenistumbukan.config(state='normal')
            text_jenistumbukan.delete(1.0, 'end')
            text_jenistumbukan.insert(1.0, 'elastis sempurna')
            text_jenistumbukan.tag_add('right', 1.0, 'end')
            text_jenistumbukan.config(state='disabled')
       
        elif restitusi > 1:     
            # Memunculkan output jenis tumbukan 'superelastis' jika koefisien restitusi bernilai >1
            text_jenistumbukan.config(state='normal')
            text_jenistumbukan.delete(1.0, 'end')
            text_jenistumbukan.insert(1.0, 'superelastis')
            text_jenistumbukan.tag_add('right', 1.0, 'end')
            text_jenistumbukan.config(state='disabled')
       
        else:   
            # Memunculkan output jenis tumbukan 'tidak dapat ditentukan' jika koefisien restitusi bernilai <0
            text_jenistumbukan.config(state='normal')
            text_jenistumbukan.delete(1.0, 'end')
            text_jenistumbukan.insert(1.0, 'tidak dapat ditentukan')
            text_jenistumbukan.tag_add('right', 1.0, 'end')
            text_jenistumbukan.config(state='disabled')
        
        # Memunculkan output koefisien restitusi
        text_restitusi.config(state='normal')                                           
        text_restitusi.delete(1.0, 'end')
        text_restitusi.insert(1.0, f'{restitusi}')
        text_restitusi.tag_add('right', 1.0, 'end')
        text_restitusi.config(state='disabled')
    
        # Memunculkan output momentum sistem sebelum tumbukan
        text_momentumawal.config(state='normal')                                        
        text_momentumawal.delete(1.0, 'end')
        text_momentumawal.insert(1.0, f'{momentum_awal}')
        text_momentumawal.tag_add('right', 1.0, 'end')
        text_momentumawal.config(state='disabled')
        
        # Memunculkan output momentum sistem setelah tumbukan
        text_momentumakhir.config(state='normal')                                       
        text_momentumakhir.delete(1.0, 'end')
        text_momentumakhir.insert(1.0, f'{momentum_akhir}')
        text_momentumakhir.tag_add('right', 1.0, 'end')
        text_momentumakhir.config(state='disabled')
        
        # Memunculkan output energi sistem kinetik sebelum tumbukan
        text_ekawal.config(state='normal')                                              
        text_ekawal.delete(1.0, 'end')
        text_ekawal.insert(1.0, f'{ek_awal}')
        text_ekawal.tag_add('right', 1.0, 'end')
        text_ekawal.config(state='disabled')
        
        # Memunculkan output energi sistem kinetik setelah tumbukan
        text_ekakhir.config(state='normal') 
        text_ekakhir.delete(1.0, 'end')                                            
        text_ekakhir.insert(1.0, f'{ek_akhir}')
        text_ekakhir.tag_add('right', 1.0, 'end')
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
                                     parent=jenis_2dimensi)
                return
        
            if v1x_awal == 0 and v1y_awal == 0 and v2x_awal == 0 and v2y_awal == 0: 
                # Memunculkan messagebox Error jika kecepatan awal kedua benda di sumbu X dan Y bernilai nol
                messagebox.showerror('Error', 'Kedua benda diam dan tidak akan '
                                     'bertumbukan.', parent=jenis_2dimensi)
                return
            
            if v1x_awal == v2x_awal and v1y_awal == v2y_awal:                                   
                # Memunculkan messagebox Error jika kecepatan awal kedua benda di sumbu X dan Y bernilai sama
                messagebox.showerror('Error', 'Kedua benda memiliki kecepatan '
                                     'awal yang sama dan tidak akan bertumbukan.', 
                                     parent=jenis_2dimensi)
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
                                 parent=jenis_2dimensi)
            return
            
        except:
            # Memberikan pesan error jika terjadi error selain error yang telah didefinisikan sebelumnya
            messagebox.showerror('Error', 'Terjadi error.', parent=jenis_2dimensi)              
            return

        if momentumx_awal != momentumx_akhir or momentumy_awal != momentumy_akhir:              
            # Ketika input tidak sesuai dengan Hukum Kekekalan Momentum, maka jenis tumbukan tidak dapat ditentukan
            messagebox.showwarning('Peringatan', 'Nilai yang anda masukkan tidak '              
                                   'sesuai dengan Hukum Kekekalan Momentum, '
                                   'sehingga jenis tumbukan tidak dapat ditentukan.', 
                                   parent=jenis_2dimensi)
            text_jenistumbukan.config(state='normal')
            text_jenistumbukan.delete(1.0, 'end')
            text_jenistumbukan.insert(1.0, 'tidak dapat ditentukan')
            text_jenistumbukan.tag_add('right', 1.0, 'end')
            text_jenistumbukan.config(state='disabled')
            
        elif v1x_akhir == v2x_akhir and v1y_akhir == v2y_akhir:                                 
            # Memunculkan output jenis tumbukan 'inelastis sempurna' jika kecepatan akhir kedua benda di sumbu X dan Y bernilai sama
            text_jenistumbukan.config(state='normal')                                           
            text_jenistumbukan.delete(1.0, 'end')
            text_jenistumbukan.insert(1.0, 'inelastis sempurna')
            text_jenistumbukan.tag_add('right', 1.0, 'end')
            text_jenistumbukan.config(state='disabled')
        
        elif ek_awal == ek_akhir:                                                               
            # Memunculkan output jenis tumbukan 'elastis sempurna' jika energi kinetik awal dan akhir bernilai sama
            text_jenistumbukan.config(state='normal')                                           
            text_jenistumbukan.delete(1.0, 'end')
            text_jenistumbukan.insert(1.0, 'elastis sempurna')
            text_jenistumbukan.tag_add('right', 1.0, 'end')
            text_jenistumbukan.config(state='disabled')
    
        elif ek_awal > ek_akhir:                                                               
            # Memunculkan output jenis tumbukan 'elastis sebagian' jika energi kinetik awal lebih besar dari energi kinetik akhir
            text_jenistumbukan.config(state='normal')
            text_jenistumbukan.delete(1.0, 'end')
            text_jenistumbukan.insert(1.0, 'elastis sebagian')
            text_jenistumbukan.tag_add('right', 1.0, 'end')
            text_jenistumbukan.config(state='disabled')
       
        elif ek_awal < ek_akhir:                                                                
            # Memunculkan output jenis tumbukan 'superelastis' jika energi kinetik awal lebih kecil dari energi kinetik akhir
            text_jenistumbukan.config(state='normal')                                           
            text_jenistumbukan.delete(1.0, 'end')
            text_jenistumbukan.insert(1.0, 'superelastis')
            text_jenistumbukan.tag_add('right', 1.0, 'end')
            text_jenistumbukan.config(state='disabled')
       
        else:                                                                                   
            # Memunculkan output jenis tumbukan 'tidak dapat ditentukan' jika terjadi kasus diluar yang telah disebutkan
            text_jenistumbukan.config(state='normal')
            text_jenistumbukan.delete(1.0, 'end')
            text_jenistumbukan.insert(1.0, 'tidak dapat ditentukan')
            text_jenistumbukan.tag_add('right', 1.0, 'end')
            text_jenistumbukan.config(state='disabled')
            
        # Memunculkan output momentum awal di sumbu-X
        text_momentumxawal.config(state='normal')                                               
        text_momentumxawal.delete(1.0, 'end')
        text_momentumxawal.insert(1.0, f'{momentumx_awal}')
        text_momentumxawal.tag_add('right', 1.0, 'end')
        text_momentumxawal.config(state='disabled')
        
        # Memunculkan output momentum awal di sumbu-Y
        text_momentumyawal.config(state='normal')                                              
        text_momentumyawal.delete(1.0, 'end')
        text_momentumyawal.insert(1.0, f'{momentumy_awal}')
        text_momentumyawal.tag_add('right', 1.0, 'end')
        text_momentumyawal.config(state='disabled')
        
        # Memunculkan output momentum akhir di sumbu-X
        text_momentumxakhir.config(state='normal')                                              
        text_momentumxakhir.delete(1.0, 'end')
        text_momentumxakhir.insert(1.0, f'{momentumx_akhir}')
        text_momentumxakhir.tag_add('right', 1.0, 'end')
        text_momentumxakhir.config(state='disabled')
        
        # Memunculkan output momentum akhir di sumbu-Y
        text_momentumyakhir.config(state='normal')                                              
        text_momentumyakhir.delete(1.0, 'end')
        text_momentumyakhir.insert(1.0, f'{momentumy_akhir}')
        text_momentumyakhir.tag_add('right', 1.0, 'end')
        text_momentumyakhir.config(state='disabled')
        
        # Memunculkan output energi kinetik awal
        text_ekawal.config(state='normal')                                                      
        text_ekawal.delete(1.0, 'end')
        text_ekawal.insert(1.0, f'{ek_awal}')
        text_ekawal.tag_add('right', 1.0, 'end')
        text_ekawal.config(state='disabled')
        
        # Memunculkan output energi kinetik akhir
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
        jenis_1dimensi = tk.Toplevel()
        jenis_1dimensi.resizable(width=False, height=False)

        # Menampilkan judul menggunakan fungsi Label
        judul1_jenis_1dimensi = ttk.Label(jenis_1dimensi, text='Menentukan Jenis Tumbukan', font=('Helvetica', 20))
        judul1_jenis_1dimensi.grid(row=0, column=0, columnspan=2, sticky='n', pady=10)
        judul2_jenis_1dimensi = ttk.Label(jenis_1dimensi, text='1 Dimensi', font=('Helvetica', 20))
        judul2_jenis_1dimensi.grid(row=1, column=0, columnspan=2, sticky='n')

        # Membuat frame benda 1 menggunakan fungsi LabelFrame
        frame_benda1 = ttk.LabelFrame(jenis_1dimensi, text='Benda 1')
        frame_benda1.grid(row=2, column=0,ipadx=5, ipady=5, padx=(20,10), pady=(10,0))
        
        # Isi dari frame benda 1
        # Frame 1 : Massa
        label_massa1 = ttk.Label(frame_benda1, text='Massa')                            # Membuat Label massa
        label_massa1.grid(row=0, column=0, sticky='w')
        titikdua = ttk.Label(frame_benda1, text=' : ')                                  # Membuat Label titik dua
        titikdua.grid(row=0, column=1)
        entry_massa1 = ttk.Entry(frame_benda1)                                          # Menggunakan fungsi entry untuk menerima input massa benda
        entry_massa1.grid(row=0, column=2)
        label_unitmassa1 = ttk.Label(frame_benda1, text=' kg')
        label_unitmassa1.grid(row=0, column=3, sticky='W')
        
        # Frame 1: Kecepatan awal
        label_v1awal = ttk.Label(frame_benda1, text='Kecepatan sebelum tumbukan')       # Membuat Label kecepatan awal
        label_v1awal.grid(row=1, column=0, sticky='w')
        titikdua = ttk.Label(frame_benda1, text=' : ')                                  # Membuat Label titik dua
        titikdua.grid(row=1, column=1)
        entry_v1awal = ttk.Entry(frame_benda1)                                          # Menggunakan fungsi Entry untuk menerima input kecepatan awal
        entry_v1awal.grid(row=1, column=2)
        label_unitv1awal = ttk.Label(frame_benda1, text=' m/s')
        label_unitv1awal.grid(row=1, column=3, sticky='W')
        
        # Frame 1: Kecepatan akhir
        label_v1akhir = ttk.Label(frame_benda1, text='Kecepatan setelah tumbukan')      # Membuat Label kecepatan akhir
        label_v1akhir.grid(row=2, column=0, sticky='w')
        titikdua = ttk.Label(frame_benda1, text=' : ')                                  # Membuat Label titik dua
        titikdua.grid(row=2, column=1)
        entry_v1akhir = ttk.Entry(frame_benda1)                                         # Menggunakan fungsi Entry untuk menerima input kecepatan akhir
        entry_v1akhir.grid(row=2, column=2)
        label_unitv1akhir = ttk.Label(frame_benda1, text=' m/s')
        label_unitv1akhir.grid(row=2, column=3, sticky='W')

        # Membuat frame benda 2 menggunakan fungsi LabelFrame
        frame_benda2 = ttk.LabelFrame(jenis_1dimensi, text='Benda 2')
        frame_benda2.grid(row=2, column=1,ipadx=5, ipady=5, padx=(10,20), pady=(10,0))
        
        # Isi dari frame benda 2
        # Frame 2 : Massa
        label_massa2 = ttk.Label(frame_benda2, text='Massa')                            # Membuat Label massa
        label_massa2.grid(row=0, column=0, sticky='w')
        titikdua = ttk.Label(frame_benda2, text=' : ')                                  # Membuat Label titik dua
        titikdua.grid(row=0, column=1)
        entry_massa2 = ttk.Entry(frame_benda2)                                          # Menggunakan fungsi Entry untuk menerima input massa benda
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
        
        # Frame 2 : Kecepatan akhir
        label_v2akhir = ttk.Label(frame_benda2, text='Kecepatan setelah tumbukan')      # Membuat Label kecepatan akhir
        label_v2akhir.grid(row=2, column=0, sticky='w')
        titikdua = ttk.Label(frame_benda2, text=' : ')                                  # Membuat Label titik dua
        titikdua.grid(row=2, column=1)
        entry_v2akhir = ttk.Entry(frame_benda2)                                         # Menggunakan fungsi Entry untuk menerima input kecepatan akhir
        entry_v2akhir.grid(row=2, column=2)
        label_unitv2akhir = ttk.Label(frame_benda2, text=' m/s')
        label_unitv2akhir.grid(row=2, column=3, sticky='W')
        
        # Membuat Label catatan keakuratan
        note_input = ttk.Label(jenis_1dimensi, text='Catatan: Untuk hasil yang '        # Menampilkan catatan untuk pengguna menggunakan fungsi Label
                               'akurat, masukkan nilai hingga 4 angka desimal '
                               'di belakang koma.', font=('Segoe UI', 7))
        note_input.grid(row=3, columnspan=2, padx=10, pady=(0,10))
        
        # Membuat Button/tombol 'Jalankan Program!'  
        button_jalankan = ttk.Button(jenis_1dimensi, text='Jalankan Program!',
                                     command=jenistumbukan_satudimensi)
        button_jalankan.grid(row=4, columnspan=2, padx=10, pady=10)
        
        # Membuat frame hasil menggunakan fungsi LabelFrame
        frame_hasil = ttk.LabelFrame(jenis_1dimensi, text='Hasil')
        frame_hasil.grid(row=5, columnspan=2,ipadx=5, ipady=5, padx=10, pady=(10,0))
        
        # Isi frame hasil
        
        # Frame hasil : Momentum awal
        label_momentumawal = ttk.Label(frame_hasil, text='Besar momentum sistem '       # Membuat Label momentum awal sistem
                                       'sebelum tumbukan')
        label_momentumawal.grid(row=0, column=0, sticky='w')
        titikdua = ttk.Label(frame_hasil, text=' : ')                                   # Membuat Label titik dua
        titikdua.grid(row=0, column=1)
        text_momentumawal = tk.Text(frame_hasil, height=1, width=25)                    # Membuat Text momentum awal sistem
        text_momentumawal.grid(row=0, column=2)
        text_momentumawal.insert(1.0, '0.0')
        text_momentumawal.tag_config('right', justify='right')
        text_momentumawal.tag_add('right',1.0,'end')
        text_momentumawal.config(state='disabled')
        label_unitmomentumawal = ttk.Label(frame_hasil, text=' kg.m/s')
        label_unitmomentumawal.grid(row=0, column=3, sticky='w')
        
        # Frame hasil : Momentum akhir
        label_momentumakhir = ttk.Label(frame_hasil, text='Besar momentum sistem '      # Membuat Label momentum akhir sistem
                                        'setelah tumbukan')
        label_momentumakhir.grid(row=1,column=0, sticky='w')
        titikdua = ttk.Label(frame_hasil, text=' : ')                                   # Membuat Label titik dua
        titikdua.grid(row=1, column=1)
        text_momentumakhir = tk.Text(frame_hasil, height=1, width=25)                   # Membuat Text momentum akhir sistem
        text_momentumakhir.grid(row=1, column=2)
        text_momentumakhir.insert(1.0, '0.0')
        text_momentumakhir.tag_config('right', justify='right')
        text_momentumakhir.tag_add('right',1.0,'end')
        text_momentumakhir.config(state='disabled')
        label_unitmomentumakhir = ttk.Label(frame_hasil, text=' kg.m/s')
        label_unitmomentumakhir.grid(row=1, column=3, sticky='w')
        
        # Frame hasil : Energi kinetik awal
        label_ekawal = ttk.Label(frame_hasil, text='Besar energi kinetik sistem '       # Membuat Label energi kinetik awal sistem
                                 'sebelum tumbukan')
        label_ekawal.grid(row=2,column=0, sticky='w')
        titikdua = ttk.Label(frame_hasil, text=' : ')                                   # Membuat Label titik dua
        titikdua.grid(row=2, column=1)
        text_ekawal = tk.Text(frame_hasil, height=1, width=25)                          # Membuat Text energi kinetik awal sistem
        text_ekawal.grid(row=2, column=2)
        text_ekawal.insert(1.0, '0.0')
        text_ekawal.tag_config('right', justify='right')
        text_ekawal.tag_add('right',1.0,'end')
        text_ekawal.config(state='disabled')
        label_unitekawal = ttk.Label(frame_hasil, text=' J')
        label_unitekawal.grid(row=2, column=3, sticky='w')
        
        # Frame hasil : Energi kinetik akhir
        label_ekakhir = ttk.Label(frame_hasil, text='Besar energi kinetik sistem '      # Membuat Label energi kinetik akhir sistem
                                  'setelah tumbukan')
        label_ekakhir.grid(row=3,column=0, sticky='w')
        titikdua = ttk.Label(frame_hasil, text=' : ')                                   # Membuat Label titik dua
        titikdua.grid(row=3, column=1)
        text_ekakhir = tk.Text(frame_hasil, height=1, width=25)                         # Membuat Text energi kinetik akhir sistem
        text_ekakhir.grid(row=3, column=2)
        text_ekakhir.insert(1.0, '0.0')
        text_ekakhir.tag_config('right', justify='right')
        text_ekakhir.tag_add('right',1.0,'end')
        text_ekakhir.config(state='disabled')
        label_unitekakhir = ttk.Label(frame_hasil, text=' J')
        label_unitekakhir.grid(row=3, column=3, sticky='w')
        
        # Frame hasil : Koefisien restitusi
        label_restitusi = ttk.Label(frame_hasil, text='Nilai koefisien restitusi')      # Membuat Label koefisien restitusi
        label_restitusi.grid(row=4, column=0, sticky='w')
        titikdua0 = ttk.Label(frame_hasil, text=' : ')                                  # Membuat Label titik dua
        titikdua0.grid(row=4, column=1)
        text_restitusi = tk.Text(frame_hasil,height=1, width=25)                        # Membuat Text koefisien restitusi
        text_restitusi.grid(row=4, column=2)
        text_restitusi.tag_config('right', justify='right')
        text_restitusi.tag_add('right',1.0,'end')
        text_restitusi.config(state='disabled')
        
        # Frame hasil : Jenis tumbukan
        label_jenistumbukan = ttk.Label(frame_hasil, text='Jenis tumbukan')             # Membuat Label jenis tumbukan
        label_jenistumbukan.grid(row=5, column=0, sticky='w')
        titikdua0 = ttk.Label(frame_hasil, text=' : ')                                  # Membuat Label titik dua
        titikdua0.grid(row=5, column=1)
        text_jenistumbukan = tk.Text(frame_hasil,height=1, width=25)                    # Membuat Text jenis tumbukan
        text_jenistumbukan.grid(row=5, column=2)
        text_jenistumbukan.tag_config('right', justify='right')
        text_jenistumbukan.tag_add('right',1.0,'end')
        text_jenistumbukan.config(state='disabled')
        
        # Membuat Label catatan pembulatan
        note_hasil = ttk.Label(jenis_1dimensi, text='Catatan: Hasil dibulatkan '        # Menampilkan catatan untuk pengguna menggunakan fungsi Label
                               'hingga tiga angka di belakang koma.', 
                               font=('Segoe UI', 7))
        note_hasil.grid(row=6, columnspan=2, pady=(0,20))
    
    elif pilihandimensi =='2 Dimensi': # Jika opsi yang dipilih adalah 1 dimensi
        
        # Set-up window
        jenis_2dimensi = tk.Toplevel()
        jenis_2dimensi.resizable(width=False, height=False)
        
        # Menampilkan judul menggunakan fungsi Label
        judul1_jenis_2dimensi = ttk.Label(jenis_2dimensi, text='Menentukan Jenis Tumbukan', 
                                          font=('Helvetica', 20))
        judul1_jenis_2dimensi.grid(row=0, column=0, columnspan=2, sticky='n', pady=10)
        judul2_jenis_2dimensi = ttk.Label(jenis_2dimensi, text='2 Dimensi', font=('Helvetica', 20))
        judul2_jenis_2dimensi.grid(row=1, column=0, columnspan=2, sticky='n')
        
        # Membuat frame benda 1 menggunakan LabelFrame
        frame_benda1 = ttk.LabelFrame(jenis_2dimensi, text='Benda 1')
        frame_benda1.grid(row=2, column=0,ipadx=5, ipady=5, padx=(20,10), pady=(10,0))
        
        # Isi dari frame benda 1
        # Frame 1 : Massa
        label_massa1 = ttk.Label(frame_benda1, text='Massa')                            # Membuat Label massa
        label_massa1.grid(row=0, column=0, sticky='w')
        titikdua = ttk.Label(frame_benda1, text=' : ')                                  # Membuat Label titik dua
        titikdua.grid(row=0, column=1)
        entry_massa1 = ttk.Entry(frame_benda1)                                          # Menggunakan fungsi Entry untuk menerima input massa benda
        entry_massa1.grid(row=0, column=2)
        label_unitmassa1 = ttk.Label(frame_benda1, text=' kg')
        label_unitmassa1.grid(row=0, column=3, sticky='W')
        
        # Frame 1 : Kecepatan awal
        label_v1awal = ttk.Label(frame_benda1, text='Kecepatan sebelum tumbukan')       # Membuat Label kecepatan awal
        label_v1awal.grid(row=1, column=0, sticky='w')
        titikdua = ttk.Label(frame_benda1, text=' : ')                                  # Membuat Label titik dua
        titikdua.grid(row=1, column=1)
        entry_v1xawal = ttk.Entry(frame_benda1)                                         # Menggunakan fungsi Entry untuk menerima input kecepatan awal di sumbu-X
        entry_v1xawal.grid(row=1, column=2)
        label_v1awalvektor1 = ttk.Label(frame_benda1, 
                                        text=' \N{LATIN SMALL LETTER I WITH CIRCUMFLEX}  + ')
        label_v1awalvektor1.grid(row=1, column=3)
        entry_v1yawal = ttk.Entry(frame_benda1)                                         # Menggunakan fungsi Entry untuk menerima input kecepatan awal di sumbu-Y
        entry_v1yawal.grid(row=1,column=4)
        label_v1awalvektor2 = ttk.Label(frame_benda1, 
                                        text=' \N{LATIN SMALL LETTER J WITH CIRCUMFLEX}  m/s')
        label_v1awalvektor2.grid(row=1, column=5, sticky='W')
        
        # Frame 1 : Kecepatan akhir
        label_v1akhir = ttk.Label(frame_benda1, text='Kecepatan setelah tumbukan')      # Membuat Label kecepatan akhir
        label_v1akhir.grid(row=2, column=0, sticky='w')
        titikdua = ttk.Label(frame_benda1, text=' : ')                                  # Membuat Label titik dua
        titikdua.grid(row=2, column=1)
        entry_v1xakhir = ttk.Entry(frame_benda1)                                        # Menggunakan fungsi Entry untuk menerima input kecepatan akhir di sumbu-X
        entry_v1xakhir.grid(row=2, column=2)
        label_v1akhirvektor1 = ttk.Label(frame_benda1, 
                                         text=' \N{LATIN SMALL LETTER I WITH CIRCUMFLEX}  + ')
        label_v1akhirvektor1.grid(row=2, column=3)
        entry_v1yakhir = ttk.Entry(frame_benda1)                                        # Menggunakan fungsi Entry untuk menerima input kecepatan akhir di sumbu-Y
        entry_v1yakhir.grid(row=2,column=4)
        label_v1akhirvektor2 = ttk.Label(frame_benda1, 
                                         text=' \N{LATIN SMALL LETTER J WITH CIRCUMFLEX}  m/s')
        label_v1akhirvektor2.grid(row=2, column=5, sticky='W')
        
        # Membuat frame benda 2 menggunakan fungsi LabelFrame
        frame_benda2 = ttk.LabelFrame(jenis_2dimensi, text='Benda 2')
        frame_benda2.grid(row=2, column=1,ipadx=5, ipady=5, padx=(10,20), pady=(10,0))
        
        # Isi dari frame benda 2
        # Frame 2 : Massa
        label_massa2 = ttk.Label(frame_benda2, text='Massa')                            # Membuat Label massa
        label_massa2.grid(row=0, column=0, sticky='w')
        titikdua = ttk.Label(frame_benda2, text=' : ')                                  # Membuat Label titik dua
        titikdua.grid(row=0, column=1)
        entry_massa2 = ttk.Entry(frame_benda2)                                          # Menggunakan fungsi Entry untuk menerima input massa benda
        entry_massa2.grid(row=0, column=2)
        label_unitmassa2 = ttk.Label(frame_benda2, text=' kg')
        label_unitmassa2.grid(row=0, column=3, sticky='W')
       
        # Frame 2 : Kecepatan awal
        label_v2awal = ttk.Label(frame_benda2, text='Kecepatan sebelum tumbukan')       # Membuat Label kecepatan awal
        label_v2awal.grid(row=1, column=0, sticky='w')
        titikdua = ttk.Label(frame_benda2, text=' : ')                                  # Membuat Label titik dua
        titikdua.grid(row=1, column=1)
        entry_v2xawal = ttk.Entry(frame_benda2)                                         # Menggunakan fungsi Entry untuk menerima input kecepatan awal di sumbu-X
        entry_v2xawal.grid(row=1, column=2)
        label_v2awalvektor1 = ttk.Label(frame_benda2, 
                                        text=' \N{LATIN SMALL LETTER I WITH CIRCUMFLEX}  + ')
        label_v2awalvektor1.grid(row=1, column=3)
        entry_v2yawal = ttk.Entry(frame_benda2)                                         # Menggunakan fungsi Entry untuk menerima input kecepatan awal di sumbu-Y
        entry_v2yawal.grid(row=1,column=4)
        label_v2awalvektor2 = ttk.Label(frame_benda2, 
                                        text=' \N{LATIN SMALL LETTER J WITH CIRCUMFLEX}  m/s')
        label_v2awalvektor2.grid(row=1, column=5, sticky='W')
        
        # Frame 2 : Kecepatan akhir
        label_v2akhir = ttk.Label(frame_benda2, text='Kecepatan setelah tumbukan')      # Membuat Label kecepatan akhir
        label_v2akhir.grid(row=2, column=0, sticky='w')
        titikdua = ttk.Label(frame_benda2, text=' : ')                                  # Membuat Label titik dua
        titikdua.grid(row=2, column=1)
        entry_v2xakhir = ttk.Entry(frame_benda2)                                        # Menggunakan fungsi Entry untuk menerima input kecepatan akhir di sumbu-X
        entry_v2xakhir.grid(row=2, column=2)
        label_v2akhirvektor1 = ttk.Label(frame_benda2, 
                                         text=' \N{LATIN SMALL LETTER I WITH CIRCUMFLEX}  + ')
        label_v2akhirvektor1.grid(row=2, column=3)
        entry_v2yakhir = ttk.Entry(frame_benda2)                                        # Menggunakan fungsi Entry untuk menerima input kecepatan akhir di sumbu-Y
        entry_v2yakhir.grid(row=2,column=4)
        label_v2akhirvektor2 = ttk.Label(frame_benda2, 
                                         text=' \N{LATIN SMALL LETTER J WITH CIRCUMFLEX}  m/s')
        label_v2akhirvektor2.grid(row=2, column=5, sticky='W')
        
        # Membuat Label catatan keakuratan
        note_input = ttk.Label(jenis_2dimensi, text='Catatan: Untuk hasil yang '        # Menampilkan catatan untuk pengguna menggunakan fungsi Label
                               'akurat, masukkan nilai hingga 4 angka desimal '
                               'di belakang koma.', font=('Segoe UI', 7))
        note_input.grid(row=3, columnspan=2, padx=10, pady=(0,10))
        
        # Membuat Button/tombol 'Jalankan Program!'  
        button_jalankan = ttk.Button(jenis_2dimensi, text='Jalankan Program!', 
                                     command=jenistumbukan_duadimensi)
        button_jalankan.grid(row=4, columnspan=2, padx=10, pady=10)
        
        # Membuat frame hasil menggunakan fungsi LabelFrame
        frame_hasil = ttk.LabelFrame(jenis_2dimensi, text='Hasil')
        frame_hasil.grid(row=5, columnspan=2, ipadx=5, ipady=5, padx=(10,0), pady=(10,0))
        
        # Isi frame hasil
        # Frame hasil : Momentum awal
        label_momentumawal = ttk.Label(frame_hasil, text='Besar momentum sistem '       # Membuat Label momentum awal sistem
                                       'sebelum tumbukan adalah')
        label_momentumawal.grid(row=0, column=0, sticky='w')
        titikdua = ttk.Label(frame_hasil, text=' : ')                                   # Membuat Label titik dua
        titikdua.grid(row=0, column=1)
        text_momentumxawal = tk.Text(frame_hasil, height=1, width=25)                   # Membuat Text momemntum awal di sumbu-X
        text_momentumxawal.grid(row=0, column=2)
        text_momentumxawal.insert(1.0, '0.0')
        text_momentumxawal.tag_config('right', justify='right')
        text_momentumxawal.tag_add('right',1.0,'end')
        text_momentumxawal.config(state='disabled')
        label_momentumawalvektor1 = ttk.Label(frame_hasil, 
                                              text=' \N{LATIN SMALL LETTER I WITH CIRCUMFLEX}  + ')
        label_momentumawalvektor1.grid(row=0, column=3)
        text_momentumyawal = tk.Text(frame_hasil, height=1, width=25)                   # Membuat Text momentum awal di sumbu-Y
        text_momentumyawal.grid(row=0, column=4)
        text_momentumyawal.insert(1.0, '0.0')
        text_momentumyawal.tag_config('right', justify='right')
        text_momentumyawal.tag_add('right',1.0,'end')
        text_momentumyawal.config(state='disabled')
        label_momentumawalvektor2 = ttk.Label(frame_hasil,
                                              text=' \N{LATIN SMALL LETTER J WITH CIRCUMFLEX}  kg.m/s')
        label_momentumawalvektor2.grid(row=0, column=5, sticky='w')
        
        # Frame hasil : Momentum akhir
        label_momentumakhir = ttk.Label(frame_hasil, text='Besar momentum sistem '      # Membuat Label momentum akhir sistem
                                        'setelah tumbukan adalah')
        label_momentumakhir.grid(row=1, column=0, sticky='w')
        titikdua = ttk.Label(frame_hasil, text=' : ')                                   # Membuat Label titik dua
        titikdua.grid(row=1, column=1)
        text_momentumxakhir = tk.Text(frame_hasil, height=1, width=25)                  # Membuat Text momentum akhir di sumbu-X
        text_momentumxakhir.grid(row=1, column=2)
        text_momentumxakhir.insert(1.0, '0.0')
        text_momentumxakhir.tag_config('right', justify='right')
        text_momentumxakhir.tag_add('right',1.0,'end')
        text_momentumxakhir.config(state='disabled')
        label_momentumakhirvektor1 = ttk.Label(frame_hasil, 
                                               text=' \N{LATIN SMALL LETTER I WITH CIRCUMFLEX}  + ')
        label_momentumakhirvektor1.grid(row=1, column=3)
        text_momentumyakhir = tk.Text(frame_hasil, height=1, width=25)                  # Membuat Text momentum akhir di sumbu-Y
        text_momentumyakhir.grid(row=1, column=4)
        text_momentumyakhir.insert(1.0, '0.0')
        text_momentumyakhir.tag_config('right', justify='right')
        text_momentumyakhir.tag_add('right',1.0,'end')
        text_momentumyakhir.config(state='disabled')
        label_momentumakhirvektor2 = ttk.Label(frame_hasil,
                                               text=' \N{LATIN SMALL LETTER J WITH CIRCUMFLEX}  kg.m/s')
        label_momentumakhirvektor2.grid(row=1, column=5, sticky='w')
        
        # Frame hasil : Energi kinetik awal
        label_ekawal = ttk.Label(frame_hasil, text='Besar energi kinetik sistem '       # Membuat Label energi kinetik awal sistem
                                 'sebelum tumbukan adalah')
        label_ekawal.grid(row=2,column=0, sticky='w')
        titikdua = ttk.Label(frame_hasil, text=' : ')                                   # Membuat Label titik dua
        titikdua.grid(row=2, column=1)
        text_ekawal = tk.Text(frame_hasil, height=1, width=25)                          # Membuat Text energi kinetik awal sistem
        text_ekawal.grid(row=2, column=2)
        text_ekawal.insert(1.0, '0.0')
        text_ekawal.tag_config('right', justify='right')
        text_ekawal.tag_add('right',1.0,'end')
        text_ekawal.config(state='disabled')
        label_unitekawal = ttk.Label(frame_hasil, text=' J')
        label_unitekawal.grid(row=2, column=3, sticky='w')
        
        # Frame hasil : Energi kinetik akhir
        label_ekakhir = ttk.Label(frame_hasil, text='Besar energi kinetik sistem '      # Membuat Label energi kinetik akhir sistem
                                  'setelah tumbukan adalah')
        label_ekakhir.grid(row=3,column=0, sticky='w')
        titikdua = ttk.Label(frame_hasil, text=' : ')                                   # Membuat Label titik dua
        titikdua.grid(row=3, column=1)
        text_ekakhir = tk.Text(frame_hasil, height=1, width=25)                         # Membuat Text energi kinetik akhir sistem
        text_ekakhir.grid(row=3, column=2)
        text_ekakhir.insert(1.0, '0.0')
        text_ekakhir.tag_config('right', justify='right')
        text_ekakhir.tag_add('right',1.0,'end')
        text_ekakhir.config(state='disabled')
        label_unitekakhir = ttk.Label(frame_hasil, text=' J')
        label_unitekakhir.grid(row=3, column=3, sticky='w')
        
        # Frame hasil : Jenis tumbukan
        label_jenistumbukan = ttk.Label(frame_hasil, text='Jenis tumbukan adalah')      # Membuat Label jenis tumbukan
        label_jenistumbukan.grid(row=4, column=0, sticky='w')
        titikdua0 = ttk.Label(frame_hasil, text=' : ')                                  # Membuat Label titik dua
        titikdua0.grid(row=4, column=1)
        text_jenistumbukan = tk.Text(frame_hasil,height=1, width=25)                    # Membuat Text jenis tumbukan
        text_jenistumbukan.grid(row=4, column=2)
        text_jenistumbukan.tag_config('right', justify='right')
        text_jenistumbukan.tag_add('right',1.0,'end')
        text_jenistumbukan.config(state='disabled')
        
        # Membuat Label catatan pembulatan
        note_hasil = ttk.Label(jenis_2dimensi, text='Catatan: Hasil dibulatkan '        # Menampilkan catatan pengguna menggunakan fungsi Label
                               'hingga tiga angka di belakang koma.', 
                               font=('Segoe UI', 7))
        note_hasil.grid(row=6, columnspan=2, pady=(0,20))