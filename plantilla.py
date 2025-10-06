from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Medidas
page_width, page_height = letter
card_width = 2.5 * 28.35  # cm to points (1 cm = 28.35 points)
card_height = 1.5 * 28.35
margin = 36  # 0.5 inch margin

# Crear PDF
pdf_path = "/mnt/data/plantilla_aretes_oro10k_separados.pdf"
c = canvas.Canvas(pdf_path, pagesize=letter)
c.setFont("Helvetica", 6)

# Calcular cuántas tarjetas caben
cols = int((page_width - 2 * margin) / card_width)
rows = int((page_height - 2 * margin) / card_height)

# Centrar la cuadrícula
start_x = (page_width - cols * card_width) / 2
start_y = (page_height - rows * card_height) / 2

for row in range(rows):
    for col in range(cols):
        x = start_x + col * card_width
        y = start_y + row * card_height
        
        # Dibujar borde de guía
        c.setStrokeColorRGB(0, 0, 0)
        c.rect(x, y, card_width, card_height)
        
        # Texto "Oro 10K"
        c.setFont("Helvetica-Bold", 7)
        c.drawCentredString(x + card_width / 2, y + card_height - 10, "Oro 10K")
        
        # Marcas para orificios (centradas horizontalmente, más separadas)
        center_x = x + card_width / 2
        center_y = y + card_height / 2
        spacing = 18  # separación entre los agujeros en puntos (~6.3 mm)
        c.circle(center_x - spacing / 2, center_y, 0.7, stroke=1, fill=0)
        c.circle(center_x + spacing / 2, center_y, 0.7, stroke=1, fill=0)
        
        # Espacio inferior (dejar en blanco)

c.showPage()
c.save()

pdf_path
