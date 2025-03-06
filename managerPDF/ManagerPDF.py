from fpdf import FPDF
import os

path = os.path.dirname(__file__)
path_pdfs = "PDFs/"

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

    def generar_fecha_actual(self):
        from datetime import datetime
        now = datetime.now()
        return now.strftime("%d-%m-%Y-%H-%M-%S")

class PDF1(FPDF):
    def header(self):
        # Logo
        logo = "\logo.png"
        path_logo = path + logo
        print(path_logo)
        self.image(path_logo, 10, 8, 20)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        #self.cell(80)
        # Title
        self.cell(0,10,'Billete', align='C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        logo_alber = "\logo_alberti.png"
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
        logo = "\logo.png"
        path_logo = path + logo
        print(path_logo)
        self.image(path_logo, 10, 8, 20)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Title
        self.cell(0, 10, 'Mis Viajes', align='C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        logo_alber = "\logo_alberti.png"
        path_logo_alber = path + logo_alber
        
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        self.image(path_logo_alber, None, None, 30, 15)
        # Arial italic 8
        self.set_font('Arial', 'I', 10)
        self.set_y(-25)

        # Page number
        self.cell(0, 10, 'Página ' + str(self.page_no()), 0, 0, 'R')
        

class PDF3(FPDF):
    
    def header(self):
        # Logo
        logo = "\logo.png"
        path_logo = path + logo
        print(path_logo)
        self.image(path_logo, 10, 8, 20)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        #self.cell(80)
        # Title
        self.cell(0,10,'Vuelos', align='C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        logo_alber = "\logo_alberti.png"
        path_logo_alber = path + logo_alber
        
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        self.image(path_logo_alber, None, None, 30, 15)
        # Arial italic 8
        self.set_font('Arial', 'I', 10)
        self.set_y(-25)

        # Page number
        self.cell(0, 10, 'Página ' + str(self.page_no()), 0, 0, 'R')

class PDF4(FPDF):
    def header(self):
        # Logo
        logo = "logo.png"
        path_logo = path + logo
        self.image(path_logo, 10, 8, 20)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Title
        self.cell(0, 10, 'Información Usuario', align='C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        logo_alber = "\logo_alberti.png"
        path_logo_alber = path + logo_alber
        
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        self.image(path_logo_alber, None, None, 30, 15)
        # Arial italic 8
        self.set_font('Arial', 'I', 10)
        self.set_y(-25)


class PDF5(FPDF):
    def header(self):
        # Logo
        logo = "logo.png"
        path_logo = path + logo
        self.image(path_logo, 10, 8, 20)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Title
        self.cell(0, 10, 'Destinos', align='C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        logo_alber = "\logo_alberti.png"
        path_logo_alber = path + logo_alber
        
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        self.image(path_logo_alber, None, None, 30, 15)
        # Arial italic 8
        self.set_font('Arial', 'I', 10)
        self.set_y(-25)