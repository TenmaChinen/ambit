from app.settings import MEDIA_ROOT, BASE_DIR
from reportlab.pdfgen.canvas import Canvas
from cats.models import Cat
from pathlib import Path
from io import BytesIO
from PIL import Image

DIR_ICONS = BASE_DIR / 'staticfiles' / 'icons'

def create_census_pdf(colony_id):

    queryset = Cat.objects.filter(colony=colony_id)
    queryset = queryset.order_by('-sterilized')
    values_queryset = queryset.values_list('name','thumbnail','sterilized','gender')
    
    buffer = BytesIO()
    # buffer.seek(0)
    canvas = Canvas(buffer)
    canvas.setFont(psfontname='Helvetica', size=14)

    W_PAGE, H_PAGE = canvas._pagesize
    ROWS, COLS = 6, 4
    X_MARGIN = W_PAGE * 0.1
    Y_MARGIN = X_MARGIN
    H_LABEL = 24

    S_IMG = (H_PAGE - (2*Y_MARGIN)) / ROWS - H_LABEL
    X_SEP = (W_PAGE - (2*X_MARGIN) - S_IMG * COLS) / (COLS-1)
    
    H_CARD = S_IMG + H_LABEL
    Y_TOP = H_PAGE - S_IMG - Y_MARGIN

    S_ICON = S_IMG * 0.1
    row, col = 0, 0

    for name, thumbnail, sterilized, gender in values_queryset:
        
        x_pos = X_MARGIN + (col * (S_IMG + X_SEP))
        y_pos = Y_TOP - (row * H_CARD)
        
        file_path = MEDIA_ROOT / thumbnail
        canvas.drawImage(image=file_path, x=x_pos, y=y_pos, width=S_IMG, height=S_IMG)

        y_text = y_pos - 13
        canvas.setFillColorRGB(0.4,0.4,0.4)
        canvas.drawString(x=x_pos, y=y_text, text=name)
        
        param_1 = 'female' if gender else 'male'
        param_2 = '-neutered' if sterilized else ''
        file_path = DIR_ICONS / f'ic-{param_1}{param_2}.png'

        x_icon = x_pos + S_IMG - S_ICON - 2
        y_icon = y_pos - S_ICON - 3
        
        canvas.drawImage(image=file_path, x=x_icon, y=y_icon, width=S_ICON, height=S_ICON)

        col = (col + 1) % COLS
        if col == 0:
            row = (row+1) % ROWS

            if row == 0:
                canvas.showPage()
                col = 0

    canvas.save()
    buffer.seek(0)
    return buffer