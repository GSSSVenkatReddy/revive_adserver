"""ads URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addAdvertiser/', views.add_advertiser),
    path('getAdvertiser/', views.get_advertiser),
    path('modifyAdvertiser/', views.modify_advertiser),
    path('deleteAdvertiser/', views.delete_advertiser),
    path('addCampaign/', views.add_campaign),
    path('getCampaign/', views.get_campaign),
    path('modifyCampaign/', views.modify_campaign),
    path('deleteCampaign/', views.delete_campaign),
    path('addBanner/', views.add_banner),
    path('getBannersByCampaign/', views.get_banners_by_campaign),
    path('getBanner/', views.get_banner),
    path('modifyBanner/', views.modify_banner),
    path('deleteBanner/', views.delete_banner),
    path('setBannerTargeting/', views.set_banner_targeting),
    path('getBannerTargeting/', views.get_banner_targeting),
    path('linkCampaignWithBannerToZone/', views.link_campaign_with_banner_to_zone),
    path('unlinkCampaignFromZone/', views.unlink_campaign_from_zone),
    path('unlinkBannerFromZone/', views.unlink_banner_from_zone),
    path('getCampaignListByZone/', views.get_campaign_list_by_zone),
    path('getBannerListByZone/', views.get_banner_list_by_zone),
    path('getStatisticsOfBanner/', views.get_statistics_of_banner),
    path('getZoneByBanner/', views.get_zone_by_banner),
    path('test/', views.test),
    path('getAllAdvertisers/', views.get_all_advertisers),
]
