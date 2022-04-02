from django.urls import path
from owner import views


# class base

urlpatterns = [
    path("add_books/add", views.Addbook.as_view(), name="addbook"),
    path("view_books/all", views.Book_list.as_view(), name="listbook"),
    path("view_books/<int:pk>", views.Bookdetails.as_view(), name="bookdetails"),
    path("view_books/change/<int:pk>", views.Bookchange.as_view(), name="bookedit"),
    path("books/remove/<int:pk>", views.BookDelete.as_view(), name="deletebook"),
    path("dashboard", views.OwnerDashBoard.as_view(), name="dashboard"),
    path("orders:<int:o_id>", views.OrderDetails.as_view(), name="order_details"),
    path("orders/process/<int:id>", views.OrderProcessView.as_view(), name="order_process"),

]
