# Aturan Wabah
def diagnose_bulai(gejala):
    return gejala['a'] and gejala['b'] and gejala['c'] and gejala['d'] and gejala['e'] and gejala['f']

def diagnose_hawar(gejala):
    return gejala['e'] and gejala['g'] and gejala['k'] and gejala['j'] and gejala['l']

def diagnose_karat_daun(gejala):
    return gejala['k'] and gejala['m'] and gejala['p'] and gejala['q']

def diagnose_terbakar(gejala):
    return gejala['r'] and gejala['s'] and gejala['t'] and gejala['u'] and gejala['v']

# Aturan turunan berdasarkan gejala yang saling terkait
def forward_chaining(gejala):
    # Bulai
    if gejala['a'] and gejala['b']:
        gejala['c'] = True
    if gejala['b'] and gejala['c']:
        gejala['d'] = True
    if gejala['d']:
        gejala['e'] = True
    if gejala['c'] and gejala['e']:
        gejala['f'] = True

    # Hawar
    if gejala['e'] and gejala['g']:
        gejala['k'] = True
    if gejala['h'] and gejala['i']:
        gejala['j'] = True
    if gejala['g'] and gejala['j']:
        gejala['l'] = True

    # Karat Daun
    if gejala['a'] and gejala['b'] or gejala['h'] and gejala['i']:
        gejala['m'] = True
    if gejala['m']:
        gejala['p'] = True
    if gejala['n']:
        gejala['p'] = True
    if gejala['o']:
        gejala['m'] = True
    if gejala['g']:
        gejala['k'] = True
    if gejala['k']:
        gejala['q'] = True

    # Terbakar
    if gejala['r']:
        gejala['s'] = True
    if gejala['s']:
        gejala['t'] = True
    if gejala['t']:
        gejala['u'] = True
    if gejala['u']:
        gejala['v'] = True

# Pertanyaan Gejala
def tanya_gejala(gejala, kode, pertanyaan):
    if gejala[kode] is None:
        jawaban = input(pertanyaan + " (Y/T): ").strip().upper()
        gejala[kode] = (jawaban == 'Y')

def main():
    # Inisialisasi gejala dengan None
    gejala = {
        'a': None, 'b': None, 'c': None, 'd': None, 'e': None,
        'f': None, 'g': None, 'h': None, 'i': None, 'j': None,
        'k': None, 'l': None, 'm': None, 'n': None, 'o': None,
        'p': None, 'q': None, 'r': None, 's': None, 't': None,
        'u': None, 'v': None
    }

    print("Selamat datang di sistem pakar diagnosa penyakit tanaman.")
    selesai = False

    while not selesai:
        # Tanyakan gejala yang dibutuhkan
        tanya_gejala(gejala, 'a', "Apakah daun berwarna klorosis?")
        tanya_gejala(gejala, 'b', "Apakah tanaman mengalami pertumbuhan terhambat?")
        tanya_gejala(gejala, 'g', "Apakah daun yang terkena terlihat layu?")
        tanya_gejala(gejala, 'h', "Apakah terdapat beberapa bintik kecil yang bersatu membentuk bintik lebih besar?")
        tanya_gejala(gejala, 'i', "Apakah bintik-bintik berbentuk seperti gulungan atau perahu?")
        tanya_gejala(gejala, 'n', "Apakah terdapat bintik merah pada tulang daun tengah?")
        tanya_gejala(gejala, 'o', "Apakah terdapat benang-benang tidak teratur yang berwarna putih kemudian berubah menjadi coklat?")
        tanya_gejala(gejala, 'r', "Apakah terdapat pembengkakan pada tongkol?")
        
        # Lakukan forward chaining untuk menentukan gejala turunan
        forward_chaining(gejala)

        # Diagnosis penyakit
        if diagnose_bulai(gejala):
            print("Diagnosis: Tanaman terkena Bulai.")
            selesai = True
        elif diagnose_hawar(gejala):
            print("Diagnosis: Tanaman terkena Hawar.")
            selesai = True
        elif diagnose_karat_daun(gejala):
            print("Diagnosis: Tanaman terkena Karat Daun.")
            selesai = True
        elif diagnose_terbakar(gejala):
            print("Diagnosis: Tanaman terkena Wabah Terbakar.")
            selesai = True
        else:
            print("Belum ditemukan diagnosis yang sesuai. Lanjutkan dengan gejala lebih lanjut.")

        # Jika belum selesai, tanyakan lebih banyak gejala
        if not selesai:
            tanya_gejala(gejala, 'c', "Apakah terdapat warna putih seperti tepung di permukaan atas dan bawah daun?")
            tanya_gejala(gejala, 'd', "Apakah daun melengkung dan memutar?")
            tanya_gejala(gejala, 'e', "Apakah pembentukan tongkol terganggu?")
            tanya_gejala(gejala, 'j', "Apakah bintik coklat berbentuk elips?")
            tanya_gejala(gejala, 'k', "Apakah daun terlihat kering?")
            tanya_gejala(gejala, 'm', "Apakah terdapat bintik kecil coklat atau kuning pada permukaan daun?")
            tanya_gejala(gejala, 'p', "Apakah muncul bubuk seperti tepung coklat kekuningan?")
            tanya_gejala(gejala, 'q', "Apakah tanaman menunjukkan tanda-tanda karat daun?")
            tanya_gejala(gejala, 's', "Apakah terdapat jamur berwarna putih hingga hitam pada biji?")
            tanya_gejala(gejala, 't', "Apakah biji membengkak?")
            tanya_gejala(gejala, 'u', "Apakah terdapat kelenjar pada biji?")
            tanya_gejala(gejala, 'v', "Apakah kelobot terbuka dan terdapat banyak jamur putih hingga hitam?")
            
            # Lakukan forward chaining lagi
            forward_chaining(gejala)

        # Periksa kembali setelah menambahkan gejala baru
        if diagnose_bulai(gejala):
            print("Diagnosis: Tanaman terkena Bulai.")
            selesai = True
        elif diagnose_hawar(gejala):
            print("Diagnosis: Tanaman terkena Hawar.")
            selesai = True
        elif diagnose_karat_daun(gejala):
            print("Diagnosis: Tanaman terkena Karat Daun.")
            selesai = True
        elif diagnose_terbakar(gejala):
            print("Diagnosis: Tanaman terkena Wabah Terbakar.")
            selesai = True
        else:
            print("Belum ditemukan diagnosis yang sesuai dengan gejala yang Anda masukkan.")

if _name_ == "_main_":
    main()
