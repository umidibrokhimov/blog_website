from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Portfolio

class Home(ListView):
    template_name = 'index.html'
    context_object_name = 'portfolios'
    queryset = Portfolio.objects.all()

class PortfolioDetail(DetailView):
    template_name = 'portfolio-details.html'
    context_object_name = 'portfolio'
    queryset = Portfolio.objects.all()