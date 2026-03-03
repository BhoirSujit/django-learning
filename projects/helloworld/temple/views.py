from django.shortcuts import render

# Create your views here.
def home(req):
    data = {'name' : 'sujit', 'age' : 21, 'skills' : ['java' , 'python', 'rest', 'django', 'react', 'nodejs']}
    return render(req, 'home.html', data)
  