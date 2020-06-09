"""web_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
import web.views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    url(r'^admin/', admin.site.urls),

    # url(r'^data.json$', web.views.data_json),

    # url(r'^polls/to_graph$', web.views.to_graph),

    url(r'^$',  web.views.home_page),

    url('polls/home', web.views.home_page),

    url('polls/realtime_analysis', web.views.realtime_analysis),

    url('polls/detail_analysis', web.views.detail_analysis),

    url('polls/two_detail_analysis', web.views.two_detail_analysis),

    url('polls/synthesis_detail_analysis', web.views.synthesis_detail_analysis),

    url('polls/main_realtime_analysis', web.views.main_realtime_analysis),

    url('polls/to_graph', web.views.to_graph),

    url('polls/two_to_graph', web.views.two_to_graph),

    url('polls/backup', web.views.backup),

    url('polls/two_backup', web.views.two_backup),

    url('polls/test_page', web.views.test_page),

    url('polls/goto_test_page', web.views.goto_test_page),

    url('polls/goto_log', web.views.goto_log),

    url('polls/detail_graph_one', web.views.detail_graph_one),

    url('polls/detail_graph_DR_onevsT', web.views.detail_graph_DR_onevsT),

    url('polls/detail_graph_DR_progresses', web.views.detail_graph_DR_progresses),

    url('polls/goto_get_quantity', web.views.goto_get_quantity),

    url('polls/two_goto_get_quantity', web.views.two_goto_get_quantity),

    url('polls/goto_reflec', web.views.goto_reflec),

    url('polls/two_detail_graph_one', web.views.two_detail_graph_one),

    url('polls/two_detail_graph_DR_onevsT', web.views.two_detail_graph_DR_onevsT),

    url('polls/two_goto_reflec', web.views.two_goto_reflec),

]

