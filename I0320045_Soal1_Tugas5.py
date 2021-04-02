# Mulai

# Daftar Nama:
# "Harry", "Brahmana" untuk laki laki
# "Kasih", "Karina" untuk perempuan

# Kalimat sapaan awal untuk pengunjung hotel saat memasuki hotel
print("Selamat datang di Hotel Sebelas Maret")
print("")
print("Adakah yang bisa kami bantu?")
print("")
x = str(input("Sebelumnya saya sudah melakukan resevasi lewat aplikasi HSM (Hotel Sebelas Maret) atas nama: "))
if x == "Harry" :
    print("")
    print("Selamat datang Pak", x, ",", "Ini kunci kamar anda, kamar nya berada dilantai 3, selamat menikmati pelayanan dan fasilitas hotel kami")
elif x == "Brahmana" :
    print("")
    print("Selamat datang Pak", x, ",", "Ini kunci kamar anda, kamar nya berada dilantai 3, selamat menikmati pelayanan dan fasilitas hotel kami")
elif x == "Kasih" :
    print("")
    print("Selamat datang Bu", x, ",", "Ini kunci kamar anda, kamar nya berada dilantai 3, selamat menikmati pelayanan dan fasilitas hotel kami")
elif x == "Karina" :
    print("")
    print("Selamat datang Bu", x, ",", "Ini kunci kamar anda, kamar nya berada dilantai 3, selamat menikmati pelayanan dan fasilitas hotel kami")
else:
    pass

print("")
input("Untuk kembali klik enter")
print("")
if x == "Harry" :
    print("")
    print("Terima kasih Pak", x)
elif x == "Brahmana" :
    print("")
    print("Terima kasih Pak", x)
elif x == "Kasih" :
    print("")
    print("Terima kasih Bu", x)
elif x == "Karina" :
    print("")
    print("Terima kasih Bu", x)
else:
    pass

print("")
print("Selesai")