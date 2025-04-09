import os
import shutil
import zipfile
import pandas as pd
from PyPDF2 import PdfReader

files_to_zip = ["import_empl_csv.csv", "import_empl_xlsx.xlsx", "Еще один важный файл.pdf"]

zip_filename = "testhw7.zip"

with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for file in files_to_zip:
        zipf.write(file)
        print(f"Архивирован: {file}")
print(f"архив '{zip_filename} создала")


project_path = '/Users/donchuleskoevgeniya/PycharmProjects/hw-7'
resources_folder = os.path.join(project_path, 'resources')
if not os.path.exists(resources_folder):
    os.makedirs(resources_folder)
    print("папка создана")


zip_file_path = os.path.join(project_path, zip_filename)
shutil.move(zip_file_path, os.path.join(resources_folder, zip_filename))

def check_pdf(file):
    try:
        reader = PdfReader(file)
        return len(reader.pages) > 0
    except Exception as e:
        print(f"Ошибка проверки файла PDF: {e}")
        return False


def check_cvs(file):
    try:
        df = pd.read_cvs(file)
        return not df.empty
    except Exception as e:
        print(f"Ошибка проверки файла CVS: {e}")
        return False

def check_xlsx(file):
    try:
        df = pd.read_excel(file)
        return not df.empty
    except Exception as e:
        print(f"Ошибка проверки файла XLSX: {e}")
        return False


zip_file_path = os.path.join(resources_folder, zip_filename)
with  zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    for file_info in zip_ref.infolist():
        file_name = file_info.filename
        print(f"Проверяем файл: {file_name}")

        if file_name.endswith('.pdf'):
            with zip_ref.open(file_name) as f:
                result = check_pdf(f)
            print(f"PDF {file_name} соответствует: {result}")

        elif file_name.endswith('.xlsx'):
            with zip_ref.open(file_name) as f:
                result = check_xlsx(f)
            print(f"XLSX {file_name} соответствует: {result}")

        elif file_name.endswith('.csv'):
            with zip_ref.open(file_name) as f:
                result = check_csv(f)  # Исправлено на check_csv
            print(f"CSV {file_name} соответствует: {result}")

        else:
            print(f"Файл {file_name} имеет неподдерживаемый формат")









