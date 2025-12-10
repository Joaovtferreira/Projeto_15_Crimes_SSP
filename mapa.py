import folium

def create_map(coordinates):
    lat_center = coordinates['LATITUDE'].median()
    lon_center = coordinates['LONGITUDE'].median()

    m = folium.Map(location=[lat_center, lon_center], zoom_start=13)

    for _, row in coordinates.iterrows():
        
        popup_html = f"""
            <b>{row['NATUREZA_APURADA']}</b><br>
            Período: {row['DESC_PERIODO']} <br>
            Local: {row['DESCR_SUBTIPOLOCAL']} <br>
            Data: {row['DATA_OCORRENCIA_BO'].date()} <br>
            
        """
        folium.Marker(
            location=[row['LATITUDE'], row['LONGITUDE']],
            popup=popup_html
        ).add_to(m)

    m.save("mapa.html")