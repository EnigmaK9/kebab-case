import os
import re

def to_kebab_case(s):
    # Convierte la cadena a minúsculas y reemplaza espacios y caracteres especiales con guiones
    s = re.sub(r'[\s_]+', '-', s)
    s = re.sub(r'[^\w-]', '', s)
    return s.lower()

def rename_files_in_directory(directory):
    for filename in os.listdir(directory):
        # Obtiene la ruta completa del archivo
        full_path = os.path.join(directory, filename)
        if os.path.isfile(full_path):
            # Divide el nombre del archivo y la extensión
            name, ext = os.path.splitext(filename)
            # Convierte el nombre a kebab case
            kebab_name = to_kebab_case(name)
            # Genera el nuevo nombre del archivo
            new_filename = kebab_name + ext
            new_full_path = os.path.join(directory, new_filename)
            # Renombra el archivo
            os.rename(full_path, new_full_path)
            print(f'Renamed: {filename} -> {new_filename}')

# Especifica el directorio que contiene los archivos
directory_path = '/home/enigma/repos/rosalia/video-scrapper/vocals-only'
rename_files_in_directory(directory_path)

