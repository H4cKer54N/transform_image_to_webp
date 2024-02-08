from PIL import Image
import os

def convert_and_compress_png_to_webp(input_path, output_path, quality=60, lossless=False):
    with Image.open(input_path) as img:
        if img.mode != 'RGB':
            img = img.convert('RGB')
        img.save(output_path, 'webp', quality=quality, lossless=lossless)

def process_directory(input_directory, output_directory, quality=60, lossless=False):
    # Crear el directorio de salida si no existe
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Procesar cada archivo en el directorio de entrada
    for filename in os.listdir(input_directory):
        if filename.lower().endswith('.png') or filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg') or filename.lower().endswith('.webp'):
            input_file = os.path.join(input_directory, filename)
            output_file = os.path.join(output_directory, os.path.splitext(filename)[0] + '.webp')
            convert_and_compress_png_to_webp(input_file, output_file, quality, lossless)
            print(f"Convertido: {input_file} a {output_file}")

# Rutas de los directorios de entrada y salida
input_directory = './'
output_directory = './processed_images/'

# Convertir y comprimir todos los archivos PNG en la carpeta
process_directory(input_directory, output_directory, quality=60, lossless=False)
