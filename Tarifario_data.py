import requests
import pandas as pd

# Obtener el contenido de la página web solo una vez
url = "https://tarifario.org/"
response = requests.get(url)

# Extraer las tablas de la página
tables = pd.read_html(response.text)

# Procesar las tablas como antes
columns = ["Concept", "Client A", "Client B", "Client C", "Consult", "Category", "Subcategory"]
categories = ["Diseño Audiovisual", "Diseño Gráfico", "Diseño Gráfico", "Editorial", "Identidad", "Identidad", "Identidad",
              "Ilustración", "Ilustración", "Ilustración", "Ilustración", "Multimedia", "Fotografia", "Multimedia", "Multimedia", "Video",
              "Papelería", "Papelería", "Papelería", "Publicidad", "Publicidad", "Publicidad", "Hourly Rates", "Web", "Web", "Web", "Web",
              "Marketing", "Redacción", "Redes Sociales", "Programación"]

subcategories = ["Audio", "Merchandising", "Packaging", "Piezas Editoriales", "Corporativa", "Otros Servicios de Identidad",
                 "Señalética", "A Mano Alzada", "Ilustración 3D", "Ilustración Vectorial", "Otros Servicios de Ilustración",
                 "Presentación Digital", "Fotografía", "Multimedia 3D", "Otros Servicios Multimedia",
                 "Video", "Básica", "Comercial", "Comunicación", "Cartelería", "Editorial", "Folletería", "Hourly Rates",
                 "Banners", "Diseño y Maquetación", "Flash", "Otros Servicios Web", "Identidad Corporativa", "Redacción",
                 "Redes Sociales", "Web"]

df = pd.DataFrame(columns=columns)

for i in range(len(categories)):
    table_web = tables[i]
    table_web["Category"] = [categories[i] for x in range(len(table_web))]
    table_web["Subcategory"] = [subcategories[i] for x in range(len(table_web))]
    table_web.columns = columns
    df = pd.concat([df, table_web], ignore_index=True)

# Limpiar los valores monetarios
for i in ["Client A", "Client B", "Client C"]:
    df[i] = df[i].str.replace("$", "").str.replace(",", "").str.replace("-", "0").astype(int)

# Reorganizar las columnas
df = df[["Category", "Subcategory", "Concept", "Client A", "Client B", "Client C"]]

# Guardar el DataFrame a un CSV
df.to_csv('tarifario_data.csv', index=False)

# Mostrar el DataFrame
print(df)