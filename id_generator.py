from jinja2 import Template
import pandas as pd
import os, glob, sys, re
from html2image import Html2Image
import zipfile as zp
import barcode
from barcode.writer import SVGWriter
from FORMAT import *

hti = Html2Image(output_path='GENERATEDIDs/')
barcode_format = barcode.get_barcode_class('code128')
current_dir = os.getcwd()

arg_name = sys.argv

if len(arg_name) != 4:
    print("Please provide the zip file and excel sheet")
    sys.exit()

zip_photos = f"{current_dir}/{arg_name[1]}"
zip_signatures = f"{current_dir}/{arg_name[2]}"
excel_sheet = f"{current_dir}/{arg_name[3]}"

destination_folder = f"{current_dir}/GENERATEDIDs"
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

with zp.ZipFile(zip_photos, "r") as zip1:
    zip1.extractall("unzip_photos")

with zp.ZipFile(zip_signatures, "r") as zip2:
    zip2.extractall("unzip_sign")


photos_folder = glob.glob(f"{current_dir}/unzip_photos/*/")
sign_folder = glob.glob(f"{current_dir}/unzip_sign/*/")


ID_data=pd.read_excel(excel_sheet)
last_val = ID_data.index[-1]
print(current_dir)

column_patterns = {
    'name': r'[Nn]ame',
    'father_name': r'[Ff]ather.',
    'dob': r'[Dd]ate [Oo]f [Bb]irth|DOB|dob|DoB',
    'rank': r'[Cc]et [Rr]ank|CET*|[Rr]ank*]',
    'number': r'[Nn]umber|[Nn]o\.?|[Pp]hone [Nn]umber|[Pp]hone|[Mm]obile*|[Mm]ob',
    'course': r'[Cc]ourse|[Cc]ourse [Nn]ame',
    'batch': r'[Bb]atch|[Bb]atch [Yy]ear',
    'photo': r'[Pp]hoto',
    'signature': r'[Ss]ignature',
    'address': r'[Pp]ermanent [Aa]ddress|[Aa]ddress|[Aa]ddress [Ll]ine'
}

for key, pattern in column_patterns.items():
        for column_header in ID_data.columns:
            if re.match(pattern, column_header):
                column_patterns[key] = column_header
                break


for index, row in ID_data.head(last_val).iterrows():
    for key, pattern in column_patterns.items():

        # Barcode generation
        rank_val = ID_data.iloc[index][column_patterns['rank']].astype(int)
        batch_val = ID_data.iloc[index][column_patterns['batch']].astype(int)
        barval = f'{rank_val}{batch_val}'
        my_barcode = barcode_format(barval, writer=SVGWriter())
        my_barcode.save(os.path.join(destination_folder, f'id_card{index}'))


        data = {
        'logo': f'{current_dir}/logo.webp',
        'name': ID_data.iloc[index][column_patterns['name']],
        'father_name': ID_data.iloc[index][column_patterns['father_name']],
        'dob': ID_data.iloc[index][column_patterns['dob']],
        'cet_rank': ID_data.iloc[index][column_patterns['rank']],
        'phone': ID_data.iloc[index][column_patterns['number']],
        'course': ID_data.iloc[index][column_patterns['course']],
        'batch': ID_data.iloc[index][column_patterns['batch']],
        'photo': f'{photos_folder[0]}'+ID_data.iloc[index][column_patterns['photo']],
        'signature': f'{sign_folder[0]}'+ID_data.iloc[index][column_patterns['signature']],
        'personal_address': ID_data.iloc[index][column_patterns['address']],
        'barcode': f'{current_dir}/GENERATEDIDs/id_card{index}.svg'
    }



    template = Template(template_html)
    output_html = template.render(data)


    generated_file_path = os.path.join(destination_folder, f'id_card{index}.html')
    with open(generated_file_path, 'w') as f:
        f.write(output_html)


x = 0
while (x <= last_val-1):
     generated_file_path = os.path.join(destination_folder, f'id_card{x}.html')
     generated_file_pdf = os.path.join(destination_folder, f'id_card{x}.jpg')
     hti.screenshot(
    html_file=generated_file_path,
    save_as=f'id_card{x}.jpg',
    size=(700, 450),
)
     x +=1

unwanted_html = glob.glob(f'{destination_folder}/*.html')
for file in unwanted_html:
    os.remove(file)
