import os
import json
from fpdf import FPDF
from parsers import (
    parse_electrek
)
from weather import (
    today,
    get_sunrise_sunset
)

# --- load config object ---
config = json.load(open('config.json'))

# --- Initialize PDF ---
# initialize
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=15)

# --- Title ---
pdf.cell(
    200, 10,
    txt="Duckpaper",
    ln=1, align='C')

# --- Date ---
pdf.cell(
    200, 10,
    txt=today,
    ln=2, align='C'
)

# --- Sunrise / Sunset ---
pdf.cell(
    200, 10,
    txt=str(get_sunrise_sunset()),
    ln=3, align='C'
)

# --- Weather ---
pdf.cell(
    200, 10,
    txt='test',
    ln=3, align='C'
)

# save the pdf with name .pdf
pdf.output("duckpaper.pdf")