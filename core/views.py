from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import date
import calendar


#MACROS
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

#Views
def displayMainpage(request):
    today = date.today()
    month = MONTHS[today.month - 1]
    year = year = str(today.year)
    return render(request, 'index.html', {'mm_yy':month+" "+year})