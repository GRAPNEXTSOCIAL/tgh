from dataclasses import field, fields
from pyexpat import model
# from tkinter import Widget
# from tkinter.tix import Select
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation
from django.forms import ModelForm, TextInput

from .models import Customer, Tax, User, Product, Image, Cart, OrderPlaced, Coupon, Color, Size, Supplier, Itemgroup, Category, Purchase


class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Pleade Enter the Username'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Password'}))
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Password Again'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Email'}))
    class Meta:
        model = User
        fields = ['username', 
        'email', 
        'password1', 
        'password2'
        ]
        labels = {'email':'Email'}
        Widgets = {'username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Username'})}

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control', 'placeholder':'Please Enter the Username'}))
    password = forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs=
    {"autocomplete": "current-password", 'class':'form-control', 'placeholder':'Please Enter the Password'}))

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old Password"), 
    strip=False, widget=forms.PasswordInput(attrs=
    {'autocomplete': 'current-password', 'autofocus':True,  
    'class':'form-control', 'placeholder':'Please Enter the Old Password'}))
    new_password1 = forms.CharField(label=_("New Password"), 
    strip=False, widget=forms.PasswordInput(attrs=
    {'autocomplete': 'new-password', 'class':'form-control', 'placeholder':'Please Enter the New Password'}),
    help_text=password_validation.
    password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"), 
    strip=False, widget=forms.PasswordInput(attrs=
    {'autocomplete': 'new-password', 'class':'form-control', 'placeholder':'Please Enter the New Password Again'}))

class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length=254, widget=forms.EmailInput(attrs=
    {'autocomplete': 'email', 'class':'form-control', 'placeholder':'Please Enter the Email'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New Password"), 
    strip=False, widget=forms.PasswordInput(attrs=
    {'autocomplete': 'new-password', 'class':'form-control', 'placeholder':'Please Enter the New Password'}),
    help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"), 
    strip=False, widget=forms.PasswordInput(attrs=
    {'autocomplete': 'new-password', 'class':'form-control', 'placeholder':'Please Enter the New Password Again'}))

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 
        'locality', 
        'city', 
        'zipcode', 
        'state'
        ]
        widgets = {'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Name'}), 
                   'locality':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Locality'}), 
                   'city':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the City'}), 
                   'zipcode':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Zipcode'}),
                   'state':forms.Select(attrs={'class':'form-control', 'placeholder':'Please Enter the State'})
                }

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['group', 
        'item_type', 
        'manufacturer', 
        'supplier', 
        'title', 
        'barcode', 
        'item_size', 
        'item_color', 
        'actual_mrp', 
        'purchase_price', 
        'selling_price', 
        'discounted_price',
        'purchase_tax_type',  
        'purchase_tax', 
        'selling_tax', 
        'description', 
        'brand', 
        'category', 
        'product_purchase_date',
        'manufacture_date',  
        'expiry_date', 
        'alertment_date', 
        'product_image'
        ]
        widgets = {
            'group' :forms.Select(attrs={'class':'form-control', 'placeholder':'Select'}),
            'item_type' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Item Type'}), 
            'manufacturer' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Manufacturer'}), 
            'supplier' :forms.Select(attrs={'class':'form-control', 'placeholder':'Select'}), 
            'title' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Product Name'}), 
            'barcode' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Barcode'}), 
            'item_size' :forms.Select(attrs={'class':'form-control', 'placeholder':'Select'}), 
            'item_color' :forms.Select(attrs={'class':'form-control', 'placeholder':'Select'}), 
            'purchase_price' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Purchase Price'}), 
            'actual_mrp' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Actual Mrp Rs.'}), 
            'selling_price' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Selling Price'}),
            'discounted_price' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Discounted Price'}),  
            'purchase_tax_type' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Purchase Tax Type'}), 
            'purchase_tax' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Purchase Tax'}), 
            'selling_tax' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Selling Tax'}), 
            'description' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Description'}), 
            'brand' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the Brand Name'}), 
            'category' :forms.Select(attrs={'class':'form-control', 'placeholder':'Select'}), 
            'product_purchase_date' :forms.DateInput(attrs={'class':'form-control', 'placeholder':'YYYY-MM-DD'}), 
            'manufacture_date' :forms.DateInput(attrs={'class':'form-control', 'placeholder':'YYYY-MM-DD'}), 
            'expiry_date' :forms.DateInput(attrs={'class':'form-control', 'placeholder':'YYYY-MM-DD'}), 
            'alertment_date' :forms.DateInput(attrs={'class':'form-control', 'placeholder':'YYYY-MM-DD'}), 
            'product_image' :forms.ClearableFileInput(attrs={'class':'form-control'}), 
        }

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['mobile_no', 
        'user', 
        'name', 
        'email', 
        'locality', 
        'city', 
        'zipcode', 
        'state'
        ]
        Widgets = {
            'mobile_no' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Mobile No'}), 
            'user' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Username'}), 
            'name' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Fullname'}), 
            'email' :forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Email'}), 
            'locality' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Locality'}), 
            'city' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the City'}), 
            'zipcode' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Zipcode'}), 
            'state':forms.Select(attrs={'class':'form-control', 'placeholder':'Select'})
        }

class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields =['product', 'pimage']
        widgets = {
            'product' :forms.Select(attrs={'class':'form-control', 'placeholder':'Select'}), 
            'pimage' :forms.FileInput(attrs={'class':'form-control'})
        }

class CartForm(ModelForm):
    class Meta:
        model = Cart
        fields = ['cart_id', 'customer', 'product', 'quantity']
        Widgets = {
            'cart_id' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Id No'}),
            'customer' :forms.Select(attrs={'class':'form-control', 'placeholder':'Select'}),
            'product' :forms.Select(attrs={'class':'form-control', 'placeholder':'Select'}),
            'quantity' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Quantity'})
        }

class OrderPlacedForm(ModelForm):
    class Meta:
        model = OrderPlaced
        fields = ['user', 'customer', 'product', 'quantity', 'order_date', 'status']
        widgets = {
            'user' :forms.Select(attrs={'class':'form-control', 'placeholder':'Select'}), 
            'customer' :forms.Select(attrs={'class':'form-control', 'placeholder':'Select'}), 
            'product' :forms.Select(attrs={'class':'form-control', 'placeholder':'Select'}), 
            'quantity' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Quantity'}), 
            'order_date' :forms.DateInput(attrs={'class':'form-control', 'placeholder':'YYYY-MM-DD'}), 
            'status' :forms.Select(attrs={'class':'form-control', 'placeholder':'Select'})
        }

class CouponForm(ModelForm):
    class Meta:
        model = Coupon
        fields = ['code', 'valid_from', 'valid_to', 'discount', 'active']                                   
        input_type = 'date'                                                                                                                                                                                                                                                                                                                                                                                                                        
        Widgets ={
            'code' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the CouponCode'}), 
            'valid_from' :forms.DateInput(attrs={'class':'form-control', 'type':'date', 'placeholder':'YYYY-MM-DD'}), 
            'valid_to' :forms.DateInput(attrs={'class':'form-control', 'placeholder':'YYYY-MM-DD'}), 
            'discount' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Discount Value'}), 
            'active' :forms.CheckboxInput(attrs={'class':'form-control'})
        }

class TaxForm(ModelForm):
    class Meta:
        model = Tax
        fields = ('tax_type', 'value')
        Widgets ={
            'tax_type' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Tax Type'}), 
            'value' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Tax Value in %'})
        }

class ColorForm(ModelForm):
    class Meta:    
        model = Color
        fields = ('color_code', 'item_color')
        widgets = {
            'color_code' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Color Code'}), 
            'item_color' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Color'})
        }

class SizeForm(ModelForm):
    class Meta:
        model = Size
        fields = ('size_code', 'item_size')
        Widgets = {
            'size_code' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Size Code'}), 
            'item_size' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Size'})
        }
class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = ['supplier_code', 'supplier', 'address', 'contact_no', 'supplier_email', 'gstin_no', 'state', 'pin']
        widgets = {
            'supplier_code' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Supplier Code'}), 
            'supplier' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Name'}), 
            'address' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Sup. Address'}), 
            'contact_no' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Contact No'}), 
            'supplier_email' :forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Supplier Email'}), 
            'gstin_no' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the GSTIN No'}), 
            'state' :forms.Select(attrs={'class':'form-control', 'placeholder':'Select'}), 
            'pin' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Pincode'})
        }

class ItemgroupForm(ModelForm):
    class Meta:
        model = Itemgroup
        fields = ['item_group_code', 'item_group_name', 'item_group_description']
        widgets = {
            'item_group_code' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Group Code'}), 
            'item_group_name' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Group Name'}), 
            'item_group_description' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Group Description'}), 
        }

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['item_group_name', 'category_code', 'category_name']
        widgets = {
           'item_group_name' :forms.Select(attrs={'class':'form-control', 'placeholder':'Select'}), 
           'category_code' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Category Code'}), 
           'category_name' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Category Name'}), 
        }

class PurchaseForm(ModelForm):
    class Meta:
        model = Purchase
        fields = [
            'trans_date', 
            'pur_bill_no', 
            'supplier_name', 
            'total_qty', 
            'gross_amt', 
            'disc_amt', 
            'gst_amt', 
            'tcs', 
            'o_charge', 
            'o_disc', 
            'grand_total'
        ]
        widgets = {
            'trans_date' :forms.DateInput(attrs={'class':'form-control', 'placeholder':'YYYY-MM-DD'}),
            'pur_bill_no' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter The Bill No'}), 
            'supplier_name' :forms.Select(attrs={'class':'form-control', 'placeholder':'Select'}), 
            'total_qty' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter The Total Quantity'}), 
            'gross_amt' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter The Gross Amount'}), 
            'disc_amt' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter The Discounted Amount'}), 
            'gst_amt' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter The GST Amount'}), 
            'tcs' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter The TCS Amount'}), 
            'o_charge' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter The Overall Charge'}), 
            'o_disc' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter The Overall Discount'}), 
            'grand_total' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter The Grand Total'})
        }


# class UserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
#         Widgets ={
#             'username' :forms.TextInput(attrs={'class':'form-control'}), 
#             'email' :forms.EmailInput(attrs={'class':'form-control'}), 
#             'password1' :forms.PasswordInput(attrs={'class':'form-control'}), 
#             'password2' :forms.PasswordInput(attrs={'class':'form-control'})
#         }