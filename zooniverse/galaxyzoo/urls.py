from django.conf.urls import url

from . import views

app_name = 'galaxyzoo'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.create_user, name='create_user'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<pk>[0-9]+)/round/$', views.RoundView.as_view(), name='round'),
    url(r'^(?P<pk>[0-9]+)/parent/$', views.ParentView.as_view(), name='parent'),
    url(r'^(?P<pk>[0-9]+)/odd/$', views.OddView.as_view(), name='odd'),
    url(r'^(?P<pk>[0-9]+)/tidal/$', views.TidalView.as_view(), name='tidal'),
    url(r'^(?P<pk>[0-9]+)/prominence/$', views.ProminenceView.as_view(), name='prominence'),
    url(r'^(?P<pk>[0-9]+)/sa_num/$', views.Sa_numView.as_view(), name='sa_num'),
    url(r'^(?P<pk>[0-9]+)/sa/$', views.SaView.as_view(), name='sa'),
    url(r'^(?P<pk>[0-9]+)/pattern/$', views.PatternView.as_view(), name='pattern'),
    url(r'^(?P<pk>[0-9]+)/bar/$', views.BarView.as_view(), name='bar'),
    url(r'^(?P<pk>[0-9]+)/bulge/$', views.BulgeView.as_view(), name='bulge'),
    url(r'^(?P<pk>[0-9]+)/edge/$', views.EdgeView.as_view(), name='edge'),
    url(r'^(?P<question_id>[0-9]+)/restart/$', views.restart, name='restart'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<question_id>[0-9]+)/to_round/$', views.to_round, name='to_round'),
    url(r'^(?P<question_id>[0-9]+)/to_edge/$', views.to_edge, name='to_edge'),
	url(r'^(?P<question_id>[0-9]+)/to_bulge/$', views.to_bulge, name='to_bulge'),
	url(r'^(?P<question_id>[0-9]+)/to_bar/$', views.to_bar, name='to_bar'),
	url(r'^(?P<question_id>[0-9]+)/to_pattern/$', views.to_pattern, name='to_pattern'),
	url(r'^(?P<question_id>[0-9]+)/to_sa/$', views.to_sa, name='to_sa'),
	url(r'^(?P<question_id>[0-9]+)/to_sa_num/$', views.to_sa_num, name='to_sa_num'),
	url(r'^(?P<question_id>[0-9]+)/to_prominence/$', views.to_prominence, name='to_prominence'),
	url(r'^(?P<question_id>[0-9]+)/to_tidal/$', views.to_tidal, name='to_tidal'),
	url(r'^(?P<question_id>[0-9]+)/to_odd/$', views.to_odd, name='to_odd')
]
