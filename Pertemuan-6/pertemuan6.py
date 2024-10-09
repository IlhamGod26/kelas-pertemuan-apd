# daftar_buku = { 
# "Buku1" : "Harry Potter", 
# "Buku2" : "Percy Jackson", 
# "Buku3" : "Twillight" 
# } 
# print(daftar_buku["Buku1"]) 
# print(daftar_buku["Buku2"]) 
# print(daftar_buku["Buku3"])

# Biodata = { 
# "Nama" : "Aldy Ramadhan Syahputra", 
# "NIM" : 2109106079, 
# "KRS" : ["Program Web", "Struktur Data", "Basis Data"], "Mahasiswa_Aktif" :True, 
# "Social Media" : { 
# "Instagram" : "@aldyrmdhns_", 
# "Discord" : "\'Izanami#6848"
# } 
# }
# print(Biodata["KRS"][0])
# print(Biodata["Social Media"]["Instagram"])



# games = dict(Sekiro = "Action", Pokemon = "Adventure", 
# Valorant = {"nama" : {123 : "informatika"}}) 
# print(games['Valorant']['nama'][123])

# Games = {
#     "Game1" : "Mobile Legend",
#     "Game2" : "PUBG Mobile",
#     "Game3" : {
#         "nama" : "COC",
#         "genre" : "strategy"
#     }

# }
# print((Games.get('Game3)))

# Nilai = { 
# "Matematika" : 80, 
# "B. Indonesia" : 90, 
# "B. Inggris" : 81, 
# "Kimia" : 78, 
# "Fisika" : 80 
# }
# #tanpa menggunakan items 
# for i in Nilai: 
#     print(i) 
# print("") 
# #menggunakan items 
# for i, j in Nilai.items(): 
#     print(f"Nilai {i} anda adalah {j}")

# Film = {
# "Avenger Endgame" : "Action", 
# "Sherlock Holmes" : "Mystery", 
# "The Conjuring" : "Horror" 
# } 
# #Sebelum Ditambah 
# print(Film)

# Film["Zombieland"] = "Comedy" 
# Film.update({"Hours" : "Thriller", 
#              "Rush Hour" : "Comedy",
#              "Oblivion" : "Science Fiction"})
# # Setelah Ditambah 
# # pengguna del
# del Film["Avenger Endgame"]
# print(Film)
# simpan = Film.pop('Hours')
# print(Film)
# Film["Hours"] = simpan
# print(Film)
# print("Jumlah Film = ", len(Film))

# movies = Film.copy()
# print(movies)
# print("Jumlah Film = ", len(movies))

# key = "apel", "jeruk", "mangga" 
# value = 1
# buah = dict.fromkeys(key, value) 
# print(buah)

# Nilai = { 
# "Matematika" : 80, 
# "B. Indonesia" : 90, 
# "B. Inggris" : 81 
# } 
# #sebelum Setdefault 
# print(Nilai) 
# print("") 
# #menggunakan setdefault 
# print("Nilai : ", Nilai.setdefault("Kimia", 70)) 
# print("") 
# #setelah menggunakan setdefault 
# print(Nilai) 

# Musik = { 
# "The Chainsmoker" : ["All we Know", "TheParis"], 
# "Alan Walker" : ["Alone", "Lily"], 
# "Neffex" : ["Best of Me", "Memories"] 
# } 
# for i, j in Musik.items(): 
#     print(f"Musik milik {i} adalah : ") 
#     for song in j: 
#         print(song) 
# print("")

# mahasiswa = { 
# 114 : {"Nama" : "Riduan", "Umur" : 18}, 
# 111 : {"Nama" : "Jamal", "Umur" : 18} 
# } 
# for key, value in mahasiswa.items(): 
#     print("ID Mahasiswa : ", key) 
#     for x, y in value.items(): 
#         print (x, " : ", y) 
# print("")

nilai ={
    'matematika' : 90,
    'Fisika' : 80,
    'Biologi' : 80,
    'Kimia' : 70
}
total = 0
for i in nilai.values():
    total1 =+ i
print(f"total nilai adalah {total}")
print(f"rata rata nilai adalah {total/4}")