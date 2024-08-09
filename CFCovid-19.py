
while True:
    print("___________________________________________________________________________")
    print("|--Selamat Datang pada Program untuk menghitung gejala penyakit Covid-19--|\n"
          "|---------------------menggunakan metode Certainty Factor-----------------|")
    print("|Isi 'y' jika terdapat gejala, isi 't' jika tidak terdapat gejala tersebut|")
    print("---------------------------------------------------------------------------")

    penyakit = ["COVID-19"]
    gejala = ["Sesak Nafas","Sakit Tenggorokan","Batuk","Demam","Pilek"]
    pengetahuan = [
        ["COVID-19","Sesak Nafas", 0.8, 0.01],
        ["COVID-19","Sakit Tenggorokan", 0.7, 0.03],
        ["COVID-19","Batuk", 0.6, 0.05],
        ["COVID-19","Demam", 0.3, 0.1],
        ["COVID-19","Pilek", 0.4, 0.1]
    ]


    gejala_dipilih = []

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
                            mb = mbperhitungan
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

    data = open("data.txt","a+")
    data.write(f'- CF = {max(cfrangking)} \n')
    data.write("Terima Kasih \n")
    data.write("--------------------------------------------\n")
    data = open("data.txt", "r")


    ulg = input("Lanjut?, Tekan Enter untuk lanjut, Tekan x untuk keluar dari program \n")
    if ulg == 'x':
        input("Terima Kasih\n")
        break


