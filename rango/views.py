from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category
from rango.models import Page
from rango.forms import CategoryForm
print(Category.objects.all())

def index(request):   
   context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
   category_list=Category.objects.order_by('-likes')[:5]
   context_dict={'categories':category_list}
   page_list = Page.objects.order_by('-views')[:5]
   context_dict['pages'] = page_list
   
  
   return render(request, 'rango/index.html', context = context_dict)
   
def about(request):
    context_dict= {'name': 'Denitsa Velichkova'}
    
    return render(request,'rango/about.html', context = context_dict)
def add_category(request):
    form = CategoryForm()
    if request.method == 'POST' :
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request) 
        else:
            print(form.errors)
    return render(request,'rango/add/category.html', {'form' :form})     

def show_category(request, category_name_slug):
    context_dict={}
    try:
        category=Category.objects.get(slug=category_name_slug)
        pages=Page.objects.filter(category=category)
   
        context_dict['pages']=pages    
        context_dict['category']=category
    
    except Category.DoesNotExist:
        context_dict['category']=None
        contect_dict['pages']=None
    
    return render(request,'rango/category.html',context_dict)
        