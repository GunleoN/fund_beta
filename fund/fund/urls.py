from django.conf.urls import patterns, include, url
import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fund.views.home', name='home'),
    # url(r'^fund/', include('fund.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
	(r'^time/$','allocation.views.current_date'),
	(r'^site_media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_PATH}),

	(r'^$', 'allocation.views.home'),#1

	#(r'^login/$','allocation.views.login'),

	(r'^register/$','allocation.views.register'),#2
	(r'^supervisorRegister/$','allocation.views.supervisorRegister'),

	(r'^regist/$','allocation.views.regist'),#3
	(r'^supervisorRegist/$','allocation.views.supervisorRegist'),

	(r'^login/$','allocation.views.login'),
	(r'^supervisorLogin/$','allocation.views.supervisorLogin'),

	#(r'^distribute/$','allocation.views.distribute'),
    (r'^index/$','allocation.views.index'),#4
	(r'^supervisorIndex/$','allocation.views.supervisorIndex'),
	(r'^editPage/(?P<tid_from_url>\d+)$','allocation.views.editPage'),
	(r'^DeletePage/(?P<Delid_from_url>\d+)$','allocation.views.DeletePage'),
	(r'^DeleteSave/(?P<DeleteSaveid_from_url>\d+)$','allocation.views.DeleteSave'),
	(r'^propertyInfo/(?P<tID_from_url>\d+)$','allocation.views.propertyInfo'),
	(r'^supervisorpropertyInfo/(?P<supervisortID_from_url>\d+)$','allocation.views.supervisorpropertyInfo'),

	(r'^AllocatePage/(?P<Allocateid_from_url>\d+)$','allocation.views.AllocatePage'),
	(r'^AllocateResult/(?P<Resultid_from_url>\d+)$','allocation.views.AllocateResult'),

	(r'^AllocationInformation/(?P<AllocationInfoid_from_url>\d+)$','allocation.views.AllocationInformation'),
	(r'^editAllocation/(?P<editAllocationid_from_url>\d+)$','allocation.views.editAllocation'),
	(r'^SaveEditAllocation/(?P<SaveEditAllocationid_from_url>\d+)$','allocation.views.SaveEditAllocation'),
	#(r'^index/$','allocation.views.index'),
	(r'^tradesTable/$','allocation.views.getTradesTable'),
	(r'^test/$','allocation.views.addTrades'),
	(r'^editSave/(?P<saveid_from_url>\d+)$','allocation.views.editSave'),
	(r'^Allocate/(?P<allocateid_from_url>\d+)$','allocation.views.Allocate'),
	(r'^search/$','allocation.views.search'),

	(r'^CheckPage/(?P<checkid_from_url>\d+)$','allocation.views.CheckPage'),
	(r'^supervisorCheckPage/(?P<supervisorcheckid_from_url>\d+)$','allocation.views.supervisorCheckPage'),
	(r'^saveResult/(?P<saveResultid_from_url>\d+)$','allocation.views.saveResult'),
	#(r'^test/$','allocation.views.addTrades'),
	(r'^read/$','allocation.views.read'),

)



