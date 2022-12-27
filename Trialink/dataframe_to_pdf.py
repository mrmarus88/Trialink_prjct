from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus.tables import Table,TableStyle,colors

def export():
    vers = SimpleDocTemplate('D:\python\Trialink\Trialink_prjct\Trialink\media\export.pdf',pagesize=letter)

    c_width=[1*inch] # width of the columns 
    t=Table(vers,colWidths=c_width,repeatRows=1)
    t.setStyle(TableStyle([('FONTSIZE',(0,0),(-1,-1),12),
                           ('BACKGROUND',(0,0),(-1,0),colors.lightgreen),('VALIGN',(0,0),(-1,0),'TOP')]))
    elements=[]
    elements.append(t)
    vers.build(elements)
    print(vers)