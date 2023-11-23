from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def home(request):
    peoples = [
        {'name': 'John', 'age':23},
        {'name': 'kisor', 'age':17}

    ]
    # return HttpResponse(peoples);
    text = """ 
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Eaque reiciendis repellendus provident ratione accusamus dolores earum iste iure aperiam doloremque nam tempore, aliquam dolore temporibus quis suscipit rerum nemo quos.
    """
    vegetables = ['potato', 'pumpkin']
    return render(request, 'index.html', context={'peoples': peoples, 'text': text, "vegetables": vegetables})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')