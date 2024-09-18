# cuaca = "mendung"
# if cuaca == "mendung":
#     print("diam di rumah")
# else:
#     print("hari ini mendung")

# umur = (int(input("Masukkan umur anda : ")))
# if umur > 0:
#     if umur <= 10:
#         print( " umur anda termaksuk kategori anak-anak")
#     elif umur <= 18:
#         print("umur anda termasuk kategori remaja")
#     elif umur <= 35:
#         print("umur anda termaksuk kategori dewasa")
#     elif umur <= 65:
#         print("umur anda termasuk kategori paruh baya")
#     else:
#         print("umur anda termasuk kategori tua")
# else:
#     print("input usia harus bilangan positif")



# nim = int(input("masukan nim:"))
# if nim >= 1 and nim <=50 :
#     if nim >= 1 and nim <=25 :
#         print("kelas A'1")
#     else :
#         print("kelas A'2") 
# elif nim >= 51 and nim <= 100:
#     if nim >= 51 and nim <=75 :
#         print("kelas B'1")
#     else :
#         print("kelas B'2")
# elif nim >= 101 and nim <= 121 :
#     if nim >= 101 and nim <= 110 :
#         print("kelas C'1")
#     else :
#         print("kelas C'2")
# else :
#     print("anda bukan mahasiswa informatika 24")



angka = int(input("masukkan angka: "))
result = "Genap" if angka % 2 == 0 else "Ganjil"
print(result)
nim = int(input("masukkan nim: "))
hasil = "kelas A" if nim >= 1 and nim <=50 else "kelas B" if nim <=51 and nim <= 100 else "kelas C" if nim >=101 and nim <= 121 else "mahasiswa siluman"
print(hasil)