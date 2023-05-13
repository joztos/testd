# example/views.py
from datetime import datetime
from django.http import HttpResponse

def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <style>
            body {{
                background-image: url('https://i.im.ge/2023/05/13/UbjYym.como-disfrutar-del-sexo-con-condon-1550x.webp');
                background-repeat: no-repeat;
                background-size: cover;
            }}
        </style>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is { now }.</p>
            <iframe width="560" height="315" src="https://www.youtube.com/embed/videoseries?list=RDQMgEzdN5RuCXE" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
        </body>
    </html>
    '''
    return HttpResponse(html)
