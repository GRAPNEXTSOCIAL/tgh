from datetime import date, datetime
from distutils.command import upload
from itertools import product
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime, date

# Create your models here.

MANAGER='MANAGER'
CASHIER='CASHIER'
ACCOUNTANT = 'ACCOUNTANT'

STATE_CHOICES = ( 
    ('Andhra Pradesh', 'Andhra Pradesh'), 
    ('Arunachal Pradesh', 'Arunachal Pradesh'), 
    ('Bihar', 'Bihar'), 
    ('Chhattisgarh', 'Chhattisgarh'), 
    ('Goa', 'Goa'), 
    ('Gujurat', 'Gujurat'), 
    ('Haryana', 'Haryana'), 
    ('Himachal Pradesh', 'Himachal Pradesh'), 
    ('Jharkhand', 'Jharkhand'), 
    ('Karnataka', 'Karnataka'), 
    ('Kerala', 'Kerala'), 
    ('Assam', 'Assam'), 
    ('Madhya Pradesh', 'Madhya Pradesh'), 
    ('Maharashtra', 'Maharashtra'), 
    ('Manipur', 'Manipur'), 
    ('Meghalaya', 'Meghalaya'), 
    ('Mizoram', 'Mizoram'), 
    ('Nagaland', 'Nagaland'), 
    ('Odisha', 'Odisha'), 
    ('Punjab', 'Punjab'), 
    ('Rajasthan', 'Rajasthan'), 
    ('Sikkim', 'Sikkim'), 
    ('Tamil Nadu', 'Tamil Nadu'), 
    ('Telangana', 'Telangana'), 
    ('Tripura', 'Tripura'), 
    ('Uttarakhand', 'Uttarakhand'), 
    ('Uttar Pradesh', 'Uttar Pradesh'), 
    ('West Bengal', 'West Benga'), 
)

STAFF_CATEGORY_CHOICES = (
    (MANAGER, 'Manager'),
    (CASHIER, 'Cashier'), 
    (ACCOUNTANT, 'Accountant')
)

STATUS_CHOICES = (
    ('Accepted', 'Accepted'), 
    ('Packed', 'Packed'), 
    ('On The Way', 'On The Way'), 
    ('Delivered', 'Delivered'), 
    ('Cancel', 'Cancel')
)

class Color(models.Model):
    color_code = models.CharField(max_length=5)
    item_color = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.item_color

class Size(models.Model):
    size_code = models.CharField(max_length=5)
    item_size = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.item_size

# class Prodgroup(models.Model):
#     p_group_code = models.IntegerField()
#     p_group_name = models.CharField(max_length=70)
#     p_group_description = models.CharField(max_length=200)

class Supplier(models.Model):
    supplier_code = models.CharField(max_length=50)
    supplier = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    contact_no = models.CharField(max_length=50)
    supplier_email = models.EmailField(null=True)
    gstin_no = models.CharField(max_length=50)
    state = models.CharField(choices=STATE_CHOICES, max_length=50, null=True)
    pin = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.supplier

class User(AbstractUser):
    staff_category = models.CharField(choices=STAFF_CATEGORY_CHOICES, max_length=100)

class Customer(models.Model):
    mobile_no = models.CharField(max_length=15)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    locality = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=50, null=True)
    zipcode = models.CharField(max_length=10, null=True)
    state = models.CharField(choices=STATE_CHOICES, max_length=50, null=True)

    def __str__(self):
        return str(self.id)

class Itemgroup(models.Model):
    item_group_code = models.IntegerField()
    item_group_name = models.CharField(max_length=50)
    item_group_description = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.item_group_name

class Category(models.Model):
    item_group_name = models.ForeignKey(Itemgroup, on_delete=models.CASCADE, null=True)
    category_code = models.IntegerField()
    category_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.category_name

class Product(models.Model):
    group = models.ForeignKey(Itemgroup, on_delete=models.CASCADE, null=True)
    item_type = models.TextField()
    manufacturer = models.TextField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    barcode = models.CharField(max_length=100)    
    item_size = models.ForeignKey(Size, on_delete=models.CASCADE, null=True)
    item_color = models.ForeignKey(Color, on_delete=models.CASCADE, null=True)    
    actual_mrp = models.FloatField()
    purchase_price = models.FloatField()
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    purchase_tax_type = models.CharField(max_length=30)
    purchase_tax = models.FloatField()
    selling_tax = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    product_purchase_date = models.DateField(auto_now_add=False, auto_now=False, null=True)
    manufacture_date = models.DateField(auto_now_add=False, auto_now=False, null=True)
    expiry_date = models.DateField(auto_now_add=False, auto_now=False, null=True)
    alertment_date = models.DateField(auto_now_add=False, auto_now=False, null=True)
    product_image = models.ImageField(upload_to='productimg')



class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # title = models.ForeignKey(Product, on_delete=models.CASCADE)
    pimage = models.ImageField(upload_to='productimage')

    def __str__(self):
        return str(self.id)

class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True)
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    active = models.BooleanField()

    def __str__(self):
        return self.code

class Cart(models.Model):
    cart_id = models.CharField(max_length=100, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    offer_applied = models.ForeignKey(Coupon, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateField(auto_now_add=False)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

class Tax(models.Model):
    tax_type = models.CharField(max_length=10, unique=True)
    value = models.FloatField()

class Purchase(models.Model):
    trans_date = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    pur_bill_no = models.CharField(max_length=50)
    supplier_name = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)
    total_qty = models.IntegerField()
    gross_amt = models.FloatField()
    disc_amt = models.FloatField()
    gst_amt = models.FloatField()
    tcs = models.FloatField()
    o_charge = models.FloatField()
    o_disc = models.FloatField()
    grand_total = models.FloatField()