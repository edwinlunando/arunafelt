from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.auth.views import logout
from django.views.generic import TemplateView
from django.contrib import admin
from core import views as core_views


urlpatterns = patterns('',
                       url(r'^$', TemplateView.as_view(template_name='base.html'), name='home'),
                       url(r'^sign-in/$', core_views.SignInPage.as_view(), name='sign-in'),
                       url(r'^sign-out/$', logout, {'next_page': '/'}, name='sign-out'),
                       url(r'^contact/$', core_views.ContactPage.as_view(), name='contact'),
                       url(r'^forgot-password/$', core_views.ForgotPasswordPage.as_view(), name='forgot-password'),
                       url(r'^reset-password/(?P<guid>[-_\w]+)$',
                           core_views.ResetPasswordPage.as_view(), name='reset-password'),

                       # Examples:
                       # url(r'^$', '{{ project_name }}.views.home', name='home'),
                       # url(r'^{{ project_name }}/', include('{{ project_name }}.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       (r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
                       url(r'^admin/', include('admin_honeypot.urls'), namespace='admin_honeypot'),  # The fake admin URI
                       url(r'^backend/', include(admin.site.urls)),  # The real admin URI
                       )

# Uncomment the next line to serve media files in dev.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )
