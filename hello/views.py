from django.shortcuts import render, HttpResponse
import datetime

from hello.utils import Cow

# Create your views here.
def hello_view(request):
    return HttpResponse("Witaj świecie!")

def hi_view(request):
    return HttpResponse(
        """
        <!DOCTYPE html>
        <html>
            <head>
            </head>
            <body>
                <h2>Hello, Wolrd!</h2>
            </body>
        </html>
        """)

# szablon
def hi2_view(request):
    return render(request, 'hello.html')

def byk_view(request):
    return HttpResponse("Elo byku malinowy!")

# Podatność XSS - przykład
def name_view(request,name ):
    #importy powinny być zawsze na samej górze
    from django.utils.html import escape


    # always remember to escape your output
    print(name)
    escaped_name = escape(name)
    return HttpResponse(f"Witaj, {escaped_name}!")

# kontekst szablonu
def name_view2(request, name):
    return render(
        request,
        'hello2.html',
        {"x": name}
    )

def is_it_new_year(request):
    today = datetime.date.today()

    is_new_year = False
    if today.month == 1 and today.day == 1:
        is_new_year = True
    #
    # if today.month == 1 and today.day == 1:
    #     msg = "Tak"
    #     color = "green"
    # else:
    #     msg = "Nie"
    #     color = "red"

    return render(
        request,
        'isitnewyear.html',
        {'is_new_year': is_new_year}
    )

def collection_view(request):

    fruits = [
        'jabłko',
        'banan',
        'winogrona',
        'mandarynki'
    ]

    person = {
        "name": "Jan",
        "surname": "Kowalski",
        "age": 25
    }


    cow = Cow("Mućka", 3)

    return render(
        request,
        'collection.html',
        {'fruits': fruits,
         'person': person,
         'cow': cow
         }


    )