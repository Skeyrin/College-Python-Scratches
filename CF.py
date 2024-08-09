import tkinter as tk
from tkinter import ttk
from tkinter import *

win = tk.Tk()

l1 = ttk.Label(win, text="  Program Pembeda Demam Biasa, Demam Berdarah, & Demam Covid-19  ",
               borderwidth = 10, relief = "solid",
               font = ("Helvetica", 15))
l1.pack()


print("Selamat Datang pada Program untuk membedakan penyakit Demam biasa, berdarah, Covid-19 "
      "menggunakan metode Certainty factor")
print("Isi 'y' jika terdapat gejala isi 't' jika tidak terdapat gejala tersebut")

penyakit = ["Demam Biasa","Demam Berdarah","COVID-19"]
gejala = ["Panas","Sakit Kepala","Batuk",
          "Bersin,Pilek,Hidung Tersumbat",
          "Kedinginan","Sakit Tenggorokan",
          "Kelelahan","Kehilangan Selera Makan",
          "Sesak Nafas","Nyeri Sekujur Tubuh",
          "Bintik Merah Pada Kulit","Mual",
          "Muntah","Diare","Mimisan"]
pengetahuan = [
    ["Demam Biasa","Panas", 0.9, 0.1],
    ["Demam Biasa","Sakit Kepala", 0.5, 0.2],
    ["Demam Biasa","Batuk", 0.5, 0.2],
    ["Demam Biasa","Bersin,Pilek,Hidung Tersumbat", 0.5, 0.3],
    ["Demam Biasa","Kedinginan", 0.5, 0.2],
    ["Demam Biasa","Sakit Tenggorokan", 0.6, 0.2],
    ["Demam Biasa","Kelelahan", 0.5, 0.1],
    ["Demam Biasa","Kehilangan Selera Makan", 0.5, 0.2],
    ["Demam Berdarah","Panas", 0.9, 0.1],
    ["Demam Berdarah","Sakit Kepala", 0.8, 0.2],
    ["Demam Berdarah","Kehilangan Selera Makan", 0.8, 0.2],
    ["Demam Berdarah","Nyeri Sekujur Tubuh", 0.9, 0.1],
    ["Demam Berdarah","Bintik Merah Pada Kulit", 0.7, 0.2],
    ["Demam Berdarah","Mual", 0.7, 0.2],
    ["Demam Berdarah","Muntah", 0.8, 0.1],
    ["Demam Berdarah","Diare", 0.8, 0.2],
    ["Demam Berdarah","Mimisan", 0.8, 0.2],
    ["COVID-19","Panas", 0.3, 0.1],
    ["COVID-19","Batuk", 0.6, 0.05],
    ["COVID-19","Bersin, Pilek, Hidung Tersumbat", 0.4, 0.1],
    ["COVID-19","Sakit Tenggorokan", 0.7, 0.3],
    ["COVID-19","Sesak Nafas", 0.8, 0.01]
]


gejala_dipilih = []


agr = []
agr2 = []
for i in range(len(gejala)):
    l2 = ttk.Label(win, text=f'Apakah Mengalami {gejala[i]} (Y/T) : ', font=("Helvetica", 10))
    l2.pack()
    agree = tk.StringVar()
    agr.append(agree)
    ttk.Checkbutton(win, text=' centang untuk y, biarkan kosong untuk t',
                    variable=agree,
                    onvalue='y',
                    offvalue='t').pack()

def hasilaaa():
    inp = agree.get()
    agr2.append(inp)
    lbl.config(text="Hasil : " + inp)
    print(inp)

tmbl = tk.Button(win,
                        text="Proses",
                        command=hasilaaa)
tmbl.pack()

lbl = tk.Label(win, text="")
lbl.pack()



win.geometry('150x280')
win.mainloop()

for i in range(len(gejala)):
    jawab = input("Apakah Mengalami "+gejala[i]+" (Y/T) : ")
    if jawab.upper() == "Y":
        gejala_dipilih.append(gejala[i])
print("Gejala Dipilih : ", gejala_dipilih)
penyakit_terpilih = []
for i in range (len(pengetahuan)):
    for j in range (len(gejala_dipilih)):
        if (pengetahuan[i][1] == gejala_dipilih[j]):
            if pengetahuan[i][0] not in penyakit_terpilih:
                penyakit_terpilih.append(pengetahuan[i][0])
print("Penyakit Terpilih", penyakit_terpilih)

list_cf = []
for i in range (len(penyakit_terpilih)):
    print("====" +penyakit_terpilih[i]+ "====")
    jmlpengetahuan = 0
    pengetahuanke = 0
    for j in range(len(pengetahuan)):
        if (pengetahuan[j][0] == penyakit_terpilih[i]) and (pengetahuan[j][1] in gejala_dipilih):
            jmlpengetahuan = jmlpengetahuan + 1
    mblama = 0
    mdlama = 0
    for j in range (len(pengetahuan)):
        if (pengetahuan[j][0] == penyakit_terpilih[i]) and \
                (pengetahuan[j][1] in gejala_dipilih):
            pengetahuanke = pengetahuanke + 1
            if(jmlpengetahuan == 1):
                mb = pengetahuan[j][2]
                md = pengetahuan[j][3]
                cf = mb - md
                print("mb = ", mb)
                print("md = ", md)
                print("cf = mb - md = ", mb, " - ", md, "=", cf)
                list_cf.append(cf)
            elif (jmlpengetahuan > 1 ):
                if (pengetahuanke == 1):
                    mblama = pengetahuan[j][2]
                    mdlama = pengetahuan[j][3]
                    print("mblama = ", mblama)
                    print("mdlama = ", mdlama)
                elif (pengetahuanke == 2):
                    mbbaru = pengetahuan[j][2]
                    mdbaru = pengetahuan[j][3]
                    mbsementara1 = mblama - mdlama
                    mbsementara2 = mbbaru - mdbaru

                    mbperhitungan = mbsementara1 + (mbsementara2 * (1 - mbsementara1))

                    print("mbsementara = mb1 + mb2 * (1 - mb1) = ",
                          mbsementara1, " + ", mbsementara2, " * (1 - ", mbsementara1, ") = ", mbperhitungan)
                    if (jmlpengetahuan == 2):
                        mb = mbsementara1
                        print("mb = mbsementara = ", mb)

                        list_cf.append(mb)
                elif (pengetahuanke >= 3):
                    mblama = mbperhitungan
                    print("mblama = mbsementara = ", mblama)
                    print("mdlama = mdsementara = ", mdlama)
                    mbbaru = pengetahuan[j][2]
                    mdbaru = pengetahuan[j][3]
                    print("mbbaru = ", mbbaru)
                    print("mdbaru = ", mdbaru)
                    mbsementara1 = mblama
                    mbsementara2 = mbbaru - mdbaru

                    mbperhitungan = mbsementara1 + (mbsementara2 * (1 - mbsementara1))

                    print("mbsementara = mb1 + mb2 * (1 - mb1) = (",
                          mbsementara1, " + ", mbsementara2, ") * (1 - ", mbsementara1, ") = ", mbperhitungan)
                    if (jmlpengetahuan == pengetahuanke):
                        mb = mbperhitungan
                        print("mb = mbsementara = ", mb)

                        list_cf.append(mb)
print("Penyakit Terpilih - ", penyakit_terpilih)
print("Dengan cf sebesar - ",list_cf)
penyakitrangking = []
cfrangking = []
for i in range(len(penyakit_terpilih)):
    penyakitrangking.append(penyakit_terpilih[i])
    cfrangking.append(list_cf[i])
for i in range (len(penyakit_terpilih)):
    for j in range (len(penyakit_terpilih)):
        if j > i:
            if cfrangking[j] > cfrangking[i]:
                tmpcf = cfrangking[i]
                tmppenyakit = penyakitrangking[i]
                cfrangking[i] = cfrangking[j]
                penyakitrangking[i] = penyakitrangking[j]
                cfrangking[j] = tmpcf
                penyakitrangking[j] = tmppenyakit
print("Rangking Penyakit - ", penyakitrangking)
print("Rangking CF       - ", cfrangking)
print("CF Tertinggi      - ", max(cfrangking),"yaitu ", penyakitrangking[0])

data = open("data.txt","a+")
data.write(f'Rangking Penyakit - {penyakitrangking}\n')
data.write(f'Rangking CF       - {cfrangking}\n')
data.write(f'CF Tertinggi      - {max(cfrangking)}, yaitu, {penyakitrangking[0]}\n')
data.write("Terima Kasih")
data = open("data.txt", "r")

input("Press enter to proceed...")
