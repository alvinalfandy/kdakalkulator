# kda kalkulator
# Menghitung kda

## Apa Fungsi Script ini?
- Fungsi dari script ini adalah untuk menghitung dan menampilkan rasio Kill-Death-Assist (KDA) berdasarkan input yang diberikan oleh pengguna. Dalam konteks permainan video atau situasi yang melibatkan skor atau statistik terkait kemenangan atau keberhasilan, KDA adalah metrik yang umumnya digunakan. Dalam banyak permainan, terutama game daring (online), KDA digunakan untuk menilai kontribusi seorang pemain dalam pertandingan.

- Sebagai contoh, dalam game seperti MOBA (Multiplayer Online Battle Arena) seperti League of Legends atau Dota 2, KDA adalah indikator yang sering digunakan untuk mengevaluasi seberapa efektif seorang pemain dalam membantu timnya dengan mengamati jumlah kill (membunuh musuh), death (terbunuh), dan assist (membantu membunuh musuh).

- Dengan menggunakan script ini, pemain dapat dengan mudah menghitung dan melihat seberapa baik mereka atau pemain lainnya berkinerja dalam hal KDA. Ini dapat memberikan wawasan tambahan tentang seberapa efektif pemain tersebut dalam kontribusinya terhadap tim.

- Jadi, secara umum, fungsi dari script ini adalah memberikan alat sederhana untuk mengukur dan melihat performa pemain dalam konteks tertentu, terutama dalam permainan daring yang menggunakan konsep KDA.

## Kode program
```def hitung_kda(k, d, a):
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

```
## Atau bisa kalian download pada file main.py

# OUTPUT PROGRAM
<img width="841" alt="image" src="https://github.com/alvinalfandy/kdakalkulator/assets/64345368/44db597c-12b0-4317-a8fb-5c177b483125">
