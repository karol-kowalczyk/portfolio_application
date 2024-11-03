from django.urls import path
from .views import stocks_overview, stocks_data, slug_data_view


urlpatterns = [
    path('', stocks_overview),
    path('stocks_data/<int:stocks_id>', stocks_data),
    path('stocks_data/<slug:slug_id>', slug_data_view),
]
