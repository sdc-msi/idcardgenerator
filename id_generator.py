from jinja2 import Template
import pandas as pd
import os
from html2image import Html2Image

hti = Html2Image(output_path='GENERATEDIDs/')
current_dir = os.getcwd()
destination_folder = "GENERATEDIDs"

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

template_html = """
<!DOCTYPE html>
<html>
<head>
    <title>ID Card</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
            margin: 0;
            padding: 0;
        }

        @page {
            /* dimensions for the whole page */
            size: 74mm 51.7mm;
            margin: 0;
        }

        .page-layout {
            width: 700px;
            height: 450px;
            background-color: white;
            border: 1px solid #ccc;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            padding: 20px;
            box-sizing: border-box;
        }

/* This Section is for the college part  */

        .top-block {
         text-align: center;
         display: flex;
            }

        .college-logo {
            float: left;
            width: 130px;
            height: 125px;
            margin-right: 30px;
        }

        .college-info {
            width: 70%;
            float: right;
        }

        .college-name {
            font-size: 32px;
            font-weight: bold;
            color: #0000ff;
        }

        .about {
            font-size: 14px;
            color: #00ff00;
            margin-top: 5px;
        }

        .college-address {
            font-size: 14px;
            color: #ff0000;
        }

        .college-phone-number {
            font-size: 14px;
            color: #ff0000;
            margin-top: 5px;
        }

/* This Section is for personal information */

        .bottom-block {
            text-align: left`;
            display: flex;
        }

        .personal-info {
            width: 60%;
            float: right;
        }

        .personal-photo {
            width: 40%;
            float: right;
            }


        .name {
            font-size: 20px;
            font-weight: bold;
            margin-top: 15px;
        }

        .info {
            font-size: 16px;
            margin-top: 10px;
        }

        .photo {
            width: 160px;
            height: 145px;
            margin-top: 10px;
        }

        .signature {
            width: 160px;
            height: 50px;
            margin-top: 10px;
        }

/* This Section is for miscellaneous  */



        .line {
            margin-top: 15px;
            border-top: 2px solid #00ff00;
        }


    </style>
</head>
<body>
    <div class="page-layout">
        <div class="top-block">
            <img class="college-logo" src="{{ logo }}" alt="Logo">
            <div class="college-info">
                <div class="college-name">{{ college_name }}</div>
                <div class="about">{{ about }}</div>
                <div class="college-address">{{ college_address }}</div>
                <div class="college-phone-number">{{ college_phone_number }}</div>
            </div>
        </div>
    <div class="line"></div>
        <div class="bottom-block">
            <div class="personal-photo">
                <img class="photo" src="{{ photo }}" alt="Photo">
                <br>
                <img class="signature" src="{{ signature }}" alt="Signature">
            </div>

            <div class="personal-info">
                <div class="name">Name: {{ name }}</div>
                <div class="info">Father's Name: {{ father_name }}</div>
                <div class="info">Date of Birth: {{ dob }}</div>
                <div class="info">CET Rank: {{ cet_rank }}</div>
                <div class="info">Phone Number: {{ phone }}</div>
                <div class="info">Course: {{ course }}</div>
                <div class="info">Batch: {{ batch }}</div>
                <div class="info">Res Address: {{ personal_address }}</div>
            </div>

        </div>
    </div>
</body>
</html>
"""

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
    size=(800, 400),
)
     x +=1














'''
pdfoption = {

    "enable-local-file-access": None,
    'format': 'jpg',
    }

x = 0
while (x <= last_val-1):
     generated_file_path = os.path.join(destination_folder, f'id_card{x}.html')
     print(generated_file_path)
     generated_file_pdf = os.path.join(destination_folder, f'id_card{x}.jpg')
     imgkit.from_file(generated_file_path, generated_file_pdf,  options=pdfoption)
     x +=1
'''