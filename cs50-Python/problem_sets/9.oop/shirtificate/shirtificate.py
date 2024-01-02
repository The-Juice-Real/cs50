from fpdf import FPDF

name = input("What's your name? ").strip()

pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(0)
pdf.set_font("helvetica", "B", 50)
pdf.cell(h = 70, txt = "CS50 Shirtificate", align = "C", center = True)
pdf.image("shirtificate.png", x = "C", w = 160, y = 80)
pdf.set_font("helvetica", "B", 30)
pdf.set_text_color(255, 255, 255)
pdf.cell(h = 240, txt = f"{name}", align = "C", center = True)
pdf.set_font("helvetica", "B", 30)
pdf.cell(h = 270, txt = "took CS50", align = "C", center = True)
pdf.output("shirtificate.pdf")