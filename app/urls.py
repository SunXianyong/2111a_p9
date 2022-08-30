from django.urls import include, path
from rest_framework import routers

from app.views import hello, alipay_callback

metrics_router = routers.DefaultRouter()
metrics_router.register('', hello)

urlpatterns = [
    # path('look/', routers.views.get_view_name(hello.hello)),
    path('user/', include(metrics_router.urls)),
    path('page_pay/', alipay_callback.page_pay_return),

]
