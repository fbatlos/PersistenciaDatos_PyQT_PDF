from fpdf import FPDF
import os

path = os.path.dirname(__file__)
path_pdfs = "/PDFs/"

class ManagerPDF:
    def __init__(self):
        if self.comprobar_ruta():
            self.crear_carpeta_pdf()

    def comprobar_ruta(self):
        return os.path.exists(path)
    
    def crear_carpeta_pdf(self):
        try:
            os.mkdir(path_pdfs)
        except:
            pass


class PDF1(FPDF):
    def header(self):
        
        # Logo
        logo = "../recursos/iconos/logo.png"
        path_logo = os.path.join(os.path.dirname(__file__), logo)
        print(path_logo)
        self.image(path_logo, 10, 8, 33)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10, 'Ejemplo de Informe', 'C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        logo_alber = "../recursos/iconos/logo_alberti.png"
        path_logo_alber = path + logo_alber
        
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        self.image(path_logo_alber, None, None, 30, 15)
        # Arial italic 8
        self.set_font('Arial', 'I', 10)
        self.set_y(-25)

        # Page number
        self.cell(0, 10, 'Página ' + str(self.page_no()), 0, 0, 'R')


class PDF2(FPDF):
    def header(self):
        # Logo
        logo = "logo.png"
        path_logo = path + logo
        self.image(path_logo, 10, 8, 33)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10, 'Title', 1, 0, 'C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')
        

class PDF3(FPDF):
    
    def header(self):
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Calcular ancho del texto (title) y establecer posición
        w = self.get_string_width(title) + 6
        self.set_x((210 - w) / 2)
        # Colores del marco, fondo y texto
        self.set_draw_color(0, 80, 180)
        self.set_fill_color(230, 230, 0)
        self.set_text_color(220, 50, 50)
        # Grosor del marco (1 mm)
        self.set_line_width(1)
        # Titulo
        self.cell(w, 9, title, 1, 1, 'C', 1)
        # Salto de línea
        self.ln(10)

    def footer(self):
        # Posición a 1.5 cm desde abajo
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Color de texto en gris
        self.set_text_color(128)
        # Numero de pagina
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def chapter_title(self, num, label):
        # Arial 12
        self.set_font('Arial', '', 12)
        # Color de fondo
        self.set_fill_color(200, 220, 255)
        # Titulo
        self.cell(0, 6, 'Chapter %d : %s' % (num, label), 0, 1, 'L', 1)
        # Salto de línea
        self.ln(4)

    def chapter_body(self, name):
        # Leer archivo de texto
        with open(name, 'rb') as fh:
            txt = fh.read().decode('latin-1')
        # Times 12
        self.set_font('Times', '', 12)
        # Emitir texto justificado
        self.multi_cell(0, 5, txt)
        # Salto de línea
        self.ln()
        # Mención en italic -cursiva-
        self.set_font('', 'I')
        self.cell(0, 5, '(end of excerpt)')

    def print_chapter(self, num, title, name):
        self.add_page()
        self.chapter_title(num, title)
        self.chapter_body(name)


class PDF4(FPDF):
    def header(self):
        # Logo
        logo = "logo.png"
        path_logo = path + logo
        self.image(path_logo, 10, 8, 33)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10, 'Title', 1, 0, 'C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')


class PDF5(FPDF):
    def header(self):
        # Logo
        logo = "logo.png"
        path_logo = path + logo
        self.image(path_logo, 10, 8, 33)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10, 'Title', 1, 0, 'C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')