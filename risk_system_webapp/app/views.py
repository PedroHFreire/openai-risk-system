from django.shortcuts import render

# Create your views here.

# Login View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import LoginForm, DataInputForm
from .models import StockData

def login_view(request):
    if request.method == 'POST':
        # User has submitted the login form
        form = LoginForm(request.POST)
        if form.is_valid():
            # Form data is valid
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # User is a valid Django user
                login(request, user)
                # Redirect to a success page
                return redirect('data_input')
            else:
                # User is not a valid Django user
                form.add_error(None, "Invalid username or password")
    else:
        # User has not submitted the login form
        form = LoginForm()
    # Render the login page
    return render(request, 'login.html', {'form': form})


## Data input view
def data_input_view(request):
    if request.method == 'POST':
        # User has submitted the data input form
        form = DataInputForm(request.POST)
        if form.is_valid():
            # Form data is valid
            ticker = form.cleaned_data['ticker']
            shares = form.cleaned_data['shares']
            purchase_price = form.cleaned_data['purchase_price']
            purchase_date = form.cleaned_data['purchase_date']
            # Save the data to the database
            data = StockData(ticker=ticker, shares=shares, purchase_price=purchase_price, purchase_date=purchase_date)
            data.save()
        else:
            # Form is not valid - render the data input page with the form and stock data
            stock_data = StockData.objects.all()
            return render(request, 'data_input.html', {'form': form, 'stock_data': stock_data})
    else:
        # User has not submitted the data input form
        form = DataInputForm()

    # Get all the data from the database
    stock_data = StockData.objects.all()

    # Render the data input page
    return render(request, 'data_input.html', {'form': form, 'stock_data': stock_data})

# Edit data View
def edit_data_view(request, id):
    data = get_object_or_404(StockData, id=id)
    if request.method == 'POST':
        # User has submitted the data input form
        form = DataInputForm(request.POST, instance=data)
        if form.is_valid():
            # Form data is valid
            form.save()
            # Redirect to the data input page
            return redirect('data_input')
    else:
        # User has not submitted the data input form
        form = DataInputForm(instance=data)
    # Render the edit data page
    return render(request, 'edit_data.html', {'form': form, 'data': data})

def delete_data_view(request, id): 
    data = get_object_or_404(StockData, id=id)
    data.delete() 
    # Redirect to the data input page
    return redirect('data_input')