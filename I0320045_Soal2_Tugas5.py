# Mulai
print("Program Grading Nilai")
print("")
print("")
print("Silahkan inputkan nama lengkap anda")
x = input(str(": "))
print("Halo", x, ",", "Silahkan input nilai anda")
y = int(input(": "))
if y < 60 :
    print("Halo", x, "!", "Nilai anda setelah dikonversi adalah E")
    print("Lebih giat lagi belajar dan tingkatkan, jika ingin tambahan nilai hubungi dosen mata kuliah ini")
elif 60 <= y <= 64 :
    print("Halo", x, "!", "Nilai anda setelah dikonversi adalah C")
    print("Lebih giat lagi belajar dan tingkatkan, jika ingin tambahan nilai hubungi dosen mata kuliah ini")
elif 65 <= y <= 69 :
    print("Halo", x, "!", "Nilai anda setelah dikonversi adalah C+")
    print("Lebih giat lagi belajar dan tingkatkan, jika ingin tambahan nilai hubungi dosen mata kuliah ini")
elif 70 <= y <= 74 :
    print("Halo", x, "!", "Nilai anda setelah dikonversi adalah B")
    print("Lebih giat lagi belajar dan tingkatkan, jika ingin tambahan nilai hubungi dosen mata kuliah ini")
elif 75 <= y <= 79 :
    print("Halo", x, "!", "Nilai anda setelah dikonversi adalah B+")
    print("Lebih giat lagi belajar dan tingkatkan, jika ingin tambahan nilai hubungi dosen mata kuliah ini")
elif 80 <= y <= 84 :
    print("Halo", x, "!", "Nilai anda setelah dikonversi adalah A-")
    print("Lebih giat lagi belajar dan tingkatkan, jika ingin tambahan nilai hubungi dosen mata kuliah ini")
elif 85 <= y <= 90 :
    print("Halo", x, "!", "Nilai anda setelah dikonversi adalah A")
    print("Lebih giat lagi belajar dan tingkatkan, jika ingin tambahan nilai hubungi dosen mata kuliah ini")
elif 91 <= y <= 100 :
    print("Halo", x, "!", "Nilai anda setelah dikonversi adalah A")
    print("Selamat, tingkatkan dan pertahankan nilai anda agar tetap di range A, Tetap Semangat")
else:
    pass
print("")
input("Tekan Enter Untuk Kembali")
print("")
print("Tetap Semangat Ya", x)

# Selesai