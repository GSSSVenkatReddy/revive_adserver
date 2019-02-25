from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.models import *
import datetime
import shutil
from django.db.models import Sum


# Create your views here.


# Add Advertiser
@csrf_exempt
def add_advertiser(request):
    if request.method == 'POST':
        print(request)
        res = request.body.decode('utf-8')
        print(res)
        dict = eval(res)
        print(dict)
        insert1 = RvAccounts.objects.create(account_name=dict['account_name'], account_type='ADVERTISER')
        insert1.save()
        date = datetime.datetime.now()
        x = str(date).split(' ')
        rld = x[0]
        dnt = x[1][:8]
        acc_id = insert1.account_id
        insert2 = RvClients(agencyid=1, clientname=dict['account_name'], contact=dict['contact'], email=dict['email'],
                            report='f', reportinterval=7, reportlastdate=rld, reportdeactivate='t', comments='',
                            updated=rld + ' ' + dnt, account_id=acc_id, advertiser_limitation=0, type=0)
        insert2.save()
        return JsonResponse({'response': 'success', 'account_id': insert1.account_id})


# Get Advertiser
def get_advertiser(request):
    if request.method == 'GET':
        acc_id = request.GET['account_id']
        res = RvClients.objects.get(account_id=acc_id)
        res1 = {'clientid': res.clientid, 'clientname': res.clientname, 'contact': res.contact, 'email': res.email}
        return JsonResponse(res1)


# Get All Advertisers
def get_all_advertisers(request):
    if request.method == 'GET':
        total = RvAccounts.objects.filter(account_type='ADVERTISER')
        js = []
        for i in total:
            advertisers = {'account_id': i.account_id, 'account_name': i.account_name}
            js.append(advertisers)
        return JsonResponse(js, safe=False)


# Modify Advertiser
@csrf_exempt
def modify_advertiser(request):
    if request.method == 'PUT':
        res = request.body.decode('utf-8')
        dict = eval(res)
        update = RvClients.objects.get(account_id=dict['account_id'])
        update.contact = dict['contact']
        update.email = dict['email']
        update.save()
        return JsonResponse({'response': 'updated'})


# Delete Advertiser
def delete_advertiser(request):
    if request.method == 'GET':
        acc_id = request.GET['account_id']
        del1 = RvAccounts.objects.get(account_id=acc_id)
        del2 = RvClients.objects.get(account_id=acc_id)
        # deleting campaigns and banners related to advertiser
        client_id = del2.clientid
        del3 = RvCampaigns.objects.filter(clientid=client_id)

        # deleting all banners related to campaigns
        for i in del3:
            RvBanners.objects.filter(campaignid=i.campaignid).delete()

        # deleting all campaigns related to advertiser
        del3.delete()

        # deleting data from rv_clients table
        del2.delete()

        # deleting data from rv_accounts table
        del1.delete()
        return JsonResponse({'response': 'deleted'})


# Add Campaign
@csrf_exempt
def add_campaign(request):
    if request.method == 'POST':
        res = request.body.decode('utf-8')
        dict = eval(res)
        # print(dict)
        acc_id = dict['account_id']
        cid = RvClients.objects.filter(account_id=acc_id)
        client_id = cid[0].clientid
        today = datetime.datetime.now()
        x = str(today).split(' ')
        dates = x[0]
        times = x[1][:8]
        insert1 = RvCampaigns.objects.create(campaignname=dict['campaignname'], clientid=client_id, views=-1,
                                             clicks=-1, conversions=-1, priority=0, weight=1, target_impression=0,
                                             target_click=0, target_conversion=0, anonymous='f', companion=0,
                                             comments='', revenue=1.0000, revenue_type=1, updated=dates + ' ' + times,
                                             block=0, capping=0, session_capping=0, status=0, hosted_views=0,
                                             hosted_clicks=0, viewwindow=0, clickwindow=0, ecpm=0, min_impressions=100,
                                             ecpm_enabled=0, activate_time=dates + ' ' + times, type=0,
                                             show_capped_no_cookie=0)
        insert1.save()
        return JsonResponse({'response': 'success', 'campaignid': insert1.campaignid})


# Get Campaign
def get_campaign(request):
    if request.method == 'GET':
        acc_id = request.GET['account_id']
        res = RvClients.objects.get(account_id=acc_id)
        res1 = res.clientid
        res2 = RvCampaigns.objects.filter(clientid=res1)
        js = []
        for i in res2:
            campaigns = {'campaignid': i.campaignid, 'campaignname': i.campaignname, 'revenue': i.revenue}
            js.append(campaigns)
        # print(js)
        return JsonResponse(js, safe=False)


# Modify Campaign
@csrf_exempt
def modify_campaign(request):
    if request.method == 'PUT':
        res = request.body.decode('utf-8')
        dict = eval(res)
        update = RvCampaigns.objects.get(campaignid=dict['campaignid'])
        update.campaignname = dict['campaignname']
        update.save()
        return JsonResponse({'response': 'updated'})


# Delete Campaign
def delete_campaign(request):
    if request.method == 'GET':
        cid = request.GET['campaignid']
        delete = RvCampaigns.objects.filter(campaignid=cid)

        # deleting all banners related to campaigns
        for i in delete:
            RvBanners.objects.filter(campaignid=i.campaignid).delete()

        # deleting campaign
        delete.delete()
        return JsonResponse({'response': 'deleted'})


# Add Banner
@csrf_exempt
def add_banner(request):
    if request.method == 'POST':
        res = request.body.decode('utf-8')
        dict = eval(res)
        today = datetime.datetime.now()
        # print(dict)
        insert1 = RvBanners.objects.create(campaignid=dict['campaignid'], contenttype=dict['contenttype'],
                                           pluginversion=0, storagetype='web', filename=dict['filename'],
                                           imageurl='', htmltemplate='', htmlcache='', width=dict['width'],
                                           height=dict['height'], weight=1, seq=0, target='', url=dict['url'], alt='',
                                           statustext='', bannertext='', description=dict['description'], adserver='',
                                           block=0, capping=0, session_capping=0, compiledlimitation='', acl_plugins='',
                                           append='', bannertype=0, alt_filename='', alt_imageurl='',
                                           alt_contenttype='gif', comments='', updated=str(today)[:-7],
                                           acls_updated=str(today)[:-7], keyword='', transparent=0, parameters='N;',
                                           status=0, ext_bannertype='', prepend='', iframe_friendly=0)
        insert1.save()
        shutil.copy2('/home/sudheer/Downloads/' + dict['filename'], '/var/www/html/revive/www/images/' +
                     dict['filename'])
        banner_id = insert1.bannerid
        insert2 = RvAdZoneAssoc.objects.create(zone_id=0, ad_id=banner_id, priority=0.0, link_type=0,
                                               priority_factor=1.0, to_be_delivered=1)
        insert2.save()
        return JsonResponse({'response': 'success', 'bannerid': insert1.bannerid})


# Get banner list by campaign_id
def get_banners_by_campaign(request):
    if request.method == 'GET':
        cid = request.GET['campaignid']
        res = RvBanners.objects.filter(campaignid=cid)
        js = []
        for i in res:
            banners = {'bannerid': i.bannerid, 'bannername': i.description, 'contenttype': i.contenttype, 'url': i.url}
            js.append(banners)
        return JsonResponse(js, safe=False)


# Get Banner
def get_banner(request):
    if request.method == 'GET':
        bid = request.GET['bannerid']
        res = RvBanners.objects.get(bannerid=bid)
        res1 = {'bannerid': res.bannerid, 'bannername': res.description, 'contenttype': res.contenttype, 'url': res.url}
        return JsonResponse(res1)


# Modify Banner
@csrf_exempt
def modify_banner(request):
    if request.method == 'PUT':
        res = request.body.decode('utf-8')
        dict = eval(res)
        update = RvBanners.objects.get(bannerid=dict['bannerid'])
        update.description = dict['bannername']
        update.url = dict['url']
        update.save()
        return JsonResponse({'response': 'updated'})


# Delete Banner
def delete_banner(request):
    if request.method == 'GET':
        bid = request.GET['bannerid']
        delete = RvBanners.objects.get(bannerid=bid)

        # deleting data from rv_ad_zone_assoc_table
        RvAdZoneAssoc.objects.filter(ad_id=bid).delete()

        # deleting targeting data from rv_acls table
        RvAcls.objects.filter(bannerid=bid).delete()

        # deleting banner
        delete.delete()
        return JsonResponse({'response': 'deleted'})


# Set Banner Targeting
@csrf_exempt
def set_banner_targeting(request):
    if request.method == 'POST':
        res = request.body.decode('utf-8')
        dict = eval(res)
        # inserting data into rv_acls table
        insert = RvAcls.objects.create(bannerid=dict['bannerid'], logical=dict['logical'], type=dict['type'],
                                       comparison=dict['comparison'], data=dict['data'], executionorder=
                                       dict['executionorder'])
        insert.save()

        # saving delivery changes by inserting data into rv_banners table

        # inserting data into compiledlimitation column
        cl = 'MAX_check'+dict['type'].split(':')[1]+'_'+dict['type'].split(':')[2]+\
             "('"+dict['data']+"',"+"'"+dict['comparison']+"'"+')'
        insert1 = RvBanners.objects.get(bannerid=dict['bannerid'])
        if insert1.compiledlimitation == 'true':
            insert1.compiledlimitation = cl
        else:
            insert1.compiledlimitation = insert1.compiledlimitation+cl
        insert1.save()

        # inserting data into acl_plugins column
        acl = 'deliveryLimitations'+':'+dict['type'].split(':')[1]+':'+dict['type'].split(':')[2]
        insert1.acl_plugins = insert1.acl_plugins+acl
        insert1.save()
        return JsonResponse({'response': 'success'})


# Get Banner Targeting
def get_banner_targeting(request):
    if request.method == 'GET':
        bid = request.GET['bannerid']
        res = RvAcls.objects.filter(bannerid=bid)
        js = []
        for i in res:
            res1 = {'type': i.type, 'data': i.data, 'executionorder': i.executionorder}
            js.append(res1)
        return JsonResponse(js, safe=False)


# Linking a Campaigns and Banners to Zone
@csrf_exempt
def link_campaign_with_banner_to_zone(request):
    if request.method == 'POST':
        res = request.body.decode('utf-8')
        dict = eval(res)
        cols = RvPlacementZoneAssoc.objects.filter(zone_id=dict['zone_id'], placement_id=dict['placement_id'])

        if len(cols) < 1:
            # linking campaign to zone by inserting campaignid into rv_placement_zone_assoc table
            insert = RvPlacementZoneAssoc.objects.create(zone_id=dict['zone_id'], placement_id=dict['placement_id'])
            insert.save()

        # linking banner with zone by inserting data into rv_ad_zone_assoc table
        insert1 = RvAdZoneAssoc.objects.create(zone_id=dict['zone_id'], ad_id=dict['ad_id'], priority=0.0,
                                               link_type=1, priority_factor=1.0, to_be_delivered=1)
        insert1.save()
        return JsonResponse({'response': 'success'})


# Unlinking a Campaign from Zone
def unlink_campaign_from_zone(request):
    if request.method == 'GET':
        zoneid = request.GET['zone_id']
        campaignid = request.GET['placement_id']

        # unlinking all banners related to campaign
        bid = RvBanners.objects.filter(campaignid=campaignid)
        for i in bid:
            RvAdZoneAssoc.objects.filter(zone_id=zoneid, ad_id=i.bannerid).delete()

        # unlinking campaign
        RvPlacementZoneAssoc.objects.filter(zone_id=zoneid, placement_id=campaignid).delete()
        return JsonResponse({'response': 'unlinked'})


# Unlinking a Banner from Zone
def unlink_banner_from_zone(request):
    if request.method == 'GET':
        zoneid = request.GET['zone_id']
        aid = request.GET['ad_id']
        RvAdZoneAssoc.objects.filter(zone_id=zoneid, ad_id=aid).delete()
        return JsonResponse({'response': 'unlinked'})


# Get Campaign list by Zone
def get_campaign_list_by_zone(request):
    if request.method == 'GET':
        zoneid = request.GET['zone_id']
        res = RvAdZoneAssoc.objects.filter(zone_id=zoneid)
        adIds = []
        for i in res:
            adIds.append(i.ad_id)
        campaignIds = []
        for i in adIds:
            campaignIds.append(RvBanners.objects.get(bannerid=i).campaignid)
        cIds = list(set(campaignIds))
        js = []
        for i in cIds:
            res1 = RvCampaigns.objects.get(campaignid=i)
            campaigns = {'campaignid': res1.campaignid, 'campaignname': res1.campaignname}
            js.append(campaigns)
        return JsonResponse(js, safe=False)


# Get Banner list by Zone
def get_banner_list_by_zone(request):
    if request.method == 'GET':
        zoneid = request.GET['zone_id']
        res = RvAdZoneAssoc.objects.filter(zone_id=zoneid)
        adIds = []
        for i in res:
            adIds.append(i.ad_id)
        js = []
        for i in adIds:
            res1 = RvBanners.objects.get(bannerid=i)
            res2 = {'bannerid': res1.bannerid, 'bannername': res1.description}
            js.append(res2)
        return JsonResponse(js, safe=False)


# Get Statistics of Banner
def get_statistics_of_banner(request):
    try:
        if request.method == 'GET':
            cid = request.GET['campaignid']
            res = RvBanners.objects.filter(campaignid=cid)
            banners = []
            for i in res:
                banners.append(i.bannerid)
            stats = []
            for i in banners:
                impressions = RvDataIntermediateAd.objects.filter(ad_id=i.banners).aggregate(Sum('impressions'))
                clicks = RvDataIntermediateAd.objects.filter(ad_id=i.banners).aggregate(Sum('clicks'))
                statistics = {'bannerid': i.banners, 'impressions': impressions, 'clicks': clicks}
                stats.append(statistics)
            return JsonResponse(stats, safe=False)
    except Exception as e:
        e = str(e)
        return JsonResponse({'response': 'fail', 'error': e})


# Get Zone by Banner
def get_zone_by_banner(request):
    if request.method == 'GET':
        bannerid = request.GET['bannerid']
        res = RvAdZoneAssoc.objects.get(ad_id=bannerid, link_type=1)
        return JsonResponse({'zoneid': res.zone_id})


# Calling REST calls through UI
def test(request):
    return render(request, 'test.html')
