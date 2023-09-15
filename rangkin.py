print ("tugas rangking nilai")
print ("-----------------------------------------")

nama = input ("Nama: ")
nim = int(input ("Nim: "))
prodi = input("Prodi: ")


# nilai = float(input ("Masukan Nilai: "))

tugas = float(input("Nilai Tugas: "))
uts = float(input("Nilai Uts: "))
uas = float(input("Nilai Uas: "))

nilai = (tugas * 0.25) + (uts * 0.35) + (uas * 0.4)

if (nilai >= 90) and (nilai <= 100):
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
    
print ("Nama Anda ", nama)
print ("Nim Anda ", nim)
print ("Prodi Anda ", prodi)
print ("Nilai Tugas Anda ", tugas)
print ("Nilai Uts Anda ", uts)
print ("Nilai Uas Anda", uas)
print ("Nilai anda", nilai)
print ("Dengan grade", grade)