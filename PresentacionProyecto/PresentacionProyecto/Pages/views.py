from django.http import HttpResponse

def homePageView(request):
    
    html = """
    <html>
    <head>
    <title>Mi primera pagina web </title>
    </head>
    <body>
    <h1 align="center" >Mi Primera pagina web </h1>
    </body>
    </html>
    """
    
return HttpResponse(html) 
