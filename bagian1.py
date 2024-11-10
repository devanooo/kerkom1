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

# print((MakeMhs('123','biyani','B',[90])))

# Definisi Spesifikasi Predikat
def Isempty(L):
    return L == []
def Tail(L):
    if Isempty(L):
        return []
    else : return L[1:]

def FirstElmnt(L):
    if Isempty(L):
        return None
    else : 
        return L[0]
def IsMember(n,L):
    if n == FirstElmnt(L):
        return True
    elif Isempty(L):
        return False
    else:
        return IsMember(n,Tail(L))
def konso(e, L):
    return [e] + L

def SumElmnt(L):
    if Isempty(L):
        return 0
    else: 
        return FirstElmnt(L) + SumElmnt(Tail(L))
## Bagian 2

# Definisi dan Spesifikasi Type
# type SetMhs : <mhs>
# {type setMhs terdiri atas mahasiswa ......}

# Definisi dan Spesifikasi Konstruktor
# MakeSetMhs : ....
# {...}
def IsMemberNIM(nim,mhs):
    if Isempty(mhs):
        return False
    elif NIM(FirstElmnt(mhs)) == nim:
        return True
    else:
        return IsMemberNIM(nim, Tail(mhs))

def MakeSetMhs(L):
    if Isempty(L):
        return []
    else:
        if IsMemberNIM(NIM(FirstElmnt(L)), MakeSetMhs(Tail(L))):
            return MakeSetMhs(Tail(L))
        else:
            return konso(FirstElmnt(L),MakeSetMhs(Tail(L)))

def banyaknilai(mhs):
    if Isempty(Nilai(mhs)):
        return 0
    else:
        return 1 + banyaknilai(MakeMhs(NIM(mhs),Nama(mhs),Kelas(mhs),Tail(Nilai(mhs))))

def AvgNilai(mhs):
    if Isempty(Nilai(mhs)):
        return 0
    else:
        return SumElmnt(Nilai(mhs))/banyaknilai(mhs)

# print("avg",AvgNilai(MakeMhs("122","Jidan","B",[10,10,10])))
# print(banyaknilai(MakeMhs("122","Jidan","B",[90,90,90])))

def MhsLulus(mhs):
    if Isempty(mhs):
        return[]
    else:
        if AvgNilai(FirstElmnt(mhs)) > 70:
            return konso(FirstElmnt(mhs),MhsLulus(Tail(mhs)))
        else:
            return MhsLulus(Tail(mhs))
print(MhsLulus([MakeMhs("122","Jidan","B",[90,90,90]),MakeMhs("122","Jidan","B",[10,10,10])]))

def TidakKuis(mhs):
    if Isempty(mhs):
        return[]
    else:
        if Isempty(Nilai(FirstElmnt(mhs))):
            return konso(FirstElmnt(mhs),TidakKuis(Tail(mhs)))
        else:
            return TidakKuis(Tail(mhs))

print(TidakKuis([MakeMhs("122","Jidan","B",[]),MakeMhs("122","Jidan","B",[10,10,10])]))

    
def maxelmt(mhs):
    if Isempty(mhs):
        return None
    elif Isempty(Tail(mhs)):
        return FirstElmnt(mhs)
    else:
        if FirstElmnt(mhs) > maxelmt(Tail(mhs)):
            return FirstElmnt(mhs)
        else: 
            return maxelmt(Tail(mhs))
            
def nilaitertinggi(mhs):
    if Isempty(Tail(mhs)):
        return AvgNilai(FirstElmnt(mhs))
    else:
        if AvgNilai(FirstElmnt(mhs)) > AvgNilai(FirstElmnt(Tail(mhs))):
            return nilaitertinggi(konso(FirstElmnt(mhs),Tail(Tail(mhs))))
        else:
            return nilaitertinggi(Tail(mhs))

def nilaitertinggikelas(kelas,mhs):
    return

# No gw blm sholat bntr sama mau makan gacoan(kudus ada gacoan anjay)
# print(nilaitertinggi([MakeMhs("123",'Devano','A',[20]),
#                   MakeMhs("122","Jidan","B",[25,10]),
#                   MakeMhs("123",'Devano','A',[90,80])]))
# [mhs1,mhs2] maxelemnt(avgnilai(mhs))
# print(maxelmt([1,2,3,4,5]))
#tes jidan 
# print(MakeSetMhs([MakeMhs("123",'Devano','A',[20]),
#                   MakeMhs("122","Jidan","B",[25,30]),
#                   MakeMhs("123",'Devano','A',[20])]))