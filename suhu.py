suhu = input("masukan suhu, (CONTOH : 30C, 95F, 300K) : ")
derajat = int(suhu[:-1])
inputan_suhu = suhu[-1]

if inputan_suhu.upper() == "C":
  #(°C × 9/5) + 32 = °F
  hasil1 = float((derajat * 9/5) + 32)
  #°C + 273.15 = K
  hasil2 = float(derajat + 273.15)
  jenisX = "celcius"
  jenis1 = "fahrenheit"
  jenis2 = "kelvin"

elif inputan_suhu.upper() == "F":
  #(F − 32) × 5/9 = °C
  hasil1 = float((derajat - 32) * 5/9)
  #(F − 32) × 5/9 + 273.15 = K
  hasil2 = float((derajat - 32) * 5/9 + 273.15)
  jenisX = "fahrenheit"
  jenis1 = "celcius"
  jenis2 = "kelvin"

elif inputan_suhu.upper() == "K":
  #K − 273.15 = C
  hasli1 = float(derajat - 273.15)
  # (K − 273.15) × 9/5 + 32 = °F
  hasil2 = float((derajat - 273.15) * 9/5 + 32)
  jenisX = "kelvin"
  jenis1 = "celcius"
  jenis2 = "fahrenheit"

else:
  print("Inputan tidak sesuai!")

print(derajat, jenisX, "=", hasil1, jenis1)
print(derajat, jenisX, "=", hasil2, jenis2)