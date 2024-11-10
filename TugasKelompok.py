# DEFINISI DAN SPESIFIKASI TYPE
# type Mhs: <nim: string, nama: string, kelas: character, nilai: list of integer>
#   {type Mhs terdiri atas nim, nama, dan kelas mahasiswa, serta kumpulan nilai kuis yang pernah dikerjakan, 
# dengan maksimal jumlah mengerjakan adalah 10 kali. Nilai mahasiswa memiliki rentang antara 0-100}
# type Nilai: <

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakeMhs: <string, string, character, list of integer>  → Mhs
#   {MakeMhs(nim, nama, kelas, nilai) membentuk sebuah mahasiswa dengan dengan nim, nama, 
# kelas dan nilai berbentuk list of integer}
def MakeMhs(nim,nama,kelas,nilai):
    return [nim,nama,kelas,nilai]

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

# Definisi Spesifikasi Predikat
# IsEmpty : list ---> boolean
#   {IsEmpty(L): merupakan fungsi yang mengetahui apakah suatu list merupakan list kosong atau bukan}
def IsEmpty(L):
    return L == []

# DEFINISI DAN SPESIFIKASI SELEKTOR
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

# DEFINISI DAN SPESIFIKASI PREDIKAT
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
def konso(e, L):
    return [e] + L

# SumElmnt : list ---> integer
#   {SumElmnt(L): merupakan fungsi untuk menjumlahkan seluruh elemen dalam suatu list}
def SumElmnt(L):
    if IsEmpty(L):
        return 0
    else: 
        return FirstElmnt(L) + SumElmnt(Tail(L))

# APLIKASI BAGIAN 1


# ==================================================================================================
# BAGIAN 2
# ==================================================================================================

# Definisi dan Spesifikasi Type
# type SetMhs : <mhs>
# {type setMhs terdiri atas mahasiswa ......}

# Definisi dan Spesifikasi Konstruktor
# MakeSetMhs : List ---> Set
#   {MakeSetMhs(L): merupakan fungsi konstruktor yang membentuk set yang unik dari sebuah list}
def MakeSetMhs(L): # A
    if IsEmpty(L):
        return []
    else:
        if IsMemberNIM(NIM(FirstElmnt(L)), MakeSetMhs(Tail(L))):
            return MakeSetMhs(Tail(L))
        else:
            return konso(FirstElmnt(L),MakeSetMhs(Tail(L)))

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsMemberNIM : string, list ---> boolean
#   {IsMemberNIM(nim,mhs: merupakan fungsi predikat ... )}
def IsMemberNIM(nim,mhs): 
    if IsEmpty(mhs):
        return False
    elif NIM(FirstElmnt(mhs)) == nim:
        return True
    else:
        return IsMemberNIM(nim, Tail(mhs))

# DEFINISI DAN SPESIFIKASI OPERATOR
# banyaknilai : mhs ---> integer
#   {banyaknilai(mhs) : merupakan fungsi yang menghitung banyak nilai yang ada}
def banyaknilai(mhs): 
    if IsEmpty(Nilai(mhs)):
        return 0
    else:
        return 1 + banyaknilai(MakeMhs(NIM(mhs),Nama(mhs),Kelas(mhs),Tail(Nilai(mhs))))

# AvgNilai : mhs ---> real
#   {AvgNilai(mhs): merupakan fungsi yang menghitung rata-rata nilai yang ada}
def AvgNilai(mhs):
    if IsEmpty(Nilai(mhs)):
        return 0
    else:
        return SumElmnt(Nilai(mhs))/banyaknilai(mhs)

# MhsLulus : setmhs ---> mhs
#   {MhsLulus(mhs): merupakan fungsi untuk mengetahui siapa saja yang lulus, dengan syarat nilai > 70}
def MhsLulus(mhs): #B
    if IsEmpty(mhs):
        return[]
    else:
        if AvgNilai(FirstElmnt(mhs)) > 70:
            return konso(FirstElmnt(mhs),MhsLulus(Tail(mhs)))
        else:
            return MhsLulus(Tail(mhs))
    
# MhsTidakKuis : setmhs ---> mhs
#   {MhsTidakKuis(mhs): merupakan fungsi untuk mengetahui mahasiswa yang tidak mengikuti kuis di kelas tertentu}

def SetKelas(kelas,mhs):
    if IsEmpty(mhs): 
        return []
    else:
        if Kelas(FirstElmnt(mhs))==kelas:
            return konso(FirstElmnt(mhs),SetKelas(kelas,Tail(mhs)))
        else :
            return SetKelas(kelas,Tail(mhs))
        
def MhsTdkKuis(kelas,mhs): #C
    if IsEmpty(SetKelas(kelas,mhs)):
        return []
    else:
        if IsEmpty(Nilai(FirstElmnt(SetKelas(kelas,mhs)))):
            return konso(FirstElmnt(SetKelas(kelas,mhs)), MhsTdkKuis(kelas,Tail(SetKelas(kelas,mhs))))
        else:
            return MhsTdkKuis(kelas,Tail(SetKelas(kelas,mhs)))
        
# NilaiTertinggi : setmhs ---> integer
#   {NilaiTertinggi(mhs): merupakan fungsi untuk menghitung nilai tertinggi dari list nilai yang diberikan}
def NilaiTertinggi(mhs): #D
    if IsEmpty(Tail(mhs)):
        return AvgNilai(FirstElmnt(mhs))
    else:
        if AvgNilai(FirstElmnt(mhs)) > AvgNilai(FirstElmnt(Tail(mhs))):
            return NilaiTertinggi(konso(FirstElmnt(mhs),Tail(Tail(mhs))))
        else:
            return NilaiTertinggi(Tail(mhs))

# NilaiTertinggiKelas : setmhs ---> mhs
def NilaiTertinggiKelas(kelas,mhs):
    if IsEmpty(SetKelas(kelas,mhs)):
        return None
    else:
        if IsEmpty(Tail(SetKelas(kelas,mhs))):
            return FirstElmnt(SetKelas(kelas,mhs))
        if IsEmpty(AvgNilai(FirstElmnt(SetKelas(kelas,mhs)))):
            return NilaiTertinggiKelas(kelas,Tail(SetKelas(kelas,mhs)))
        elif AvgNilai(FirstElmnt(SetKelas(kelas,mhs))) > AvgNilai(FirstElmnt(Tail(SetKelas(kelas,mhs)))):
            return NilaiTertinggiKelas(kelas,konso(FirstElmnt(SetKelas(kelas,mhs)),Tail(Tail(SetKelas(kelas,mhs)))))
        else:
            return NilaiTertinggiKelas(kelas,Tail(SetKelas(kelas,mhs)))
        
print("Terttinggikelas" ,NilaiTertinggiKelas('A',[MakeMhs("111","Jidan","A",[90,90,90]),
                MakeMhs("122","Jidan","F",[10,10,10]), 
                MakeMhs("123","Devano","E",[100,100,100]),
                MakeMhs("2","Aryo","E",[])]))

# TotalMhsTidakKuis mhs ---> mhs
def TotalMhsTidakKuis(mhs):
    if IsEmpty(mhs):
        return[]
    else:
        if IsEmpty(Nilai(FirstElmnt(mhs))):
            return konso(FirstElmnt(mhs),TotalMhsTidakKuis(Tail(mhs)))
        else:
            return TotalMhsTidakKuis(Tail(mhs))

# print(TotalMhsTidakKuis([MakeMhs("122","Jidan","B",[]),MakeMhs("122","Jidan","B",[10,10,10])]))
# Banyak mahasiswa yang tidak mengerjakan kuis dari semua kelas
def NbMhsTidakKuis(mhs):
    if IsEmpty(mhs):
        return 0
    else:
        return 1 + NbMhsTidakKuis(Tail(TotalMhsTidakKuis(mhs)))
# banyak mahasiswa yang lulus dari semua kelas
def NBMhsLulus(mhs):
    if IsEmpty(mhs):
        return 0
    else:
        return 1+NBMhsLulus(Tail(MhsLulus(mhs)))
    
# APLIKASI BAGIAN 2
print(MhsLulus([MakeMhs("122","Jidan","B",[90,90,90]),MakeMhs("122","Jidan","B",[10,10,10])]))
print("NilaiTertinggi",NilaiTertinggi([MakeMhs("111","Jidan","C",[90,90,90]),
                MakeMhs("122","Jidan","B",[10,10,10]), 
                MakeMhs("123","Devano","D",[100,100,100]),MakeMhs("2","Aryo","E",[])]))

print (NBMhsLulus([MakeMhs("111","Jidan","C",[90,90,90]),
                MakeMhs("122","Jidan","B",[]), 
                MakeMhs("123","Devano","D",[100,100,100]),MakeMhs("2","Aryo","E",[])]))


# print(MhsTdkKuis('A',[MakeMhs("122","Jidan",'B',[]),MakeMhs("122","Jipepekdan",'B',[10,10,10]),MakeMhs("122","devano",'A',[])]))