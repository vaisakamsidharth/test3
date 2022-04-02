from django.shortcuts import render, redirect
from customer.forms import FeedBackForm, UserRegistrationForm, LogInForm, OrderForm, ProfileForm
from django.views.generic import View, ListView, CreateView, TemplateView
from owner.models import Books
from django.contrib.auth import authenticate, login, logout
from customer.decorators import sign_in_required
from django.utils.decorators import method_decorator
from customer.models import Carts, Orders, Profile
from django.db.models import Sum
from django.contrib import messages
from customer.filters import BookFilter
from django.urls import reverse_lazy

# Create your views here.


# fn based view

# def index(request):
#     return render(request,"cust_index.html")
#
# def view_my_cart(request):
#     return render(request,"cust_index.html")
#
# def view_my_orders(request):
#     return render(request,"cust_view_order.html")

@method_decorator(sign_in_required, name="dispatch")
class CustomerHome(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            qs = Books.objects.all()
            f = BookFilter(request.GET, queryset=Books.objects.all())
            context = {"books": qs, "filter": f}
            return render(request, "cust_index.html", context)


class SignUpView(View):
    def get(self, request):
        form = UserRegistrationForm()
        context = {"form": form}
        return render(request, "signup.html", context)

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("user created")
            return render(request, "login.html")
        else:
            context = {"form": form}
            return render(request, "signup.html", context)


class LogInView(View):
    def get(self, request, *args, **kwargs):
        form = LogInForm()
        context = {"form": form}
        return render(request, "login.html", context)

    def post(self, request):
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                if request.user.is_superuser:
                    return redirect("listbook")
                else:
                    return redirect("listall_books")
            else:
                context = {"form": form}
                return render(request, "login.html", context)


@method_decorator(sign_in_required, name="dispatch")
class AddToCartView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs["id"]
        book = Books.objects.get(id=id)
        user = request.user
        cart = Carts(user=user, item=book)
        cart.save()
        print("item has been added to cart")
        return redirect("listall_books")


@method_decorator(sign_in_required, name="dispatch")
class CartItems(ListView):
    model = Carts
    template_name = "cart_items.html"
    context_object_name = "items"

    # def get_queryset(self):
    #     return self.model.objects.filter(user=self.request.user)

    def get(self, request, *args, **kwargs):
        qs = self.model.objects.filter(user=self.request.user).exclude(status="cancelled")

        total_sum = qs.aggregate(Sum("item__price"))
        total = total_sum["item__price__sum"]

        context = {"items": qs, "total": total}
        return render(request, self.template_name, context)


@method_decorator(sign_in_required, name="dispatch")
class RemoveCartItems(View):
    model = Carts

    def get(self, request, **kwargs):
        id = kwargs["id"]
        cart = Carts.objects.get(id=id)
        cart.status = "cancelled"
        cart.save()
        return redirect("listall_books")


@method_decorator(sign_in_required, name="dispatch")
class OrderCreate(CreateView):
    model = Orders
    template_name = "cust_view_order.html"
    form_class = OrderForm

    # def post(self, request, *args, **kwargs):
    #     p_id = kwargs.get("p_id")
    #     c_id = kwargs.get("c_id")
    #     form = OrderForm(request.POST)
    #
    #     if form.is_valid():
    #         cart = Carts.objects.get(id=c_id)
    #         address = form.cleaned_data.get("address")
    #         book = Books.objects.get(id=p_id)
    #         user = request.user
    #         order = Orders(item=book, user=user, address=address)
    #         order.save()
    #         cart.status = "order_placed"
    #         cart.save()
    #         messages.success(request, "your order has been placed")
    #         return redirect('listall_books')


@method_decorator(sign_in_required, name="dispatch")
class MyOrdersView(ListView):
    model = Orders
    context_object_name = "orders"
    template_name = "my_orders.html"

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user).exclude(status="cancelled")


@method_decorator(sign_in_required, name="dispatch")
def cancel_order(request, *args, **kwargs):
    o_id = kwargs.get("id")
    order = Orders.objects.get(id=o_id)
    order.status = "cancelled"
    order.save()
    messages.success("your order has been cancelled")
    return redirect("listall_books")


@method_decorator(sign_in_required, name="dispatch")
class ProfileView(CreateView):
    model = Profile
    template_name = "cust_profile.html"
    form_class = ProfileForm

    # def post(self, request):
    #     form = self.form_class(request.POST, files=request.FILES)
    #     if form.is_valid():
    #         profile = form.save(commit=False)
    #         profile.user = request.user
    #         profile.save()
    #         return redirect("listall_books")
    #     else:
    #         return render(request, self.template_name, {"form": form})


@method_decorator(sign_in_required, name="dispatch")
class ViewMyProfile(TemplateView):
    template_name = "my_profile.html"


@method_decorator(sign_in_required, name="dispatch")
class FeedBackView(View):
    def get(self, request, *args, **kwargs):
        form = FeedBackForm()
        context = {"form": form}
        return render(request, "add_feedback.html", context)

    def post(self, request):
        form = FeedBackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request, "add_feedback.html")


def sign_out(request):
    logout(request)
    return redirect("signin")




