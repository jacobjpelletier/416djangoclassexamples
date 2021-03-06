"""djangoProject1 URL Configuration

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

"""
from django.contrib import admin
from django.urls import path, include

import djangoProject1.views

urlpatterns = [
    path('', djangoProject1.views.index),
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
]
"""

''' MODELS urls.py below'''

"""TodoList URL Configuration

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
from django.contrib import admin
from django.urls import path, include
import djangoProject1.views

urlpatterns = [
    path('', djangoProject1.views.index),
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
    path('tasksWithModels/', include('tasksWithModels.urls')),
    path('contact/', include('contact.urls')),
    path('products/', include('products.urls')),
    path('auth/', include('authorization.urls')),
]
