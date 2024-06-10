def create_map():
    # Membuat peta dengan titik pusat di koordinat tertentu
    peta = folium.Map(location=[-
    peta = folium.Map(locat

    peta = folium.Ma

    peta = fo

    pe
6.200000, 106.816666], zoom_start=10)

    

  
# Menambahkan marker ke peta
    folium.Marker(
        location=[-
    folium.Marker(
        location=[-

    folium.Marker(
        loc

    folium.Marker(
   

    folium.Mar

    fo
6.200000, 106.816666],
        popup=
        p

 
'Jakarta',
        icon=folium.Icon(icon=
        icon=folium.Icon

        icon=fol

        
'info-sign')
    ).add_to(peta)

    
    ).add_to(peta)

   

    ).add_to(peta)


    ).add_to(peta

    ).add_to

    ).a

  
# Menyimpan peta ke file HTML
    peta.save(
    p
'peta.html')

    

   
print("Peta telah dibuat dan disimpan sebagai peta.html")

if __name__ == "__main__":
    create_map()
