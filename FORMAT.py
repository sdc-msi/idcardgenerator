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
                <div class="college-name">Maharaja Surajmal Institute</div>
                <div class="about">(Affiliated to GGSIP University, Dwarka, Delhi)</div>
                <div class="college-address">C-4, Janakpuri, New Delhi-110058</div>
                <div class="college-phone-number">Tel. : 011-45656183, 011-45037193</div>
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