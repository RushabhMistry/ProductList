from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm

# Create your views here.

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})

def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_form.html', {'form': form})

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        return redirect('product_list')
    return render(request, 'product_confirm_delete.html', {'product': product})


# ______________________________________"SQL"______________________________________________________


# from django.shortcuts import render, redirect
# from django.db import connection
# from .forms import ProductForm

# def execute_sql(query, params=None, fetch_one=False, fetch_all=False):
#     with connection.cursor() as cursor:
#         cursor.execute(query, params or [])
#         if fetch_one:
#             return cursor.fetchone()
#         if fetch_all:
#             return cursor.fetchall()
#         connection.commit()
#     return None

# def product_list(request):
#     query = "SELECT id, name, description, quantity, price FROM inventory_product"
#     products = execute_sql(query, fetch_all=True)
#     return render(request, 'product_list.html', {'products': products})

# def add_product(request):
#     if request.method == "POST":
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             query = """
#             INSERT INTO inventory_product (name, description, quantity, price)
#             VALUES (%s, %s, %s, %s)
#             """
#             execute_sql(query, [data['name'], data['description'], data['quantity'], data['price']])
#             return redirect('product_list')
#     else:
#         form = ProductForm()
#     return render(request, 'product_form.html', {'form': form})

# def edit_product(request, pk):
#     if request.method == "POST":
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             query = """
#             UPDATE inventory_product
#             SET name = %s, description = %s, quantity = %s, price = %s
#             WHERE id = %s
#             """
#             execute_sql(query, [data['name'], data['description'], data['quantity'], data['price'], pk])
#             return redirect('product_list')
#     else:
#         query = "SELECT id, name, description, quantity, price FROM inventory_product WHERE id = %s"
#         product = execute_sql(query, [pk], fetch_one=True)
#         if not product:
#             return redirect('product_list')
#         form = ProductForm(initial={
#             'name': product[1],
#             'description': product[2],
#             'quantity': product[3],
#             'price': product[4]
#         })
#     return render(request, 'product_form.html', {'form': form})

# def delete_product(request, pk):
#     query = "SELECT id, name FROM inventory_product WHERE id = %s"
#     product = execute_sql(query, [pk], fetch_one=True)
#     if not product:
#         return redirect('product_list')
#     if request.method == "POST":
#         query = "DELETE FROM inventory_product WHERE id = %s"
#         execute_sql(query, [pk])
#         return redirect('product_list')
#     return render(request, 'product_confirm_delete.html', {'product': product})
