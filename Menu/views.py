# views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView,TemplateView
from .models import *
from .forms import OrderForm,  ProductForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth import logout
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

@login_required
def user_logout(request):
    logout(request) 
    return render(request, 'registration/log_out.html') 

def login(request):
    return redirect("accounts/login/")


class Base(TemplateView):
    template_name = "base.html"


# Order

class OrderListView(ListView):
    model = Book
    template_name = 'o_list.html'




class OrderCreateView(CreateView):
    model = Book
    form_class = OrderForm
    template_name = 'o_cr.html'
    success_url = reverse_lazy('o_list')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class OrderUpdateView(UpdateView):
    model = Book
    form_class = OrderForm
    template_name = 'o_up.html'
    success_url = reverse_lazy('o_list')

    
    def get_queryset(self):
        return Book.objects.filter(user = self.request.user)

class OrderDeleteView(PermissionRequiredMixin,DeleteView):
    model = Book
    template_name = 'o_delete.html'
    success_url = reverse_lazy('o_list')
    permission_required = "view_order"
    permission_denied_message = "Shumo nametavoned dida!"
    
    def get_queryset(self):
        return Book.objects.filter(user = self.request.user)

class OrderDetailView(DetailView):
    model = Book
    template_name = 'o_detail.html'
    context_object_name = "object"
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["vakansi"] = Borrow.objects.filter(book = self.kwargs['pk'])
        return context





class ProductListView(ListView):
    model = Borrow
    template_name = 'p_list.html'


class ProductCreateView(CreateView):
    model = Borrow
    form_class = ProductForm
    template_name = 'p_cr.html'
    success_url = reverse_lazy('p_list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProductUpdateView(UpdateView):
    model = Borrow
    form_class = ProductForm
    template_name = 'p_up.html'
    success_url = reverse_lazy('p_list')
    
    def get_queryset(self):
        return Borrow.objects.filter(user = self.request.user)

class ProductDeleteView(DeleteView):
    model = Borrow
    template_name = 'p_delete.html'
    success_url = reverse_lazy('p_list')
    
    def get_queryset(self):
        return Borrow.objects.filter(user = self.request.user)

class ProductDetailView(DetailView):
    model = Borrow
    template_name = 'p_detail.html'
    context_object_name = "object"