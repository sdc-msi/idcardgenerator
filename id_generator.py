from jinja2 import Template
import pandas as pd
import os, glob
from html2image import Html2Image
from FORMAT import *

hti = Html2Image(output_path='GENERATEDIDs/')
current_dir = os.getcwd()
destination_folder = f"{current_dir}/GENERATEDIDs"

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)



ID_data=pd.read_excel("student_information.xlsx")
last_val = ID_data.index[-1]
print(current_dir)

for index, row in ID_data.head(last_val).iterrows()    :
    data = {
    'logo': f'{current_dir}/logo.webp',
    'college_name': 'Maharaja Surajmal Institute',
    'about': '(Affiliated to GGSIP University, Dwarka, Delhi)',
    'college_address': 'C-4, Janakpuri, New Delhi-110058',
    'college_phone_number': 'Tel. : 011-45656183, 011-45037193',
    'name': ID_data.iloc[index]['name'],
    'father_name': ID_data.iloc[index]['father_name'],
    'dob': ID_data.iloc[index]['date_of_birth'],
    'cet_rank': ID_data.iloc[index]['cet_rank'],
    'phone': ID_data.iloc[index]['phone_number'],
    'course': ID_data.iloc[index]['course'],
    'batch': ID_data.iloc[index]['batch'],
    'photo': f'{current_dir}/photos/'+ID_data.iloc[index]['photograph'],
    'signature': f'{current_dir}/sign/'+ID_data.iloc[index]['digital_sign'],
    'personal_address': ID_data.iloc[index]['address']
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

