import sys
import socket

class Utama():
    def __init__(self):
        print("Masukkan Pil. Anda : ")
        print("1. Sebagai Server")
        print("2. Sebagai Client")
        print("3. Keluar")

        pilih = input("Mskkan Angka pilihan = ")

        if pilih == "1":
            lokasi = socket.gethostbyname("127.0.0.1")
            s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
            s.bind((lokasi, 2120))
            s.listen(5)
            print("Server Sudah Aktif")

            client, alamat = s.accept()
            print("menerima koneksi dari : ", alamat)
            while True:
                data = client.recv(1024).decode()
                if not data:
                    break;
                print("Pesan masuk :", str(data))
                data = input(">")
                client.send(data.encode())
        elif pilih=="2":
            alamatServer = input("masukkan alamat server : ")
            s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
            s.connect((alamatServer, 2120))
            pesan = input(">")
            while pesan!="bye":
                s.send(pesan.encode())
                data = s.recv(1024).decode()
                print("Server : ", data)
                pesan = input(">")
                s.close()
        else:
            quit()

if __name__ == "__main__":
    Utama()
    sys.exit()