from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group

from .models import LaundryOrder
from .user_roles import AdminRole, CustomerRole, DriverRole


# =======================
# AUTH
# =======================

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Arahkan sesuai role
            if user.groups.filter(name="Admin").exists():
                return redirect("admin_dashboard")
            elif user.groups.filter(name="Customer").exists():
                return redirect("customer_dashboard")
            elif user.groups.filter(name="Driver").exists():
                return redirect("driver_dashboard")
            else:
                return render(request, "login.html", {"error": "User belum punya role."})

        # kalau user None
        return render(request, "login.html", {"error": "Username atau password salah!"})

    return render(request, "login.html")


def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        if password != password2:
            return render(request, "register.html", {"error": "Password tidak sama."})

        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {"error": "Username sudah digunakan."})

        # buat user baru
        user = User.objects.create_user(username=username, password=password)

        # otomatis masuk group Customer
        customer_group, _ = Group.objects.get_or_create(name="Customer")
        user.groups.add(customer_group)

        return redirect("login")

    return render(request, "register.html")


# =======================
# ADMIN
# =======================

@login_required(login_url="login")
def admin_dashboard(request):
    role_obj = AdminRole(request.user.username)

    orders = LaundryOrder.objects.all().select_related("customer").order_by("-created_at")

    total_orders = orders.count()
    active_orders = orders.exclude(status="done").count()
    pending_orders = orders.filter(status="request").count()
    done_orders = orders.filter(status="done").count()

    context = {
        "role": role_obj.get_role_name(),
        "username": request.user.username,
        "orders": orders,
        "total_orders": total_orders,
        "active_orders": active_orders,
        "pending_orders": pending_orders,
        "done_orders": done_orders,
        "menu": "dashboard",
    }
    return render(request, "admin_dashboard.html", context)


@login_required(login_url="login")
def admin_customers(request):
    role_obj = AdminRole(request.user.username)

    # bikin ringkasan pelanggan dari semua order
    orders = LaundryOrder.objects.select_related("customer")
    customer_map = {}
    for o in orders:
        u = o.customer
        if u.id not in customer_map:
            customer_map[u.id] = {"user": u, "total_orders": 0}
        customer_map[u.id]["total_orders"] += 1

    customers = list(customer_map.values())

    context = {
        "role": role_obj.get_role_name(),
        "username": request.user.username,
        "customers": customers,
        "menu": "customers",
    }
    return render(request, "admin_customers.html", context)


@login_required(login_url="login")
def admin_orders(request):
    role_obj = AdminRole(request.user.username)
    orders = LaundryOrder.objects.all().select_related("customer").order_by("-created_at")

    context = {
        "role": role_obj.get_role_name(),
        "username": request.user.username,
        "orders": orders,
        "menu": "orders",
    }
    return render(request, "admin_orders.html", context)


@login_required(login_url="login")
def admin_reports(request):
    role_obj = AdminRole(request.user.username)
    orders = LaundryOrder.objects.all().select_related("customer")

    total_orders = orders.count()
    done_orders = orders.filter(status="done").count()
    active_orders = orders.exclude(status="done").count()
    pending_orders = orders.filter(status="request").count()

    reguler = orders.filter(service_type="reguler").count()
    express = orders.filter(service_type="express").count()
    kilat = orders.filter(service_type="kilat").count()

    # total estimasi pendapatan (pakai property total_price di model)
    total_revenue = sum(o.total_price for o in orders)

    context = {
        "role": role_obj.get_role_name(),
        "username": request.user.username,
        "menu": "reports",
        "total_orders": total_orders,
        "done_orders": done_orders,
        "active_orders": active_orders,
        "pending_orders": pending_orders,
        "reguler": reguler,
        "express": express,
        "kilat": kilat,
        "total_revenue": total_revenue,
    }
    return render(request, "admin_reports.html", context)


# =======================
# CUSTOMER
# =======================

@login_required(login_url="login")
def customer_dashboard(request):
    role_obj = CustomerRole(request.user.username)

    if request.method == "POST":
        address = request.POST.get("address")
        service_type = request.POST.get("service_type")
        pickup_time = request.POST.get("pickup_time")
        weight_kg = request.POST.get("weight_kg")
        note = request.POST.get("note")

        if address and service_type:
            LaundryOrder.objects.create(
                customer=request.user,
                address=address,
                service_type=service_type,
                pickup_time=pickup_time or "",
                weight_kg=weight_kg or 0,
                note=note or "",
            )

    orders = LaundryOrder.objects.filter(customer=request.user).order_by("-created_at")

    context = {
        "role": role_obj.get_role_name(),
        "username": request.user.username,
        "orders": orders,
    }
    return render(request, "customer_dashboard.html", context)


# =======================
# DRIVER
# =======================

@login_required(login_url="login")
def driver_dashboard(request):
    role_obj = DriverRole(request.user.username)

    if request.method == "POST":
        order_id = request.POST.get("order_id")
        new_status = request.POST.get("new_status")

        if order_id and new_status:
            try:
                order = LaundryOrder.objects.get(id=order_id)
                order.status = new_status
                order.save()
            except LaundryOrder.DoesNotExist:
                pass

    orders = (
        LaundryOrder.objects.exclude(status="done")
        .select_related("customer")
        .order_by("-created_at")
    )

    context = {
        "role": role_obj.get_role_name(),
        "username": request.user.username,
        "orders": orders,
    }
    return render(request, "driver_dashboard.html", context)


# =======================
# LOGOUT
# =======================

@login_required(login_url="login")
def logout_view(request):
    logout(request)
    return redirect("login")
