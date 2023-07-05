# College Student ID Card Generation

This repository contains a project related to the generation of ID cards for
college students. The purpose of this project is to provide a convenient and
efficient solution for creating ID cards within a college or educational
institution.

## Installation and Setup

To use this project proceed with the following steps:

1. clone this repo `git clone https://github.com/sdc-msi/idcardgenerator`

2. Download the Response sheet from excel as .xlsx file

3. Download the photos as a zip from google drive. Dont download them
   separately.

4. Install requirements `pip3 install pandas openpyxl html2image jinja2 python-barcode`

5. Run `python id_generator.py photos.zip signature.zip excel.xlsx` name both the file
   accordingly to your need.

__NOTE:__ Google Chrome (Windows) / Chromium (Linux) is required for this project.

## Google forms required fields and naming schema

TODO

## Release Info

Currently, Standalone executable are available for windows and linux. Just pass
the args into the commandline using terminal. Tested to work on Windows 10 and
arch linux.

