import numpy as np
import matplotlib.pyplot as plt


ilk_hiz = 25.0     
aci_derece = 45.0    
g = 9.81          

aci_radyan = np.deg2rad(aci_derece)


ucus_suresi = (2 * ilk_hiz * np.sin(aci_radyan)) / g


t = np.linspace(0, ucus_suresi, 100)


x_konumlari = ilk_hiz * np.cos(aci_radyan) * t
y_konumlari = (ilk_hiz * np.sin(aci_radyan) * t) - (0.5 * g * t**2)

max_yukseklik = (ilk_hiz**2 * (np.sin(aci_radyan)**2)) / (2 * g)
menzil = (ilk_hiz**2 * np.sin(2 * aci_radyan)) / g


print("--- Eğik Atış Sonuçları ---")
print("İlk Hız         : ", ilk_hiz, "m/s")
print("Atış Açısı      : ", aci_derece, "derece")
print("Uçuş Süresi     : ", round(ucus_suresi, 2), "saniye")
print("Maks Yükseklik  : ", round(max_yukseklik, 2), "metre")
print("Menzil          : ", round(menzil, 2), "metre")
print("---------------------------")

plt.figure(figsize=(10, 5))
plt.plot(x_konumlari, y_konumlari, label="Cismin Yörüngesi", color="red", linewidth=2)
plt.axhline(0, color='black', linewidth=1)
plt.title("2 Boyutlu Eğik Atış Simülasyonu")
plt.xlabel("Yatay Mesafe (m)")
plt.ylabel("Dikey Yükseklik (m)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)


plt.show()
