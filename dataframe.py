import pandas as pd

df_sampah = pd.read_csv('sampah.csv')

#1
sampah_kota = df_sampah.loc[:, ['nama_kabupaten_kota','jumlah_produksi_sampah','tahun']]
print(sampah_kota)
print('')

#2
total = 0
tahun_input = int(input("Masukkan tahun untuk melihat total sampah pada tahun itu (2015 - 2023) : "))
while(tahun_input < 2015 or tahun_input > 2023) :
    tahun_input = int(input("Masukkan antara tahun 2015 - 2023 : "))

for index, row in sampah_kota.iterrows():
    if row['tahun'] == tahun_input :
        jumlah_sampah = total + row['jumlah_produksi_sampah']
        total = jumlah_sampah
        
print(f"Jumlah sampah pada tahun itu adalah = {total} ton")
print('')


#3 
tahun_jumlah = {}

for index, row in sampah_kota.iterrows() :
    tahun_jumlah[row['tahun']] = 0

for i in tahun_jumlah.keys() :
    for index, row in sampah_kota.iterrows() :
        if row['tahun'] == int(i):
            tahun_jumlah[i] = tahun_jumlah[i] + row['jumlah_produksi_sampah']

for keys, values in tahun_jumlah.items() :
    print(f"Pada tahun {keys}, total sampah berjumlah {values} ton")

print('')


#4
kota = {}

for index, row in sampah_kota.iterrows() :
    kota[row['nama_kabupaten_kota']] = []

for i in kota.keys() :
    for index, row in sampah_kota.iterrows() :
        if row['nama_kabupaten_kota'] == i:
            data = row['jumlah_produksi_sampah']
            kota[row['nama_kabupaten_kota']].append(data)


for keys, values in kota.items() :
    print(f"Pada {keys}, total sampah dimulai dari tahun 2015-2023 adalah {values}")

print('')
    

#Export
df_total = pd.DataFrame(list(tahun_jumlah.items()), columns=['tahun', 'total_sampah'])
df_kota = pd.DataFrame(kota)
df_total.to_csv('total_sampah_pertahun.csv', index=False)
df_total.to_excel('total_sampah_pertahun.xlsx', index=False)
df_kota.to_csv('total_sampah_daerah.csv', index=False)
df_kota.to_excel('total_sampah_daerah.xlsx', index=False)