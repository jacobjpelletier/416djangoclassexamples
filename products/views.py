from django.shortcuts import render, redirect
# import product form so we can use product form in views
from .forms import ProductForm
from .models import Product


# CRUD Operations: Create, Retrieve, Update, Delete

# READ operation of CRUD
def view_products(request):
    # Retrieve all the products and render products.html with the data
    products = Product.objects.all()
    context = {'products': products}
    # now you can access all products from products.html because context=products
    return render(request, 'products/products.html', context)


# CREATE operation of CRUD
def create_product(request):
    # Create a form instance and populate it with data from the request
    # we can pass this form variable as context, and it is capable of creating html
    '''
        code that is different from the class repo that we did in class:
          - not use crispy

        form = ProductForm() # in case it is none, it will be an empty instance

        # !!! form object contains errors which can also be passed onto context,
        # so the user will see the same form with any error messages along with an empty form view

        if request.method == 'POST':

            form = ProductForm(request.POST) # at this point the form is rendered but nothing is updated

            # in case form is not NONE, (i.e. request.POST), then continue with validation

            if form.is_valid():

                # if form is valid, then save information into DB

                form.save()

                # now redirect (need to import), use name defined in view

                return redirect('view_products') # this was called 'view' in class

    '''
    form = ProductForm(request.POST or None)
    # check whether it's valid:
    if form.is_valid():
        # save the record into the db
        form.save()
        # after saving redirect to view_product page
        return redirect('view_products')

    # if the request does not have post data, a blank form will be rendered
    return render(request, 'products/product-form.html', {'form': form})


# need to add id parameter where product id will be argument
def update_product(request, id):
    # Get the product based on its id
    product = Product.objects.get(id=id)
    # populate a form instance with data from the data on the database
    # instance=product allows to update the record rather than creating a new record when save method is called
    form = ProductForm(request.POST or None, instance=product)

    '''
    # class code
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('view')
    '''

    # check whether it's valid:
    if form.is_valid():
        # update the record in the db
        form.save()
        # after updating redirect to view_product page
        return redirect('view_products')

    # if the request does not have post data, render the page with the form containing the product's info
    return render(request, 'products/product-form.html', {'form': form})


def delete_product(request, id):
    # we will need id because we need to know which particular row of Products table we are deleting
    # Get the product based on its id
    product = Product.objects.get(id=id)

    # if this is a POST request, we need to delete the form data
    if request.method == 'POST':
        product.delete()
        # after deleting redirect to view_product page
        return redirect('view_products')

    # if the request is not post, render the page with the product's info
    return render(request, 'products/delete-confirm.html', {'product': product})
