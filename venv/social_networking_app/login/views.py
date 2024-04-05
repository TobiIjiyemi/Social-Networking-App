from django.shortcuts import render
from django.http import HttpResponse
from django_nextjs.render import render_nextjs_page
# Create your views here.

def index(request):
    return HttpResponse("Hello, world.. Login index!")

# async def jobs(request):
#     return await render_nextjs_page