

# ============================================================
# BAGIAN 1: DATA PLAYER & DAFTAR ITEM (ARRAY 2 DIMENSI)
# Format data player: [Nickname Player, Level, Inventory List]
# ============================================================
players = []
daftar_item = ["Potion Heal", "Dagger", "Iron Sword", "Shield", "Bow", "Arrow", "Helmet", "Armor", "Mana potion"]

# ============================================================
# BAGIAN 2: INPUT DATA PLAYER
# ============================================================
def inputData(data):
    nickname = input("Masukkan nickname player: ")
    level = int(input("Masukkan level player: "))

    inventory = []
    jumlah_item = int(input("Jumlah item yang akan dimiliki player: "))

    print("\nDAFTAR ITEM:")
    for i in range(len(daftar_item)):
        print(i+1, ".", daftar_item[i])


    for i in range(jumlah_item):
        pilih = int(input("Pilih nomor item: "))
        inventory.append(daftar_item[pilih-1])

    data.append([nickname, level, inventory])
    print("Data player berhasil ditambahkan!")


# ============================================================
# BAGIAN 3: TAMPIL DATA PLAYER
# ============================================================
def tampilData(data):
    if len(data) == 0:
        print("Data player kosong.")
    else:
        print("\n=== DATA PLAYER ===")
        for i in range(len(data)):
            print("\nPlayer ke-", i+1)
            print("Nickname:", data[i][0])
            print("Level:", data[i][1])
            print("Inventory:")
            for item in data[i][2]:
                print(" -", item)


# ============================================================
# BAGIAN 4: PENGURUTAN (SORTING)
# Insertion Sort (Pengurutan Sisip) berdasarkan Level
# ============================================================
def insertionTurun(data, n):
    for i in range(1, n):
        m = data[i] # satu baris player
        j = i - 1
        ketemu = False
        
        while j >= 0 and not ketemu:
            if m[1] > data[j][1]: # bandingkan level
                data[j + 1] = data[j]
                j -= 1
            else:
                ketemu = True
        data[j + 1] = m


# ============================================================
# BAGIAN 5: PENCARIAN (SEARCHING)
# Sequential Search berdasarkan Nickname Player
# ============================================================
def sequential_search(data, dicari):
    i = 0
    banyakData = len(data)
    while i < banyakData and data [i][0] != dicari: # kolom Nickname Player
        i += 1
    if i < banyakData:
        return i
    else:
        return -1
    

# ============================================================
# BAGIAN 6: PROGRAM UTAMA (MENU)
# urutkan data player berdasarkan level dan cari player berdasarkan nickname
# ============================================================
while True:
    print("\n==============================")
    print("MENU MANAGEMENT PLAYER GAME")
    print("==============================")
    print("1. Input Data Player")
    print("2. Tampil Data Player")
    print("3. Urutkan Data Player berdasarkan (Level Tertinggi ke Terendah)")
    print("4. Cari Data Player berdasarkan (Nickname Player)")
    print("5. Keluar")

    pilih = int(input("Pilih menu: "))

    if pilih == 1:
        inputData(players)

    elif pilih == 2:
        tampilData(players)

    elif pilih == 3:
        insertionTurun(players, len(players))
        print("Data player telah diurutkan berdasarkan level (tertinggi ke terendah).")

    elif pilih == 4:
        nickname_cari = input("Masukkan nickname player yang dicari: ")
        posisi = sequential_search(players, nickname_cari)
        if posisi != -1:
            print("Data player ditemukan pada posisi ke-", posisi + 1)
            print("Nickname:", players[posisi][0])
            print("Level:", players[posisi][1])
            print("Inventory:", players[posisi][2])
        else:
            print("Data player dengan nickname tersebut tidak ditemukan.")

    elif pilih == 5:
        print("Keluar dari program.")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
