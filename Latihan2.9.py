print (20*"=") #untuk memberikan = sebanyak 20kali
print ("INPUT NILAI MAHASIWA") #meberikan judul di awal
print (20*"=") #untuk memberikan = sebanyak 20kali

nama = input ("Nama: ") #untuk menginput nama mahasiswa dengan tipe data string
nim = int(input ("Nim: ")) #untuk menginput nama mahasiswa dengan tipe data integer
prodi = input("Prodi: ") #untuk menginput nama mahasiswa dengan tipe data string

tugas = float(input("Nilai Tugas Mahasiswa: ")) #untuk menginput nilai tugas mahasiswa dengan tipe data float
uts = float(input("Nilai UTS Mahasiswa: ")) #untuk menginput nilai uts mahasiswa dengan tipe data float
uas = float(input("Nilai UAS Mahasiswa: ")) #untuk menginput nilai uas mahasiswa dengan tipe data float

nilai = (tugas * 0.25) + (uts * 0.35) + (uas * 0.4) #lalu jumlah nilai nya di olah dengan komposisi tugas 25%,uts 35%, dan uas 40%
if (nilai >= 90) and (nilai <= 100): #lalu di berikan kondisi if else untuk menentukan hasil perhitungan nilainya masuk di grade apa
    grade = 'A'
elif (nilai >= 80) and (nilai <= 89):
    grade = 'A-'
elif (nilai >= 75) and (nilai <= 79):
    grade = 'B+'
elif (nilai >= 70) and (nilai <= 74):
    grade = 'B-'
elif (nilai >= 65) and (nilai <= 69):
    grade = 'C+'
elif (nilai >= 60) and (nilai <= 64):
    grade = 'C-'
elif (nilai >= 50) and (nilai <= 59):
    grade = 'D'
else :
    grade = 'E'

#lalu nilai akan di print beserta keterangan di bawah ini
print (20*"=")
print ("GRADE NILAI MAHASIWA")
print (20*"=")
  
print ("Nama Anda ", nama)
print ("Nim Anda ", nim)
print ("Prodi Anda ", prodi)
print ("Nilai Tugas Anda ", tugas)
print ("Nilai UTS Anda ", uts)
print ("Nilai UAS Anda", uas)
print ("Nilai Anda", nilai)
print ("Dengan GRADE", grade)