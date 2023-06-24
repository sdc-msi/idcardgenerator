from jinja2 import Template
import pandas as pd
import os, glob
from html2image import Html2Image
import zipfile as zp
from FORMAT import *


current_dir = os.getcwd()
photos_folder = glob.glob(f"{current_dir}/ID*/Photo*/")
sign_folder = glob.glob(f"{current_dir}/ID*/Signature*/")
destination_folder = f"{current_dir}/GENERATEDIDs"

zip_photos = glob.glob('*.zip')
excel_sheet = glob.glob('*.xlsx')

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

hti = Html2Image(output_path='GENERATEDIDs/')

with zp.ZipFile(zip_photos[0], "r") as zip_ref:
    zip_ref.extractall()


ID_data=pd.read_excel(excel_sheet[0])
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
