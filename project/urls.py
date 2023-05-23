"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from core.views import index, fill_steps

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__reload__/', include('django_browser_reload.urls')),
    path("<str:type_form>/<int:step>/", fill_steps, name="forms_steps"),

    # path('psicologa/2/', fill_step_2),
    #  path('psicologa/3/', fill_step_3),
    # path('advogada/', fill_step_1),
    # path('advogada/2/', fill_step_2),
    # path('advogada/3/', fill_step_3),

    path('', index),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
