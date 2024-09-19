from django.shortcuts import render, redirect

#Django authentication libraries
from django.contrib.auth import authenticate, login, logout
#Django authentication form
from django.contrib.auth.forms import AuthenticationForm

#function to call login_view that takes request from user
def login_view(request):
    #initialize:
    #error_message to none
    error_message = None
    #form object with usernmae and password fields
    form = AuthenticationForm()

#When user hit login button post request is generated
    if request.method == 'POST':
        #reads data sent by form via post request
        form =AuthenticationForm(data=request.POST)

        #check if form is valid
        if form.is_valid():
            #read username
            username=form.cleaned_data.get('username')
            #read password
            password=form.cleaned_data.get('password')
            
            #Use DJango authenticate function to validate the user
            user=authenticate(username=username, password=password)
            if user is not None:
                #If user is authenticated, then use predefined function to login
                login(request,user)
                return redirect('recipes:recipes_list') #send user to desired page
            else:
                #In case of error, print error message
                error_message = 'oops... something went wrong'
    #Prepare data to send from view to template
    context ={
        'form': form, #End the form data
        'error_message': error_message #End error_message
    }
    #Load login page using context information
    return render(request, 'auth/login.html', context)

def logout_view(request):
    logout(request)
    return redirect(request, 'auth/successhtml')

def logout_success(request):
    return render(reques, 'success.html')