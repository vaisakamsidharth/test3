from django import forms
from django.forms import ModelForm
from owner.models import Books
from customer.models import Orders


# class MobileForm(forms.Form):
#     mobile_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
#     price = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}))
#     RAM_ROM = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
#     processor = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
#     rear_camera = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
#     front_camera = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
#     battery = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
#     display = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
#     stock = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}))
#
#     def clean(self):
#         cleaned_data = super().clean()
#         price = cleaned_data.get("price")
#         stock = cleaned_data.get("stock")
#         if price < 0:
#             msg = "invalid price"
#             self.add_error("price", msg)
#         if stock < 0:
#             msg = "invalid stock"
#             self.add_error("stock", msg)


class Bookform(ModelForm):

   class Meta:

        model = Books
        # exclude = ("active_status",)
        fields = "__all__"
        widgets = {
            "book_name": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "copies": forms.NumberInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),

        }

        def clean(self):

            cleaned_data = super().clean()
            price = int(cleaned_data["price"])
            copies = int(cleaned_data["copies"])
            if price < 0:
                print("value<0")
                msg = "invalid price"
                self.add_error("price", msg)
            if copies < 0:
                print("value<0")
                msg = "invalid copies"
                self.add_error("copies", msg)


class OrderProcessForm(ModelForm):

    class Meta:
        model = Orders
        fields = ["status", "expected_delivery_date"]
        widgets = {
            "status": forms.Select(attrs={"class": "form-control"}),
            "expected_delivery_date": forms.DateInput(attrs={"class": "form-control", "type": "date"})
        }
