from django.shortcuts import render
from django.http import HttpResponse
from django_nextjs.render import render_nextjs_page_sync
# Create your views here.

def index(request):
    return render_nextjs_page_sync(request)

def login(request):
    return HttpResponse("Hello theree??")
# async def jobs(request):
#     return await render_nextjs_page