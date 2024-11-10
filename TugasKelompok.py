# ======================================================================================
# BAGIAN 1
# ======================================================================================

# TYPE MAHASISWA

# DEFINISI DAN SPESIFIKASI TYPE
# type Mhs: <nim: string, nama: string, kelas: character, nilai: list of integer>
#   {type Mhs terdiri atas nim, nama, dan kelas mahasiswa, serta kumpulan nilai kuis yang pernah dikerjakan, 
# dengan maksimal jumlah mengerjakan adalah 10 kali. Nilai mahasiswa memiliki rentang antara 0-100}

# DEFINISI DAN SPESIFIKASI SELEKTOR
# NIM: Mhs → string
#   {NIM(mhs) mengambil elemen NIM dari Mhs}
def NIM(mhs):
    return mhs[0]

# Nama: Mhs → string
#   {Nama(mhs) mengambil elemen Nama dari Mhs}
def Nama(mhs):
    return mhs[1]

# Kelas: Mhs → character
#   {Kelas(mhs) mengambil elemen Kelas dari Mhs}
def Kelas(mhs):
    return mhs[2]

# Nilai: Mhs → NKuis
#   {Nilai(mhs) mengambil elemen Nilai dari Mhs}
def Nilai(mhs):
    return mhs[3]

# NKuis1: Nilai → integer
#   {NKuis1(mhs) mengambil elemen nilai kuis pertama dari Nilai}
def NKuis1(mhs):
    if mhs[3] == []:
        return []
    else:
        return mhs[3][0]

# Tail : list ---> list
#   {Tail(L): merupakan fungsi untuk mengambil list tapa first elementnya}
def Tail(L):
    if IsEmpty(L):
        return []
    else : return L[1:]

# FirstElmnt : list ---> integer
#   {FirstElmnt(L): merupakan fungsi selektor yang mengambil element pertama dari suatu list yang diberikan}
def FirstElmnt(L):
    if IsEmpty(L):
        return None
    else : 
        return L[0]
    

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakeMhs: <string, string, character, list of integer> ---> Mhs
#   {MakeMhs(nim, nama, kelas, nilai) membentuk sebuah mahasiswa dengan dengan nim, nama, 
# kelas dan nilai berbentuk list of integer}
def MakeMhs(nim,nama,kelas,nilai):
    return [nim,nama,kelas,nilai]

# konso : elemen, list ---> list
#   {konso(e, L): menghasilkan sebuah list dari edan L, dengan e sebagai element pertama, e: e o L ---> L'}
def konso(e, L):
    return [e] + L


# Definisi Spesifikasi Predikat
# IsEmpty : list ---> boolean
#   {IsEmpty(L): merupakan fungsi yang mengetahui apakah suatu list merupakan list kosong atau bukan}
def IsEmpty(L):
    return L == []

# IsMember : integer, list ---> boolean
#   {IsMember(n,L): merupakan fungsi predikat untuk mengecek apakah suatu element itu mmerupakan anggota dari suatu list yang 
# diberikan}
def IsMember(n,L):
    if n == FirstElmnt(L):
        return True
    elif IsEmpty(L):
        return False
    else:
        return IsMember(n,Tail(L))
    

# DEFINISI DAN SPESIFIKASI OPERATOR
# SumElmnt : list ---> integer
#   {SumElmnt(L): merupakan fungsi untuk menjumlahkan seluruh elemen dalam suatu list}
def SumElmnt(L):
    if IsEmpty(L):
        return 0
    else: 
        return FirstElmnt(L) + SumElmnt(Tail(L))



# ==================================================================================================
# BAGIAN 2
# ==================================================================================================


# DEFINISI DAN SPESIFIKASI TYPE
# type SetMhs : <mhs>
# {type SetMhs : <mhs> merupakan type set yang berisi list mahasiswa yang unik (tidak ada yang sama)}


# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakeSetMhs : List ---> SetMhs
#   {MakeSetMhs(L): merupakan fungsi konstruktor yang membentuk set yang unik dari sebuah list}
def MakeSetMhs(L): # JAWABAN A
    if IsEmpty(L):
        return []
    else:
        if IsMemberNIM(NIM(FirstElmnt(L)), MakeSetMhs(Tail(L))):
            return MakeSetMhs(Tail(L))
        else:
            return konso(FirstElmnt(L),MakeSetMhs(Tail(L)))


# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsMemberNIM : string, SetMhs ---> boolean
#   {IsMemberNIM(nim,mhs): merupakan fungsi predikat untuk mengecek apakah suatu nim yang berbentuk string bagian dari suatu set)}
def IsMemberNIM(nim,mhs): 
    if IsEmpty(mhs):
        return False
    elif NIM(FirstElmnt(mhs)) == nim:
        return True
    else:
        return IsMemberNIM(nim, Tail(mhs))


# DEFINISI DAN SPESIFIKASI OPERATOR
# banyaknilai : SetMhs ---> integer
#   {banyaknilai(mhs) : merupakan fungsi yang menghitung banyak nilai yang ada}
def BanyakNilai(mhs): 
    if IsEmpty(Nilai(mhs)):
        return 0
    else:
        return 1 + BanyakNilai(MakeMhs(NIM(mhs),Nama(mhs),Kelas(mhs),Tail(Nilai(mhs))))

# AvgNilai : SetMhs ---> real
#   {AvgNilai(mhs): merupakan fungsi yang menghitung rata-rata nilai yang ada}
def AvgNilai(mhs):
    if IsEmpty(Nilai(mhs)):
        return 0
    else:
        return SumElmnt(Nilai(mhs))/BanyakNilai(mhs)

# MhsLulus : SetMhs ---> SetMhs
#   {MhsLulus(mhs): merupakan fungsi untuk mengetahui siapa saja yang lulus, dengan syarat nilai > 70}
def MhsLulus(mhs): # JAWABAN B
    if IsEmpty(mhs):
        return[]
    else:
        if AvgNilai(FirstElmnt(mhs)) > 70:
            return konso(FirstElmnt(mhs),MhsLulus(Tail(mhs)))
        else:
            return MhsLulus(Tail(mhs))
    
# SetKelas : char, SetMhs ---> SetMhs
#   {SetKelas(kelas,mhs): merupakan fungsi untuk membentuk set dari tipe character dan list}
def SetKelas(kelas,mhs):
    if IsEmpty(mhs): 
        return []
    else:
        if Kelas(FirstElmnt(mhs))==kelas:
            return konso(FirstElmnt(mhs),SetKelas(kelas,Tail(mhs)))
        else :
            return SetKelas(kelas,Tail(mhs))

# MhsTidakKuis : SetMhs ---> SetMhs
#   {MhsTidakKuis(mhs): merupakan fungsi untuk mengetahui mahasiswa yang tidak mengikuti kuis di kelas tertentu}
def MhsTdkKuis(kelas,mhs): # JAWABAN C
    if IsEmpty(SetKelas(kelas,mhs)):
        return []
    else:
        if IsEmpty(Nilai(FirstElmnt(SetKelas(kelas,mhs)))):
            return konso(FirstElmnt(SetKelas(kelas,mhs)), MhsTdkKuis(kelas,Tail(SetKelas(kelas,mhs))))
        else:
            return MhsTdkKuis(kelas,Tail(SetKelas(kelas,mhs)))
        
# NilaiTertinggi : SetMhs ---> integer
#   {NilaiTertinggi(mhs): merupakan fungsi untuk menghitung nilai tertinggi dari list nilai yang diberikan}
def NilaiTertinggi(mhs): # JAWABAN D
    if IsEmpty(Tail(mhs)):
        return AvgNilai(FirstElmnt(mhs))
    else:
        if AvgNilai(FirstElmnt(mhs)) > AvgNilai(FirstElmnt(Tail(mhs))):
            return NilaiTertinggi(konso(FirstElmnt(mhs),Tail(Tail(mhs))))
        else:
            return NilaiTertinggi(Tail(mhs))

# NilaiTertinggiKelas : SetMhs ---> SetMhs
#   {NilaiTertinggiKelas(kelas,mhs): merupakan fungsi untuk mengetahui set yang mengandung nilai tertinggi}
def NilaiTertinggiKelas(kelas,mhs):
    if IsEmpty(SetKelas(kelas,mhs)):
        return None
    else:
        if IsEmpty(Tail(SetKelas(kelas,mhs))):
            return FirstElmnt(SetKelas(kelas,mhs))
        elif IsEmpty(AvgNilai(FirstElmnt(SetKelas(kelas,mhs)))):
            return NilaiTertinggiKelas(kelas,Tail(SetKelas(kelas,mhs)))
        elif AvgNilai(FirstElmnt(SetKelas(kelas,mhs))) > AvgNilai(FirstElmnt(Tail(SetKelas(kelas,mhs)))):
            return NilaiTertinggiKelas(kelas,konso(FirstElmnt(SetKelas(kelas,mhs)),Tail(Tail(SetKelas(kelas,mhs)))))
        else:
            return NilaiTertinggiKelas(kelas,Tail(SetKelas(kelas,mhs)))

# TotalMhsTidakKuis SetMhs ---> SetMhs
#   {TotalMhsTidakKuis(mhs): merupakan fungsi untuk menghitung berapa mahasiswa yang tidak mengikuti kuis}
def TotalMhsTidakKuis(mhs):
    if IsEmpty(mhs):
        return[]
    else:
        if IsEmpty(Nilai(FirstElmnt(mhs))):
            return konso(FirstElmnt(mhs),TotalMhsTidakKuis(Tail(mhs)))
        else:
            return TotalMhsTidakKuis(Tail(mhs))

# NbMhsTidakKuis : SetMhs ---> integer
#   {NbMhsTidakKuis(mhs): merupakan fungsi untuk menghitung jumlah mahasiswa yang tidak mengikuti kuis dari suatu SetMhs yang diberikan}
def NbMhsTidakKuis(mhs):
    if IsEmpty(mhs):
        return 0
    else:
        return 1 + NbMhsTidakKuis(Tail(TotalMhsTidakKuis(mhs)))

# NBMhsLulus : SetMhs ---> integer
#   {NBMhsLulus(mhs):  merupakan fungsi untuk menghitung jumlah mahasiswa yang lulus}
def NBMhsLulus(mhs):
    if IsEmpty(mhs):
        return 0
    else:
        return 1 + NBMhsLulus(Tail(MhsLulus(mhs)))
    
# APLIKASI BAGIAN 2
print(MhsLulus([MakeMhs("122","Jidan","B",[90,90,90]),MakeMhs("122","Yummy","B",[10,10,10])]))
print(MhsLulus([MakeMhs("122","Jidan","B",[70,100,98]),MakeMhs("122","Cell","B",[100,100,100])]))
print(MhsLulus([MakeMhs("122","Jidan","B",[98,88,50]),MakeMhs("122","Dua","B",[60,60,100])]))
print("NilaiTertinggi",NilaiTertinggi([MakeMhs("111","Jidan","C",[90,90,90]),
                                       MakeMhs("122","Bayu","B",[10,10,10]), 
                                       MakeMhs("123","Devanoto","D",[100,100,100]),
                                       MakeMhs("2","Aryo","E",[])]))
print("NilaiTertinggi",NilaiTertinggi([MakeMhs("111","Jidan","C",[60,100,99]),
                                       MakeMhs("122","Sair","B",[99,99,99]), 
                                       MakeMhs("123","Wahyu","D",[100,99,98]),
                                       MakeMhs("2","Dewi","E",[])]))
print("NilaiTertinggi",NilaiTertinggi([MakeMhs("111","Jidan","C",[88,99,87]),
                                       MakeMhs("122","Garong","B",[87,10,100]), 
                                       MakeMhs("123","Yuni","D",[80,81,82]),
                                       MakeMhs("2","Sarah","E",[])]))
print(MhsTdkKuis("B", [MakeMhs("123", "Daniel", "B", [90,95,98]), 
                       MakeMhs("246", "Devanoot", "C", [98,98,97]), 
                       MakeMhs("145", "Dehar", "B", [])]))
print(MhsTdkKuis("B", [MakeMhs("123", "Daniel", "B", [89,90,91]), 
                       MakeMhs("246", "Devanoot", "C", [92,93,94]), 
                       MakeMhs("145", "Dehar", "B", [])]))
print(MhsTdkKuis("B", [MakeMhs("123", "Daniel", "B", [98,99,100]), 
                       MakeMhs("246", "Devanoot", "C", [98,100,98]), 
                       MakeMhs("145", "Dehar", "B", [])]))
print(NilaiTertinggiKelas("B", [MakeMhs("123", "Daniel", "B", [90,95,98]), 
                                MakeMhs("246", "Devanoot", "C", [98,98,97]), 
                                MakeMhs("145", "Biyani", "B", [90,99,100])]))
print(NilaiTertinggiKelas("B", [MakeMhs("123", "Daniel", "B", [96,97,98]), 
                                MakeMhs("246", "Devanoot", "C", [98,99,97]), 
                                MakeMhs("145", "Biyani", "B", [90,99,100])]))
print(NilaiTertinggiKelas("B", [MakeMhs("123", "Daniel", "B", [95,95,98]), 
                                MakeMhs("246", "Devanoot", "C", [95,95,95]), 
                                MakeMhs("145", "Biyani", "B", [100,99,100])]))
print (NBMhsLulus([MakeMhs("111","Jidan","C",[100,100,100]),
                   MakeMhs("122","Jidan","B",[]), 
                   MakeMhs("123","Devano","D",[95,80,100]),
                   MakeMhs("2","Aryo","E",[])]))
print (NBMhsLulus([MakeMhs("111","Jidan","C",[77,75,100]),
                   MakeMhs("122","Jidan","B",[]), 
                   MakeMhs("123","Devano","D",[88,65,87]),
                   MakeMhs("2","Aryo","E",[])]))
print (NBMhsLulus([MakeMhs("111","Jidan","C",[98,94,92]),
                   MakeMhs("122","Jidan","B",[]), 
                   MakeMhs("123","Devano","D",[20,68,90]),
                   MakeMhs("2","Aryo","E",[])]))
print(TotalMhsTidakKuis([MakeMhs("122","Jidan","B",[]),MakeMhs("122","Biyani","B",[])]))
print(TotalMhsTidakKuis([MakeMhs("122","Jidan","B",[10,10,20]),MakeMhs("122","Biyani","B",[10,10,10])]))
print(TotalMhsTidakKuis([MakeMhs("122","Jidan","B",[1,2,3]),MakeMhs("122","Biyani","B",[])]))
print(NbMhsTidakKuis([MakeMhs("122","Bayu","B",[]),MakeMhs("122","Daniel","B",[100,90,91])]))
print(NbMhsTidakKuis([MakeMhs("122","Bayu","B",[]),MakeMhs("122","Sarah","B",[])]))
print(NbMhsTidakKuis([MakeMhs("122","Bayu","B",[1,2,3]),MakeMhs("122","Bambang","B",[])]))
print(NBMhsLulus([MakeMhs("12345", "Bayu", "B", [75,72,100]), 
                  MakeMhs("6789", "Devanoot", "C", [60,89,81]), 
                  MakeMhs("1452", "Dehar", "E", [82,83,84])]))
print(NBMhsLulus([MakeMhs("12345", "Bayu", "B", [1,2,3]), 
                  MakeMhs("6789", "Devanoot", "C", [4,5,6]), 
                  MakeMhs("1452", "Dehar", "E", [100,100,100])]))
print(NBMhsLulus([MakeMhs("12345", "Bayu", "B", [100,100,100]), 
                  MakeMhs("6789", "Devanoot", "C", [100,100,100]), 
                  MakeMhs("1452", "Dehar", "E", [])]))
