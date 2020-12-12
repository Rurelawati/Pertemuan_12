# message = 'Hello World'
# print("Updated String :- ", message[:6] + 'Python')

# var1 = 'Hello World!' # penggunaan petik tunggal
# var2 = "Python Programming" # penggunaan petik ganda
# print("var1[0]: ", var1[0]) # mengambil karakter pertama
# print("var2[1:5]: ", var2[1:5]) # karakter ke-2 s/d ke-5

#  Nama        : Rurelawati
#  Kelas       : TI.20.A2
#  Mata Kuliah : Bahasa Pemrograman
 

txt = 'Hello World'
print(80*"=")
print(len(txt))
print(txt[10]) # Ambil Karakter Terakhir
print(txt[2:5]) # Ambil Karakter index ke-2 sampai index ke-4 (llo)
print(txt[:5]+'World') # Hilangkan Spasi pada text menjadi (HelloWorld)
print(txt.upper()) # Merubah txt menjadi huruf besar
print(txt.lower()) # Merubah txt menjadi huruf kecil
print(txt.replace("H", "J")) # Merubah (H) menjadi (J)


print(80*"=")
# Latihan 2
print("============>>>>>    LATIHAN 2")
print("______________________________")
umur = 20
txt = 'Hello, nama saya Mitchel, umur saya {} tahun'
print(txt.format(umur))
print(80*"=")
