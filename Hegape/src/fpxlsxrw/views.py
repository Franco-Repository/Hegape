# Create your views here.
from django.shortcuts import render
import pandas as pd
from django.http import HttpResponse



def bienvenido(request):
    return render(request, 'base.html')


def print_lawea(request):
    message = "Lawea WEEEENA"
    return HttpResponse(message)

def read_excel(request):
    # Load the Excel file into a Pandas DataFrame
    df = pd.read_excel('./files/Decathlon.xlsx')

    # Convert the DataFrame to an HTML table
    html = df.to_html()

    # Create an HTTP response with the HTML content
    response = HttpResponse()
    response.write(html)

    return response