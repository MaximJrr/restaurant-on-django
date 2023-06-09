from django.contrib.auth.decorators import login_required
from django.forms import model_to_dict
from django.shortcuts import HttpResponseRedirect
from django.views.generic import ListView, TemplateView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from common.views import TitleMixin
from dishes.models import Basket, Dish, DishCategory


class IndexView(TitleMixin, TemplateView):
    active_section = 'index'
    template_name = 'dishes/index.html'
    title = 'Restaurant'


class DishesListView(TitleMixin, ListView):
    active_section = 'menu'
    model = Dish
    template_name = 'dishes/menu.html'
    context_object_name = 'dishes'
    paginate_by = 4
    title = 'Restaurant - menu'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishesListView, self).get_context_data()
        context['title'] = 'Menu'
        return context


@login_required
def basket_add(request, dish_id):
    dish = Dish.objects.get(id=dish_id)
    Basket.add_or_update_basket(dish, request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])




