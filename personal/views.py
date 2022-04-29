from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

class Home(ListView):
    template_name = 'index.html'
    context_object_name = 'portfolios'
    queryset = Portfolio.objects.all()

    def get_queryset(self):
        return Portfolio.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        # here we can add so many context using that way
        context['portfolios'] = Portfolio.objects.all()
        context['blogs'] = Blog.objects.all()
        context['partners'] = Partner.objects.all()
        return context

class PortfolioDetail(DetailView):
    template_name = 'portfolio-details.html'
    context_object_name = 'portfolio'
    queryset = Portfolio.objects.all()

class BlogDetail(DetailView):
    template_name = 'blog-single.html'
    context_object_name = 'blog'
    queryset = Blog.objects.all()
