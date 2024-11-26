from django.urls import path
from core.views.entreprise import BusinessDetailView
from core.views.asset import AssetStatusUpdateView, AssetListView

app_name = 'core'

urlpatterns = [
    path('entreprise/<int:pk>/', BusinessDetailView.as_view(), name='business_detail'),
    path('actifs/<str:status>/', AssetListView.as_view(), name='asset_list'),
    path('actifs/<int:pk>/modifier/', AssetStatusUpdateView.as_view(), name='asset_update'),
]
