from django.shortcuts import render

# Create your views here.
def example_view(request):
    # my_app/template/my_app/example.html
    return render(request,'my_app/example.html')

def variable_view(request):
    my_var = {'first_name': 'First','last_name': 'Last',
        'list': [1,2,3,4],'some_dict':{1:2,3:4},'user_logged_in' : True }
    return render(request,'my_app/variable.html',context=my_var)