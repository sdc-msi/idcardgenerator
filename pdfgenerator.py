from fpdf import FPDF
import glob


folder_path = 'GENERATED IDs/'

id_card_files = glob.glob(f"{folder_path}/*.jpg")

ids_per_page = 4

num_ids = len(id_card_files)
num_pages = (num_ids + ids_per_page - 1) // ids_per_page

pdf = FPDF(orientation='L', unit='mm', format='A4')

page_width = pdf.w - 2 * pdf.l_margin
page_height = pdf.h - 2 * pdf.t_margin

id_card_width = page_width / 2
id_card_height = page_height / 2

for i, id_card_file in enumerate(id_card_files):
    page = i // ids_per_page
    position = i % ids_per_page

    if position == 0:
        pdf.add_page()

    x = pdf.l_margin + (position % 2) * id_card_width
    y = pdf.t_margin + (position // 2) * id_card_height

    pdf.image(id_card_file, x, y, id_card_width, id_card_height)

pdf.output('compiled_ids.pdf')
