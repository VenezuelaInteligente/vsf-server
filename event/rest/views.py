from django.db.models import Q

from django.shortcuts import render
from rest_framework.authentication import BasicAuthentication
from vsf.vsf_authentication import VSFTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serializers import (
    UrlSerializer,
    SiteSerializer,
    EventSerializer,
    EventGroupSerializer,
    EventGroupFilter,
    BlockedSiteSerializer,
    ISPSerializer,
    CategorySerializer
)
from django_filters.rest_framework import DjangoFilterBackend

from event.models import Event, Target, Site, ISP, SiteCategory
from datetime import datetime


class BlockedDomains(generics.ListAPIView):
    """
    Este servicio entrega una lista de
    dominios(urls) que pertenesen a eventos de
    tipo bloqueo, o sea, dominios bloqueados.
    Nota. Todos los dominios bloqueados deberian
    pertenecer a un sitio.
    Ej. http://www.midominiobloqueado.com
    """
    authentication_classes = (VSFTokenAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Event.objects.filter(
        Q(type='bloqueo por DPI') |
        Q(type='bloqueo por DNS') |
        Q(type='bloqueo por IP')
    )
    serializer_class = UrlSerializer

    def get_queryset(self):
        url_list = self.queryset.values('target')
        queryset = Target.objects.filter(id__in=url_list)
        return queryset


class BlockedSites(BlockedDomains):
    """
    Este servicio entrega una lista de
    sitios que pertenesen a eventos de
    tipo bloqueo.
    O sea, sitios bloqueados.
    Ej. Mi Sitio Bloqueado
    """

    serializer_class = BlockedSiteSerializer

    def get_queryset(self):
        queryset = super(BlockedSites, self).get_queryset()

        site_list = queryset.values('site')
        queryset = Site.objects.filter(id__in=site_list)
        return queryset


class EventList(generics.ListAPIView):
    authentication_classes = (VSFTokenAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Event.objects.filter(draft=False)
    serializer_class = EventSerializer


class ListEventGroupView(generics.ListAPIView):
    """ListEventGroupView: ListAPIView
    for displaying a list of events filtered by
    start date, end date and isp"""
    authentication_classes = (VSFTokenAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = Event.objects.filter(draft=False)
    serializer_class = EventGroupSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = EventGroupFilter


class ListSiteView(generics.ListAPIView):
    """ListSiteView: ListAPIView
    for displaying a list of all sites"""
    authentication_classes = (VSFTokenAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = Site.objects.all()
    serializer_class = SiteSerializer


class ListISPView(generics.ListAPIView):
    """ListSiteView: ListAPIView
    for displaying a list of all isps"""
    authentication_classes = (VSFTokenAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = ISP.objects.all()
    serializer_class = ISPSerializer


class ListCategoriesView(generics.ListAPIView):
    """ListSiteView: ListAPIView
    for displaying a list of all categories"""
    authentication_classes = (VSFTokenAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = SiteCategory.objects.all()
    serializer_class = CategorySerializer


class ListTargetsView(generics.ListAPIView):
    """ListSiteView: ListAPIView
    for displaying a list of all categories"""
    authentication_classes = (VSFTokenAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = Target.objects.all()
    serializer_class = UrlSerializer
