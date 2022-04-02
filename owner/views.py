from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from owner.decorators import owner_sign_in_required
from owner.form import Bookform, OrderProcessForm
from owner.models import Books
from customer.models import Orders
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail


# Create your views here.

# fn based
# def index(request):
#     return render(request, "owner_index.html")

# def view_books(request):
#        return render(request,"view_books.html")
#
# def add_books(request):
#     return render(request,"owner_add_books.html")
#
#
# def view_customer_order(request):
#     return render(request,"owner_view_order")

# class based


@method_decorator(owner_sign_in_required, name="dispatch")
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, "owner_index.html")


@method_decorator(owner_sign_in_required, name="dispatch")
class Book_list(ListView):
    model = Books
    context_object_name = "books"
    template_name = "book_list.html"
    # def get(self, request, *args, **kwargs):
    #     qs = Books.objects.all()
    #     context = {"books": qs}
    #     return render(request, "book_list.html", context)


@method_decorator(owner_sign_in_required, name="dispatch")
class Addbook(CreateView):
    model = Books
    form_class = Bookform
    template_name = "owner_add_books.html"
    success_url = reverse_lazy("listbook")

    # def get(self, request, *args, **kwargs):
    #     form = Bookform()
    #     context = {"form": form}
    #     return render(request, "owner_add_books.html", context)
    #
    # def post(self, request, *args, **kwargs):
    #     # id = kwargs["id"]
    #     # qs = Books.objects.get(id=id)
    #     form = Bookform(request.POST, files=request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, "book has been added")
    #         return redirect("addbook")
    #     else:
    #         context = {"form": form}
    #         messages.error(request, "book adding failed")
    #         return render(request, 'owner_add_books.html', context)


# mobile_name = form.cleaned_data.get("mobile_name")
# price = form.cleaned_data.get("price")
# RAM_ROM = form.cleaned_data.get("RAM_ROM")
# processor = form.cleaned_data.get("processor")
# rear_camera = form.cleaned_data.get("rear_camera")
# front_camera = form.cleaned_data.get("front_camera")
# battery = form.cleaned_data.get("battery")
# display = form.cleaned_data.get("display")
# stock = form.cleaned_data.get("stock")

# ORM Query
# qs = Mobiles(
#     mobile_name=form.cleaned_data.get("mobile_name"),
#     price=form.cleaned_data.get("price"),
#     RAM_ROM=form.cleaned_data.get("RAM_ROM"),
#     processor=form.cleaned_data.get("processor"),
#     rear_camera=form.cleaned_data.get("rear_camera"),
#     front_camera=form.cleaned_data.get("front_camera"),
#     battery=form.cleaned_data.get("battery"),
#     display=form.cleaned_data.get("display"),
#     stock=form.cleaned_data.get("stock")
# )
# qs.save()


@method_decorator(owner_sign_in_required, name="dispatch")
class Vieworder(View):
    def get(self, request, *args, **kwargs):
        return render(request, "owner_view_order.html")


@method_decorator(owner_sign_in_required, name="dispatch")
class Bookdetails(DetailView):  # for display detail of each book
    model = Books
    context_object_name = "book"
    template_name = "book_details.html"
    success_url = reverse_lazy("bookdetails")

    # def get(self, request, *args, **kwargs):
    #     id = kwargs["id"]
    #     qs = Books.objects.get(id=id)
    #     context = {"book": qs}
    #     return render(request, "book_details.html", context)
    #
    # def post(self, request, *args, **kwargs):
    #     id = kwargs["id"]
    #     qs = Books.objects.get(id=id)
    #     form = Bookform(request.POST, instance=qs, files=request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("bookdetails")


@method_decorator(owner_sign_in_required, name="dispatch")
class Bookchange(UpdateView):
    model = Books
    form_class = Bookform
    template_name = "book_edit.html"
    success_url = reverse_lazy("listbook")

    # def get(self, request, *args, **kwargs):
    #     print(kwargs)
    #     id = kwargs["id"]
    #     qs = Books.objects.get(id=id)
    #     form = Bookform(instance=qs)
    #     return render(request, "book_edit.html", {"form": form})
    #
    # def post(self, request,*args, **kwargs):
    #     id = kwargs["id"]
    #     qs = Books.objects.get(id=id)
    #     form = Bookform(request.POST, instance=qs, files=request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("listbook")


@method_decorator(owner_sign_in_required, name="dispatch")
class BookDelete(DeleteView):
    template_name = "book_delete.html"
    # pk_url_kwarg = "id"
    success_url = reverse_lazy("listbook")
    model = Books

    # def get(self, request, *args, **kwargs):
    #     id = kwargs["id"]
    #     book = Books.objects.get(id=id)
    #     book.delete()
    #     return redirect("listbook")


@method_decorator(owner_sign_in_required, name="dispatch")
class OwnerDashBoard(ListView):
    model = Orders
    template_name = "owner_dashboard.html"

    def get(self, request, *args, **kwargs):
        new_orders = self.model.objects.filter(status="order_placed")
        context = {"n_orders": new_orders}
        return render(request, self.template_name, context)


@method_decorator(owner_sign_in_required, name="dispatch")
class OrderDetails(DetailView):
    model = Orders
    template_name = "order_details.html"
    context_object_name = "order"
    pk_url_kwarg = "o_id"


@method_decorator(owner_sign_in_required, name="dispatch")
class OrderProcessView(UpdateView):
    model = Orders
    pk_url_kwarg = "id"
    template_name = "order_process.html"
    form_class = OrderProcessForm
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        self.object = form.save()
        expected_date = form.cleaned_data.get("expected_delivery_date")
        send_mail(
            'Book Order Conformation',
            'Your order will be delivered on ' + str(expected_date),
            'apsarasunil333@gmail.com',
            ['aravindsunil94@gmail.com'],
            fail_silently=False,
        )
        return super().form_valid(form)


def sign_out(request):
    logout(request)
    return redirect("signin")
