from datetime import datetime

def bienvenido_context(request):
    if request.user.is_authenticated:
        mensaje = (f"Bienvenido {request.user.username}")
    else:
        mensaje = ("Bienvenido a Entrecopas")
    return {"mensaje_bienvenida":mensaje}

def year_context(request):
    year = datetime.now().year
    return {"year":year}