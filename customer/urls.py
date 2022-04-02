from django.urls import path
from customer import views

urlpatterns = [
    path("home", views.CustomerHome.as_view(), name="listall_books"),
    path("feedback/", views.FeedBackView.as_view()),
    path("accounts/signup", views.SignUpView.as_view(), name="signup"),
    path("", views.LogInView.as_view(), name="signin"),
    path("accounts/logout", views.sign_out, name="signout"),
    path("customer/carts/add/<int:id>", views.AddToCartView.as_view(), name="addtocart"),
    path("customer/carts/items", views.CartItems.as_view(), name="cartitems"),
    path("customer/carts/items/remove/<int:id>", views.RemoveCartItems.as_view(), name="remove_item"),
    path("customer/orders/add/<int:p_id>/<int:c_id>", views.OrderCreate.as_view(), name="order_create"),
    path("customer/orders", views.MyOrdersView.as_view(), name="my_orders"),
    path("customer/orders/remove/<int:id>", views.cancel_order, name="cancel_order"),
    path("profile/add", views.ProfileView.as_view(), name="cust_profile"),
    path("customer/my_profile", views.ViewMyProfile.as_view(), name="my_profile"),
]
