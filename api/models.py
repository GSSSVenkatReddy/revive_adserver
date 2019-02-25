from django.db import models
# Create your models here.


class RvAccountPreferenceAssoc(models.Model):
    account_id = models.IntegerField(primary_key=True)
    preference_id = models.IntegerField()
    value = models.TextField()

    class Meta:
        # managed = False
        db_table = 'rv_account_preference_assoc'
        unique_together = (('account_id', 'preference_id'),)


class RvAccountUserAssoc(models.Model):
    account_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    linked = models.DateTimeField()

    class Meta:
        # managed = False
        db_table = 'rv_account_user_assoc'
        unique_together = (('account_id', 'user_id'),)


class RvAccountUserPermissionAssoc(models.Model):
    account_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    permission_id = models.IntegerField()
    is_allowed = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'rv_account_user_permission_assoc'
        unique_together = (('account_id', 'user_id', 'permission_id'),)


class RvAccounts(models.Model):
    account_id = models.AutoField(primary_key=True)
    account_type = models.CharField(max_length=16)
    account_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'rv_accounts'


class RvAcls(models.Model):
    bannerid = models.IntegerField()
    logical = models.CharField(max_length=3)
    type = models.CharField(max_length=255)
    comparison = models.CharField(max_length=2)
    data = models.TextField()
    executionorder = models.PositiveIntegerField()

    def __str__(self):
        return 'Delivery Type :{0}'.format(self.type)

    class Meta:
        # managed = False
        db_table = 'rv_acls'
        unique_together = (('bannerid', 'executionorder'),)


class RvAclsChannel(models.Model):
    channelid = models.IntegerField()
    logical = models.CharField(max_length=3)
    type = models.CharField(max_length=255)
    comparison = models.CharField(max_length=2)
    data = models.TextField()
    executionorder = models.PositiveIntegerField()

    class Meta:
        # managed = False
        db_table = 'rv_acls_channel'
        unique_together = (('channelid', 'executionorder'),)


class RvAdCategoryAssoc(models.Model):
    ad_category_assoc_id = models.AutoField(primary_key=True)
    category_id = models.PositiveIntegerField()
    ad_id = models.PositiveIntegerField()

    class Meta:
        # managed = False
        db_table = 'rv_ad_category_assoc'


class RvAdZoneAssoc(models.Model):
    ad_zone_assoc_id = models.AutoField(primary_key=True)
    zone_id = models.IntegerField(blank=True, null=True)
    ad_id = models.IntegerField(blank=True, null=True)
    priority = models.FloatField(blank=True, null=True)
    link_type = models.SmallIntegerField()
    priority_factor = models.FloatField(blank=True, null=True)
    to_be_delivered = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'rv_ad_zone_assoc'


class RvAffiliates(models.Model):
    affiliateid = models.AutoField(primary_key=True)
    agencyid = models.IntegerField()
    name = models.CharField(max_length=255)
    mnemonic = models.CharField(max_length=5)
    comments = models.TextField(blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=64)
    website = models.CharField(max_length=255, blank=True, null=True)
    updated = models.DateTimeField()
    oac_country_code = models.CharField(max_length=2)
    oac_language_id = models.IntegerField(blank=True, null=True)
    oac_category_id = models.IntegerField(blank=True, null=True)
    account_id = models.IntegerField(unique=True, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'rv_affiliates'


class RvAffiliatesExtra(models.Model):
    affiliateid = models.IntegerField(primary_key=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    postcode = models.CharField(max_length=64, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=64, blank=True, null=True)
    fax = models.CharField(max_length=64, blank=True, null=True)
    account_contact = models.CharField(max_length=255, blank=True, null=True)
    payee_name = models.CharField(max_length=255, blank=True, null=True)
    tax_id = models.CharField(max_length=64, blank=True, null=True)
    mode_of_payment = models.CharField(max_length=64, blank=True, null=True)
    currency = models.CharField(max_length=64, blank=True, null=True)
    unique_users = models.IntegerField(blank=True, null=True)
    unique_views = models.IntegerField(blank=True, null=True)
    page_rank = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    help_file = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'rv_affiliates_extra'


class RvAgency(models.Model):
    agencyid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=64)
    logout_url = models.CharField(max_length=255, blank=True, null=True)
    active = models.SmallIntegerField(blank=True, null=True)
    updated = models.DateTimeField()
    account_id = models.IntegerField(unique=True, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'rv_agency'


class RvApplicationVariable(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    value = models.TextField()

    class Meta:
        # managed = False
        db_table = 'rv_application_variable'


class RvAudit(models.Model):
    auditid = models.AutoField(primary_key=True)
    actionid = models.IntegerField()
    context = models.CharField(max_length=255)
    contextid = models.IntegerField(blank=True, null=True)
    parentid = models.IntegerField(blank=True, null=True)
    details = models.TextField()
    userid = models.IntegerField()
    username = models.CharField(max_length=64, blank=True, null=True)
    usertype = models.IntegerField()
    updated = models.DateTimeField(blank=True, null=True)
    account_id = models.IntegerField()
    advertiser_account_id = models.IntegerField(blank=True, null=True)
    website_account_id = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'rv_audit'


class RvBannerVastElement(models.Model):
    banner_vast_element_id = models.IntegerField()
    banner_id = models.IntegerField()
    vast_element_type = models.CharField(max_length=16)
    vast_video_id = models.CharField(max_length=100, blank=True, null=True)
    vast_video_duration = models.IntegerField(blank=True, null=True)
    vast_video_delivery = models.CharField(max_length=20, blank=True, null=True)
    vast_video_type = models.CharField(max_length=20, blank=True, null=True)
    vast_video_bitrate = models.CharField(max_length=20, blank=True, null=True)
    vast_video_height = models.IntegerField(blank=True, null=True)
    vast_video_width = models.IntegerField(blank=True, null=True)
    vast_video_outgoing_filename = models.TextField(blank=True, null=True)
    vast_companion_banner_id = models.IntegerField(blank=True, null=True)
    vast_overlay_height = models.IntegerField(blank=True, null=True)
    vast_overlay_width = models.IntegerField(blank=True, null=True)
    vast_video_clickthrough_url = models.TextField(blank=True, null=True)
    vast_overlay_action = models.CharField(max_length=20, blank=True, null=True)
    vast_overlay_format = models.CharField(max_length=20, blank=True, null=True)
    vast_overlay_text_title = models.TextField(blank=True, null=True)
    vast_overlay_text_description = models.TextField(blank=True, null=True)
    vast_overlay_text_call = models.TextField(blank=True, null=True)
    vast_creative_type = models.CharField(max_length=20, blank=True, null=True)
    vast_thirdparty_impression = models.TextField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'rv_banner_vast_element'


class RvBanners(models.Model):
    bannerid = models.AutoField(primary_key=True)
    campaignid = models.IntegerField()
    contenttype = models.CharField(max_length=4)
    pluginversion = models.IntegerField()
    storagetype = models.CharField(max_length=7)
    filename = models.CharField(max_length=255)
    imageurl = models.CharField(max_length=255)
    htmltemplate = models.TextField()
    htmlcache = models.TextField()
    width = models.SmallIntegerField()
    height = models.SmallIntegerField()
    weight = models.IntegerField()
    seq = models.IntegerField()
    target = models.CharField(max_length=16)
    url = models.TextField()
    alt = models.CharField(max_length=255)
    statustext = models.CharField(max_length=255)
    bannertext = models.TextField()
    description = models.CharField(max_length=255)
    adserver = models.CharField(max_length=255)
    block = models.IntegerField()
    capping = models.IntegerField()
    session_capping = models.IntegerField()
    compiledlimitation = models.TextField()
    acl_plugins = models.TextField(blank=True, null=True)
    append = models.TextField()
    bannertype = models.IntegerField()
    alt_filename = models.CharField(max_length=255)
    alt_imageurl = models.CharField(max_length=255)
    alt_contenttype = models.CharField(max_length=4, null=True)
    comments = models.TextField(blank=True, null=True)
    updated = models.DateTimeField()
    acls_updated = models.DateTimeField(null=True)
    keyword = models.CharField(max_length=255)
    transparent = models.IntegerField()
    parameters = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    ext_bannertype = models.CharField(max_length=255, blank=True, null=True)
    prepend = models.TextField()
    iframe_friendly = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'rv_banners'


class RvCampaigns(models.Model):
    campaignid = models.AutoField(primary_key=True)
    campaignname = models.CharField(max_length=255)
    clientid = models.IntegerField()
    views = models.IntegerField(blank=True, null=True)
    clicks = models.IntegerField(blank=True, null=True)
    conversions = models.IntegerField(blank=True, null=True)
    priority = models.IntegerField()
    weight = models.IntegerField()
    target_impression = models.IntegerField()
    target_click = models.IntegerField()
    target_conversion = models.IntegerField()
    anonymous = models.CharField(max_length=1)
    companion = models.SmallIntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    revenue = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    revenue_type = models.SmallIntegerField(blank=True, null=True)
    updated = models.DateTimeField()
    block = models.IntegerField()
    capping = models.IntegerField()
    session_capping = models.IntegerField()
    status = models.IntegerField()
    hosted_views = models.IntegerField()
    hosted_clicks = models.IntegerField()
    viewwindow = models.IntegerField()
    clickwindow = models.IntegerField()
    ecpm = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    min_impressions = models.IntegerField()
    ecpm_enabled = models.IntegerField()
    activate_time = models.DateTimeField(blank=True, null=True)
    expire_time = models.DateTimeField(blank=True, null=True)
    type = models.IntegerField()
    show_capped_no_cookie = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'rv_campaigns'


class RvCampaignsTrackers(models.Model):
    campaign_trackerid = models.AutoField(primary_key=True)
    campaignid = models.IntegerField()
    trackerid = models.IntegerField()
    status = models.PositiveSmallIntegerField()

    class Meta:
        # managed = False
        db_table = 'rv_campaigns_trackers'


class RvCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'rv_category'


class RvChannel(models.Model):
    channelid = models.AutoField(primary_key=True)
    agencyid = models.IntegerField()
    affiliateid = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    compiledlimitation = models.TextField()
    acl_plugins = models.TextField(blank=True, null=True)
    active = models.SmallIntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    updated = models.DateTimeField()
    acls_updated = models.DateTimeField()

    class Meta:
        # managed = False
        db_table = 'rv_channel'


class RvClients(models.Model):
    clientid = models.AutoField(primary_key=True)
    agencyid = models.IntegerField()
    clientname = models.CharField(max_length=255)
    contact = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=64)
    report = models.CharField(max_length=1)
    reportinterval = models.IntegerField()
    reportlastdate = models.DateField()
    reportdeactivate = models.CharField(max_length=1)
    comments = models.TextField(blank=True, null=True)
    updated = models.DateTimeField()
    account_id = models.IntegerField(unique=True, blank=True, null=True)
    advertiser_limitation = models.IntegerField()
    type = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'rv_clients'


class RvDataBktA(models.Model):
    server_conv_id = models.BigAutoField(primary_key=True)
    server_ip = models.CharField(max_length=16)
    tracker_id = models.IntegerField()
    date_time = models.DateTimeField()
    action_date_time = models.DateTimeField()
    creative_id = models.IntegerField()
    zone_id = models.IntegerField()
    ip_address = models.CharField(max_length=16)
    action = models.IntegerField(blank=True, null=True)
    window = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'rv_data_bkt_a'
        unique_together = (('server_conv_id', 'server_ip'),)


class RvDataBktAVar(models.Model):
    server_conv_id = models.BigAutoField(primary_key=True)
    server_ip = models.CharField(max_length=16)
    tracker_variable_id = models.IntegerField()
    value = models.TextField(blank=True, null=True)
    date_time = models.DateTimeField()

    class Meta:
        # managed = False
        db_table = 'rv_data_bkt_a_var'
        unique_together = (('server_conv_id', 'server_ip', 'tracker_variable_id'),)


class RvDataBktC(models.Model):
    interval_start = models.DateTimeField(primary_key=True)
    creative_id = models.IntegerField()
    zone_id = models.IntegerField()
    count = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'rv_data_bkt_c'
        unique_together = (('interval_start', 'creative_id', 'zone_id'),)


class RvDataBktM(models.Model):
    interval_start = models.DateTimeField(primary_key=True)
    creative_id = models.IntegerField()
    zone_id = models.IntegerField()
    count = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'rv_data_bkt_m'
        unique_together = (('interval_start', 'creative_id', 'zone_id'),)


class RvDataBktR(models.Model):
    interval_start = models.DateTimeField(primary_key=True)
    creative_id = models.IntegerField()
    zone_id = models.IntegerField()
    count = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'rv_data_bkt_r'
        unique_together = (('interval_start', 'creative_id', 'zone_id'),)


class RvDataBktVastE(models.Model):
    interval_start = models.DateTimeField(primary_key=True)
    creative_id = models.IntegerField()
    zone_id = models.IntegerField()
    vast_event_id = models.IntegerField()
    count = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'rv_data_bkt_vast_e'
        unique_together = (('interval_start', 'creative_id', 'zone_id', 'vast_event_id'),)


class RvDataIntermediateAd(models.Model):
    data_intermediate_ad_id = models.BigAutoField(primary_key=True)
    date_time = models.DateTimeField()
    operation_interval = models.PositiveIntegerField()
    operation_interval_id = models.PositiveIntegerField()
    interval_start = models.DateTimeField()
    interval_end = models.DateTimeField()
    ad_id = models.PositiveIntegerField()
    creative_id = models.PositiveIntegerField()
    zone_id = models.PositiveIntegerField()
    requests = models.PositiveIntegerField()
    impressions = models.PositiveIntegerField()
    clicks = models.PositiveIntegerField()
    conversions = models.PositiveIntegerField()
    total_basket_value = models.DecimalField(max_digits=10, decimal_places=4)
    total_num_items = models.IntegerField()
    updated = models.DateTimeField()

    class Meta:
        # managed = False
        db_table = 'rv_data_intermediate_ad'


class RvDataIntermediateAdConnection(models.Model):
    data_intermediate_ad_connection_id = models.BigAutoField(primary_key=True)
    server_raw_ip = models.CharField(max_length=16)
    server_raw_tracker_impression_id = models.BigIntegerField()
    viewer_id = models.CharField(max_length=32, blank=True, null=True)
    viewer_session_id = models.CharField(max_length=32, blank=True, null=True)
    tracker_date_time = models.DateTimeField()
    connection_date_time = models.DateTimeField(blank=True, null=True)
    tracker_id = models.PositiveIntegerField()
    ad_id = models.PositiveIntegerField()
    creative_id = models.PositiveIntegerField()
    zone_id = models.PositiveIntegerField()
    tracker_channel = models.CharField(max_length=255, blank=True, null=True)
    connection_channel = models.CharField(max_length=255, blank=True, null=True)
    tracker_channel_ids = models.CharField(max_length=64, blank=True, null=True)
    connection_channel_ids = models.CharField(max_length=64, blank=True, null=True)
    tracker_language = models.CharField(max_length=13, blank=True, null=True)
    connection_language = models.CharField(max_length=13, blank=True, null=True)
    tracker_ip_address = models.CharField(max_length=16, blank=True, null=True)
    connection_ip_address = models.CharField(max_length=16, blank=True, null=True)
    tracker_host_name = models.CharField(max_length=255, blank=True, null=True)
    connection_host_name = models.CharField(max_length=255, blank=True, null=True)
    tracker_country = models.CharField(max_length=2, blank=True, null=True)
    connection_country = models.CharField(max_length=2, blank=True, null=True)
    tracker_https = models.PositiveIntegerField(blank=True, null=True)
    connection_https = models.PositiveIntegerField(blank=True, null=True)
    tracker_domain = models.CharField(max_length=255, blank=True, null=True)
    connection_domain = models.CharField(max_length=255, blank=True, null=True)
    tracker_page = models.CharField(max_length=255, blank=True, null=True)
    connection_page = models.CharField(max_length=255, blank=True, null=True)
    tracker_query = models.CharField(max_length=255, blank=True, null=True)
    connection_query = models.CharField(max_length=255, blank=True, null=True)
    tracker_referer = models.CharField(max_length=255, blank=True, null=True)
    connection_referer = models.CharField(max_length=255, blank=True, null=True)
    tracker_search_term = models.CharField(max_length=255, blank=True, null=True)
    connection_search_term = models.CharField(max_length=255, blank=True, null=True)
    tracker_user_agent = models.CharField(max_length=255, blank=True, null=True)
    connection_user_agent = models.CharField(max_length=255, blank=True, null=True)
    tracker_os = models.CharField(max_length=32, blank=True, null=True)
    connection_os = models.CharField(max_length=32, blank=True, null=True)
    tracker_browser = models.CharField(max_length=32, blank=True, null=True)
    connection_browser = models.CharField(max_length=32, blank=True, null=True)
    connection_action = models.PositiveIntegerField(blank=True, null=True)
    connection_window = models.PositiveIntegerField(blank=True, null=True)
    connection_status = models.PositiveIntegerField()
    inside_window = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    updated = models.DateTimeField()

    class Meta:
        # managed = False
        db_table = 'rv_data_intermediate_ad_connection'


class RvDataIntermediateAdVariableValue(models.Model):
    data_intermediate_ad_variable_value_id = models.BigAutoField(primary_key=True)
    data_intermediate_ad_connection_id = models.BigIntegerField()
    tracker_variable_id = models.IntegerField()
    value = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'rv_data_intermediate_ad_variable_value'


class RvDataRawAdClick(models.Model):
    viewer_id = models.CharField(max_length=32, blank=True, null=True)
    viewer_session_id = models.CharField(max_length=32, blank=True, null=True)
    date_time = models.DateTimeField()
    ad_id = models.PositiveIntegerField()
    creative_id = models.PositiveIntegerField()
    zone_id = models.PositiveIntegerField()
    channel = models.CharField(max_length=255, blank=True, null=True)
    channel_ids = models.CharField(max_length=64, blank=True, null=True)
    language = models.CharField(max_length=32, blank=True, null=True)
    ip_address = models.CharField(max_length=16, blank=True, null=True)
    host_name = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=2, blank=True, null=True)
    https = models.IntegerField(blank=True, null=True)
    domain = models.CharField(max_length=255, blank=True, null=True)
    page = models.CharField(max_length=255, blank=True, null=True)
    query = models.CharField(max_length=255, blank=True, null=True)
    referer = models.CharField(max_length=255, blank=True, null=True)
    search_term = models.CharField(max_length=255, blank=True, null=True)
    user_agent = models.CharField(max_length=255, blank=True, null=True)
    os = models.CharField(max_length=32, blank=True, null=True)
    browser = models.CharField(max_length=32, blank=True, null=True)
    max_https = models.IntegerField(blank=True, null=True)
    geo_region = models.CharField(max_length=50, blank=True, null=True)
    geo_city = models.CharField(max_length=50, blank=True, null=True)
    geo_postal_code = models.CharField(max_length=10, blank=True, null=True)
    geo_latitude = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    geo_longitude = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    geo_dma_code = models.CharField(max_length=50, blank=True, null=True)
    geo_area_code = models.CharField(max_length=50, blank=True, null=True)
    geo_organisation = models.CharField(max_length=50, blank=True, null=True)
    geo_netspeed = models.CharField(max_length=20, blank=True, null=True)
    geo_continent = models.CharField(max_length=13, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'rv_data_raw_ad_click'


class RvDataRawAdImpression(models.Model):
    viewer_id = models.CharField(max_length=32, blank=True, null=True)
    viewer_session_id = models.CharField(max_length=32, blank=True, null=True)
    date_time = models.DateTimeField()
    ad_id = models.PositiveIntegerField()
    creative_id = models.PositiveIntegerField()
    zone_id = models.PositiveIntegerField()
    channel = models.CharField(max_length=255, blank=True, null=True)
    channel_ids = models.CharField(max_length=64, blank=True, null=True)
    language = models.CharField(max_length=32, blank=True, null=True)
    ip_address = models.CharField(max_length=16, blank=True, null=True)
    host_name = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=2, blank=True, null=True)
    https = models.IntegerField(blank=True, null=True)
    domain = models.CharField(max_length=255, blank=True, null=True)
    page = models.CharField(max_length=255, blank=True, null=True)
    query = models.CharField(max_length=255, blank=True, null=True)
    referer = models.CharField(max_length=255, blank=True, null=True)
    search_term = models.CharField(max_length=255, blank=True, null=True)
    user_agent = models.CharField(max_length=255, blank=True, null=True)
    os = models.CharField(max_length=32, blank=True, null=True)
    browser = models.CharField(max_length=32, blank=True, null=True)
    max_https = models.IntegerField(blank=True, null=True)
    geo_region = models.CharField(max_length=50, blank=True, null=True)
    geo_city = models.CharField(max_length=50, blank=True, null=True)
    geo_postal_code = models.CharField(max_length=10, blank=True, null=True)
    geo_latitude = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    geo_longitude = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    geo_dma_code = models.CharField(max_length=50, blank=True, null=True)
    geo_area_code = models.CharField(max_length=50, blank=True, null=True)
    geo_organisation = models.CharField(max_length=50, blank=True, null=True)
    geo_netspeed = models.CharField(max_length=20, blank=True, null=True)
    geo_continent = models.CharField(max_length=13, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'rv_data_raw_ad_impression'


class RvDataRawAdRequest(models.Model):
    viewer_id = models.CharField(max_length=32, blank=True, null=True)
    viewer_session_id = models.CharField(max_length=32, blank=True, null=True)
    date_time = models.DateTimeField()
    ad_id = models.PositiveIntegerField()
    creative_id = models.PositiveIntegerField()
    zone_id = models.PositiveIntegerField()
    channel = models.CharField(max_length=255, blank=True, null=True)
    channel_ids = models.CharField(max_length=64, blank=True, null=True)
    language = models.CharField(max_length=32, blank=True, null=True)
    ip_address = models.CharField(max_length=16, blank=True, null=True)
    host_name = models.CharField(max_length=255, blank=True, null=True)
    https = models.IntegerField(blank=True, null=True)
    domain = models.CharField(max_length=255, blank=True, null=True)
    page = models.CharField(max_length=255, blank=True, null=True)
    query = models.CharField(max_length=255, blank=True, null=True)
    referer = models.CharField(max_length=255, blank=True, null=True)
    search_term = models.CharField(max_length=255, blank=True, null=True)
    user_agent = models.CharField(max_length=255, blank=True, null=True)
    os = models.CharField(max_length=32, blank=True, null=True)
    browser = models.CharField(max_length=32, blank=True, null=True)
    max_https = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'rv_data_raw_ad_request'


class RvDataRawTrackerImpression(models.Model):
    server_raw_tracker_impression_id = models.BigAutoField(primary_key=True)
    server_raw_ip = models.CharField(max_length=16)
    viewer_id = models.CharField(max_length=32)
    viewer_session_id = models.CharField(max_length=32, blank=True, null=True)
    date_time = models.DateTimeField()
    tracker_id = models.PositiveIntegerField()
    channel = models.CharField(max_length=255, blank=True, null=True)
    channel_ids = models.CharField(max_length=64, blank=True, null=True)
    language = models.CharField(max_length=32, blank=True, null=True)
    ip_address = models.CharField(max_length=16, blank=True, null=True)
    host_name = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=2, blank=True, null=True)
    https = models.PositiveIntegerField(blank=True, null=True)
    domain = models.CharField(max_length=255, blank=True, null=True)
    page = models.CharField(max_length=255, blank=True, null=True)
    query = models.CharField(max_length=255, blank=True, null=True)
    referer = models.CharField(max_length=255, blank=True, null=True)
    search_term = models.CharField(max_length=255, blank=True, null=True)
    user_agent = models.CharField(max_length=255, blank=True, null=True)
    os = models.CharField(max_length=32, blank=True, null=True)
    browser = models.CharField(max_length=32, blank=True, null=True)
    max_https = models.PositiveIntegerField(blank=True, null=True)
    geo_region = models.CharField(max_length=50, blank=True, null=True)
    geo_city = models.CharField(max_length=50, blank=True, null=True)
    geo_postal_code = models.CharField(max_length=10, blank=True, null=True)
    geo_latitude = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    geo_longitude = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    geo_dma_code = models.CharField(max_length=50, blank=True, null=True)
    geo_area_code = models.CharField(max_length=50, blank=True, null=True)
    geo_organisation = models.CharField(max_length=50, blank=True, null=True)
    geo_netspeed = models.CharField(max_length=20, blank=True, null=True)
    geo_continent = models.CharField(max_length=13, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'rv_data_raw_tracker_impression'
        unique_together = (('server_raw_tracker_impression_id', 'server_raw_ip'),)


class RvDataRawTrackerVariableValue(models.Model):
    server_raw_tracker_impression_id = models.BigIntegerField(primary_key=True)
    server_raw_ip = models.CharField(max_length=16)
    tracker_variable_id = models.IntegerField()
    date_time = models.DateTimeField(blank=True, null=True)
    value = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'rv_data_raw_tracker_variable_value'
        unique_together = (('server_raw_tracker_impression_id', 'server_raw_ip', 'tracker_variable_id'),)


class RvDataSummaryAdHourly(models.Model):
    data_summary_ad_hourly_id = models.BigAutoField(primary_key=True)
    date_time = models.DateTimeField()
    ad_id = models.PositiveIntegerField()
    creative_id = models.PositiveIntegerField()
    zone_id = models.PositiveIntegerField()
    requests = models.PositiveIntegerField()
    impressions = models.PositiveIntegerField()
    clicks = models.PositiveIntegerField()
    conversions = models.PositiveIntegerField()
    total_basket_value = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    total_num_items = models.IntegerField(blank=True, null=True)
    total_revenue = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    total_techcost = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    updated = models.DateTimeField()

    class Meta:
        # managed = False
        db_table = 'rv_data_summary_ad_hourly'


class RvDataSummaryAdZoneAssoc(models.Model):
    data_summary_ad_zone_assoc_id = models.BigAutoField(primary_key=True)
    operation_interval = models.PositiveIntegerField()
    operation_interval_id = models.PositiveIntegerField()
    interval_start = models.DateTimeField()
    interval_end = models.DateTimeField()
    ad_id = models.PositiveIntegerField()
    zone_id = models.PositiveIntegerField()
    required_impressions = models.PositiveIntegerField()
    requested_impressions = models.PositiveIntegerField()
    priority = models.FloatField()
    priority_factor = models.FloatField(blank=True, null=True)
    priority_factor_limited = models.SmallIntegerField()
    past_zone_traffic_fraction = models.FloatField(blank=True, null=True)
    created = models.DateTimeField()
    created_by = models.PositiveIntegerField()
    expired = models.DateTimeField(blank=True, null=True)
    expired_by = models.PositiveIntegerField(blank=True, null=True)
    to_be_delivered = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'rv_data_summary_ad_zone_assoc'


class RvDataSummaryChannelDaily(models.Model):
    data_summary_channel_daily_id = models.BigAutoField(primary_key=True)
    day = models.DateField()
    channel_id = models.PositiveIntegerField()
    zone_id = models.PositiveIntegerField()
    forecast_impressions = models.PositiveIntegerField()
    actual_impressions = models.PositiveIntegerField()

    class Meta:
        # managed = False
        db_table = 'rv_data_summary_channel_daily'


class RvDataSummaryZoneImpressionHistory(models.Model):
    data_summary_zone_impression_history_id = models.BigAutoField(primary_key=True)
    operation_interval = models.PositiveIntegerField()
    operation_interval_id = models.PositiveIntegerField()
    interval_start = models.DateTimeField()
    interval_end = models.DateTimeField()
    zone_id = models.PositiveIntegerField()
    forecast_impressions = models.PositiveIntegerField(blank=True, null=True)
    actual_impressions = models.PositiveIntegerField(blank=True, null=True)
    est = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'rv_data_summary_zone_impression_history'


class RvDatabaseAction(models.Model):
    database_action_id = models.AutoField(primary_key=True)
    upgrade_action_id = models.PositiveIntegerField(blank=True, null=True)
    schema_name = models.CharField(max_length=64, blank=True, null=True)
    version = models.IntegerField()
    timing = models.IntegerField()
    action = models.IntegerField()
    info1 = models.CharField(max_length=255, blank=True, null=True)
    info2 = models.CharField(max_length=255, blank=True, null=True)
    tablename = models.CharField(max_length=64, blank=True, null=True)
    tablename_backup = models.CharField(max_length=64, blank=True, null=True)
    table_backup_schema = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'rv_database_action'


class RvImages(models.Model):
    filename = models.CharField(primary_key=True, max_length=128)
    contents = models.TextField()
    t_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'rv_images'


class RvLogMaintenanceForecasting(models.Model):
    log_maintenance_forecasting_id = models.AutoField(primary_key=True)
    start_run = models.DateTimeField()
    end_run = models.DateTimeField()
    operation_interval = models.IntegerField()
    duration = models.IntegerField()
    updated_to = models.DateTimeField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'rv_log_maintenance_forecasting'


class RvLogMaintenancePriority(models.Model):
    log_maintenance_priority_id = models.AutoField(primary_key=True)
    start_run = models.DateTimeField()
    end_run = models.DateTimeField()
    operation_interval = models.IntegerField()
    duration = models.IntegerField()
    run_type = models.PositiveIntegerField()
    updated_to = models.DateTimeField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'rv_log_maintenance_priority'


class RvLogMaintenanceStatistics(models.Model):
    log_maintenance_statistics_id = models.AutoField(primary_key=True)
    start_run = models.DateTimeField()
    end_run = models.DateTimeField()
    duration = models.IntegerField()
    adserver_run_type = models.IntegerField(blank=True, null=True)
    search_run_type = models.IntegerField(blank=True, null=True)
    tracker_run_type = models.IntegerField(blank=True, null=True)
    updated_to = models.DateTimeField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'rv_log_maintenance_statistics'


class RvPasswordRecovery(models.Model):
    user_type = models.CharField(primary_key=True, max_length=64)
    user_id = models.IntegerField()
    recovery_id = models.CharField(unique=True, max_length=64)
    updated = models.DateTimeField()

    class Meta:
        # managed = False
        db_table = 'rv_password_recovery'
        unique_together = (('user_type', 'user_id'),)


class RvPlacementZoneAssoc(models.Model):
    placement_zone_assoc_id = models.AutoField(primary_key=True)
    zone_id = models.IntegerField(blank=True, null=True)
    placement_id = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'rv_placement_zone_assoc'


class RvPreferences(models.Model):
    preference_id = models.AutoField(primary_key=True)
    preference_name = models.CharField(unique=True, max_length=64)
    account_type = models.CharField(max_length=16)

    class Meta:
        # managed = False
        db_table = 'rv_preferences'


class RvSession(models.Model):
    sessionid = models.CharField(primary_key=True, max_length=32)
    sessiondata = models.TextField()
    lastused = models.DateTimeField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'rv_session'


class RvStatsVast(models.Model):
    interval_start = models.DateTimeField()
    creative_id = models.IntegerField()
    zone_id = models.IntegerField()
    vast_event_id = models.IntegerField()
    count = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'rv_stats_vast'


class RvTargetstats(models.Model):
    day = models.DateField()
    campaignid = models.IntegerField()
    target = models.IntegerField()
    views = models.IntegerField()
    modified = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'rv_targetstats'


class RvTrackerAppend(models.Model):
    tracker_append_id = models.AutoField(primary_key=True)
    tracker_id = models.IntegerField()
    rank = models.IntegerField()
    tagcode = models.TextField()
    paused = models.CharField(max_length=1)
    autotrack = models.CharField(max_length=1)

    class Meta:
        # managed = False
        db_table = 'rv_tracker_append'


class RvTrackers(models.Model):
    trackerid = models.AutoField(primary_key=True)
    trackername = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    clientid = models.IntegerField()
    viewwindow = models.IntegerField()
    clickwindow = models.IntegerField()
    blockwindow = models.IntegerField()
    status = models.PositiveSmallIntegerField()
    type = models.PositiveSmallIntegerField()
    linkcampaigns = models.CharField(max_length=1)
    variablemethod = models.CharField(max_length=7)
    appendcode = models.TextField()
    updated = models.DateTimeField()

    class Meta:
        # managed = False
        db_table = 'rv_trackers'


class RvUpgradeAction(models.Model):
    upgrade_action_id = models.AutoField(primary_key=True)
    upgrade_name = models.CharField(max_length=128, blank=True, null=True)
    version_to = models.CharField(max_length=64)
    version_from = models.CharField(max_length=64, blank=True, null=True)
    action = models.IntegerField()
    description = models.CharField(max_length=255, blank=True, null=True)
    logfile = models.CharField(max_length=128, blank=True, null=True)
    confbackup = models.CharField(max_length=128, blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'rv_upgrade_action'


class RvUserlog(models.Model):
    userlogid = models.AutoField(primary_key=True)
    timestamp = models.IntegerField()
    usertype = models.IntegerField()
    userid = models.IntegerField()
    action = models.IntegerField()
    object = models.IntegerField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'rv_userlog'


class RvUsers(models.Model):
    user_id = models.AutoField(primary_key=True)
    contact_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=64)
    username = models.CharField(unique=True, max_length=64, blank=True, null=True)
    password = models.CharField(max_length=64, blank=True, null=True)
    language = models.CharField(max_length=5, blank=True, null=True)
    default_account_id = models.IntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    active = models.IntegerField()
    sso_user_id = models.IntegerField(unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    date_last_login = models.DateTimeField(blank=True, null=True)
    email_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'rv_users'


class RvVariablePublisher(models.Model):
    variable_id = models.IntegerField(primary_key=True)
    publisher_id = models.IntegerField()
    visible = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'rv_variable_publisher'
        unique_together = (('variable_id', 'publisher_id'),)


class RvVariables(models.Model):
    variableid = models.AutoField(primary_key=True)
    trackerid = models.IntegerField()
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250, blank=True, null=True)
    datatype = models.CharField(max_length=7)
    purpose = models.CharField(max_length=12, blank=True, null=True)
    reject_if_empty = models.PositiveSmallIntegerField()
    is_unique = models.IntegerField()
    unique_window = models.IntegerField()
    variablecode = models.CharField(max_length=255)
    hidden = models.CharField(max_length=1)
    updated = models.DateTimeField()

    class Meta:
        # managed = False
        db_table = 'rv_variables'


class RvZones(models.Model):
    zoneid = models.AutoField(primary_key=True)
    affiliateid = models.IntegerField(blank=True, null=True)
    zonename = models.CharField(max_length=245)
    description = models.CharField(max_length=255)
    delivery = models.SmallIntegerField()
    zonetype = models.SmallIntegerField()
    category = models.TextField()
    width = models.SmallIntegerField()
    height = models.SmallIntegerField()
    ad_selection = models.TextField()
    chain = models.TextField()
    prepend = models.TextField()
    append = models.TextField()
    appendtype = models.IntegerField()
    forceappend = models.CharField(max_length=1, blank=True, null=True)
    inventory_forecast_type = models.SmallIntegerField()
    comments = models.TextField(blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    cost_type = models.SmallIntegerField(blank=True, null=True)
    cost_variable_id = models.CharField(max_length=255, blank=True, null=True)
    technology_cost = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    technology_cost_type = models.SmallIntegerField(blank=True, null=True)
    updated = models.DateTimeField()
    block = models.IntegerField()
    capping = models.IntegerField()
    session_capping = models.IntegerField()
    what = models.TextField()
    rate = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    pricing = models.CharField(max_length=50)
    oac_category_id = models.IntegerField(blank=True, null=True)
    ext_adselection = models.CharField(max_length=255, blank=True, null=True)
    show_capped_no_cookie = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'rv_zones'
