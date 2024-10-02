nama = ["shandy",106,True,
        ["yuyun",145],3.96,
        [123,"alvito",False,3.66]
        ]
print(nama[4][2])
print(nama[4][1])
print(nama[4][3])
print(nama[5][0])
print(nama[4])

makanan = ["bakso","sate","soto","mie ayam","ayam bakar"]
print("sebelum: ")
print(makanan)
makanan.append("nasi goreng")
print("sesudah: ")
makanan.clear
data = makanan.pop(5)
print(makanan)
print(data)
print(makanan)
makanan.insert(2,"nasi goreng")
makanan[0] = "ayam","bebek"
print(makanan)

minuman = ["kawa kawa","bintang","wisky","es teh","josu","susu"]
print("sebelum")
print(minuman)
del minuman[2]
print("sesudah")
print(minuman)
minuman[4] = "air putih"
print(minuman)
minuman.insert(0,"jus tomat")
print(minuman)

makanan = ["bebek","ikan",["bakso","soto","sate","ikan","ayam"],["teh","kopi","air"]]
for i in makanan :
    if isinstance(i, list):
        for j in i :
            print(j)
    else:
        print(i)
for i in makanan :
    for j in i :
        print(j)

akuns = []

while True:
    print("halo selamat datang di aplikasi cacatan")
    print("silakan pilih 'Daftar Akun' dan jika sudah memiliki akun silakan 'login'")
    print("1. Daftar Akun")
    print("2. logi")
    print("3. Exit")
    print("_____________")
    opsi = input("pilih opsi: ")
    print(" ")
    
    if opsi == "1":
        print("halo pengguna bau! Ayo buat akun dulu")
        username = input("username: ")
        akuna = False
        for akun in akuns:
            if akun[0] == username:
                akuna = True
                break
        if akuna:
            print("nama sudah terpakai untuk registrasi silakan coba lagi")
        else:
            password = input("password: ")
            akuns.append(username, password, [])
            print(f"akun anda berhasil terdaftar dengan ID: (username)")