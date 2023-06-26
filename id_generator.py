from jinja2 import Template
import pandas as pd
import os, glob, sys
from html2image import Html2Image
import zipfile as zp
from FORMAT import *

hti = Html2Image(output_path='GENERATEDIDs/')
current_dir = os.getcwd()

arg_name = sys.argv

if len(arg_name) != 4:
    print("Please provide the zip file and excel sheet")
    exit()

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

for index, row in ID_data.head(last_val).iterrows()    :
    data = {
    'logo': f'{current_dir}/logo.webp',
    'name': ID_data.iloc[index]['Name'],
    'father_name': ID_data.iloc[index]['Fathers Name'],
    'dob': ID_data.iloc[index]['Date of birth'],
    'cet_rank': ID_data.iloc[index]['CET RANK'],
    'phone': ID_data.iloc[index]['Phone Number'],
    'course': ID_data.iloc[index]['Course '],
    'batch': ID_data.iloc[index]['Course '],
    'photo': f'{photos_folder[0]}'+ID_data.iloc[index]['Photo'],
    'signature': f'{sign_folder[0]}'+ID_data.iloc[index]['Signature'],
    'personal_address': ID_data.iloc[index]['Permanent Address']
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
