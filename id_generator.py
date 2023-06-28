from jinja2 import Template
import pandas as pd
import os, glob, sys, re
from html2image import Html2Image
import zipfile as zp
from FORMAT import *

hti = Html2Image(output_path='GENERATEDIDs/')
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

NAME = r'[Nn]ame'
FATHER_NAME = r'[Ff]ather*'
DOB = r'[Dd]ate [Oo]f [Bb]irth|DOB|dob|DoB'
RANK = r'[Cc]et [Rr]ank|CET*|[Rr]ank*]'
NUMBER = r'[Nn]umber|[Nn]o.|[Nn]o|[Pp]hone [Nn]umber|[Pp]hone|[Mm]obile*|[Mm]ob'
COURSE = r'[Cc]ourse|[Cc]ourse [Nn]ame'
BATCH = r'[Bb]atch|[Bb]atch [Yy]ear'
PHOTO = r'[Pp]hoto'
SIGNATURE = r'[Ss]ignature'
ADDRESS = r'[Pp]ermanent [Aa]ddress|[Aa]ddress|[Aa]ddress [Ll]ine'


for columns_header in ID_data.columns:
    if re.match(NAME, columns_header):
        name = columns_header
    if re.match(FATHER_NAME, columns_header):
        father_name = columns_header
    if re.match(DOB, columns_header):
        dob = columns_header
    if re.match(RANK, columns_header):
        rank = columns_header
    if re.match(NUMBER, columns_header):
        number = columns_header
    if re.match(COURSE, columns_header):
        course = columns_header
    #THIS IS FOR BATCH BUT NEEDS TO BE CHANGED
    if re.match(COURSE, columns_header):
        batch = columns_header
    if re.match(PHOTO, columns_header):
        photo = columns_header
    if re.match(SIGNATURE, columns_header):
        signature = columns_header
    if re.match(ADDRESS, columns_header):
        address = columns_header

for index, row in ID_data.head(last_val).iterrows()    :

    data = {
    'logo': f'{current_dir}/logo.webp',
    'name': ID_data.iloc[index][name],
    'father_name': ID_data.iloc[index][father_name],
    'dob': ID_data.iloc[index][dob],
    'cet_rank': ID_data.iloc[index][rank],
    'phone': ID_data.iloc[index][number],
    'course': ID_data.iloc[index][course],
    'batch': ID_data.iloc[index][batch],
    'photo': f'{photos_folder[0]}'+ID_data.iloc[index][photo],
    'signature': f'{sign_folder[0]}'+ID_data.iloc[index][signature],
    'personal_address': ID_data.iloc[index][address]
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
