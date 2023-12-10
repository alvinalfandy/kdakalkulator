def hitung_kda(k, d, a):
    if d == 0:
        return "KDA tak terbatas (karena tidak ada kematian)"
    else:
        kda = (k + a) / d
        return kda

# Fungsi untuk menampilkan ASCII art "KALKULATOR KDA"
def tampilkan_ascii_art():
    # ASCII art "KALKULATOR KDA"
    ascii_art = """
██   ██ ██████   █████      ██   ██  █████  ██      ██   ██ ██    ██ ██       █████  ████████  ██████  ██████  
██  ██  ██   ██ ██   ██     ██  ██  ██   ██ ██      ██  ██  ██    ██ ██      ██   ██    ██    ██    ██ ██   ██ 
█████   ██   ██ ███████     █████   ███████ ██      █████   ██    ██ ██      ███████    ██    ██    ██ ██████  
██  ██  ██   ██ ██   ██     ██  ██  ██   ██ ██      ██  ██  ██    ██ ██      ██   ██    ██    ██    ██ ██   ██ 
██   ██ ██████  ██   ██     ██   ██ ██   ██ ███████ ██   ██  ██████  ███████ ██   ██    ██     ██████  ██   ██ 
                                                                                                               
                                                                                                               
    """
    print(ascii_art)

# Pengulangan program
while True:
    # Menampilkan ASCII art "KALKULATOR KDA"
    tampilkan_ascii_art()

    # Meminta input dari pengguna
    kill = int(input("Masukkan jumlah Kill: "))
    death = int(input("Masukkan jumlah Death: "))
    assist = int(input("Masukkan jumlah Assist: "))

    # Menghitung dan mencetak KDA
    hasil_kda = hitung_kda(kill, death, assist)
    print("KDA:", hasil_kda)

    # Meminta pengguna untuk melakukan pengulangan
    ulangi = input("Apakah Anda ingin menghitung KDA lagi? (Y/T): ")
    if ulangi.upper() != 'Y':
        break
