from jinja2 import Template

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

        .top-section {
            display: flex;
            flex-direction: row;
            }

        .id-card {

            width: 800px;
            height: 400px;
            background-color: white;
            border: 1px solid #ccc;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            padding: 20px;
            box-sizing: border-box;
        }

        .logo {
            flex = 1;
            align-self: flex-start;
            width: 115px;
            height: 112px;
            margin-right: 20px;
        }

        .College-block {
            justify-content: center;
        }


        .institute-name {
            font-size: 24px;
            font-weight: bold;
            color: #0000ff;
        }

        .about {
            font-size: 12px;
            color: #00ff00;
            margin-top: 5px;
        }

        .address {
            font-size: 12px;
            color: #ff0000;
        }

        .phone-number {
            font-size: 12px;
            color: #ff0000;
            margin-top: 5px;
        }

        .line {
            margin-top: 15px;
            border-top: 2px solid #00ff00;
        }

        .info-block {
            display: flex;
            flex-direction: row;
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
            width: 125px;
            height: 120px;
            margin-top: 10px;
        }

        .signature {
            width: 125px;
            height: 50px;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <div class="id-card">
    <div class="top-section">
        <img class="logo" src="{{ logo }}" alt="Logo">
        <div class="College-block">
            <div class="institute-name">{{ institute_name }}</div>
            <div class="about">{{ about }}</div>
            <div class="address">{{ address }}</div>
            <div class="phone-number">{{ phone_number }}</div>
        </div>
    </div>
        <div class="line"></div>
    <div class="info-block">
        <div class="personal-info">
            <div class="name">Name: {{ name }}</div>
            <div class="info">Father's Name: {{ father_name }}</div>
            <div class="info">Date of Birth: {{ dob }}</div>
            <div class="info">CET Rank: {{ cet_rank }}</div>
            <div class="info">Phone Number: {{ phone }}</div>
            <div class="info">Course: {{ course }}</div>
            <div class="info">Batch: {{ batch }}</div>
            <div class="info">Res Address: {{ address }}</div>

        </div>
        <img class="photo" src="{{ photo }}" alt="Photo">
        <img class="signature" src="{{ signature }}" alt="Signature">
    </div>
    </div>
</body>
</html>
"""


data = {
    'logo': 'logo.jpg',
    'institute_name': 'Maharaja Surajmal Institute',
    'about': '(Affiliated to GGSIP University, Dwarka, Delhi)',
    'address': 'C-4, Janakpuri, New Delhi-110058',
    'phone_number': 'Tel. : 011-45656183, 011-45037193',
    'name': 'John Doe',
    'father_name': 'John Doe Sr.',
    'dob': '01-01-2000',
    'cet_rank': '1234',
    'phone': '1234567890',
    'course': 'Computer Science',
    'batch': '2023',
    'photo': 'photo.jpg',
    'signature': 'signature.jpg'
}



template = Template(template_html)
output_html = template.render(data)

with open('id_card.html', 'w') as f:
    f.write(output_html)
