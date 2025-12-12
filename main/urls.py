from django.urls import path
from .views import (
    login_view,
    register_view,
    admin_dashboard,
    admin_customers,
    admin_orders,
    admin_reports,
    customer_dashboard,
    driver_dashboard,
    logout_view,
)

urlpatterns = [
    path("", login_view, name="login"),
    path("register/", register_view, name="register"),

    # ADMIN
    path("admin-dashboard/", admin_dashboard, name="admin_dashboard"),
    path("admin-customers/", admin_customers, name="admin_customers"),
    path("admin-orders/", admin_orders, name="admin_orders"),
    path("admin-reports/", admin_reports, name="admin_reports"),

    # CUSTOMER
    path("customer-dashboard/", customer_dashboard, name="customer_dashboard"),

    # DRIVER
    path("driver-dashboard/", driver_dashboard, name="driver_dashboard"),

    # LOGOUT
    path("logout/", logout_view, name="logout"),
]
