from django.db.models.expressions import RawSQL
from django.conf import settings
from django.core.paginator import Paginator
from django.utils.dateparse import parse_datetime
from django.utils.timezone import make_aware
from measurement.models import Metric, Flag
from plugins.tcp.models import TCP


def web_connectivity_to_tcp():
    # Get all metrics with test_name web_connectivity
    # but only values id, measurement, test_keys->'status_code_match',
    # test_keys->'headers_match' and test_keys->'body_length_match'
    SYNCRONIZE_DATE = settings.SYNCRONIZE_DATE
    if SYNCRONIZE_DATE is not None:
        SYNCRONIZE_DATE = make_aware(parse_datetime(settings.SYNCRONIZE_DATE))
        web_connectivity_metrics = Metric.objects.filter(
            test_name='web_connectivity',
            measurement_start_time__gte=SYNCRONIZE_DATE
        ).annotate(
            tcp_connect=RawSQL(
                "test_keys->'tcp_connect'", ()
            )
        )
    else:
        web_connectivity_metrics = Metric.objects.filter(
            test_name='web_connectivity'
        ).annotate(
            tcp_connect=RawSQL(
                "test_keys->'tcp_connect'", ()
            )
        )

    web_connectivity_metrics = web_connectivity_metrics.prefetch_related(
        'tcps'
    ).values(
        'id',
        'tcp_connect',
        'tcps'
    )

    web_connectivity_paginator = Paginator(web_connectivity_metrics, 1000)

    for p in web_connectivity_paginator.page_range:
        page = web_connectivity_paginator.page(p)

        for tcp_metric in page.object_list:
            for tcp_connect in tcp_metric['tcp_connect']:
                if tcp_metric['tcps'] is None and (
                    tcp_connect['status']['blocked'] is not None) and (
                    tcp_connect['status']['success'] is not None
                ):
                    tcp = TCP(
                        metric_id=tcp_metric['id'],
                        status_blocked=tcp_connect['status']['blocked'],
                        status_failure=tcp_connect['status']['failure'],
                        status_success=tcp_connect['status']['success']
                    )
                    tcp.save()


def tcp_to_flag():

    tcp = TCP.objects.filter(flag=None)

    tcp_paginator = Paginator(tcp, 1000)
    for p in tcp_paginator.page_range:
        page = tcp_paginator.page(p)
        for tcp_obj in page.object_list:
            flag = Flag(
                metric_date=tcp_obj.metric.measurement_start_time,
                flag=False
            )
            if tcp_obj.status_blocked:
                flag.is_flag = True
            else:
                flag.is_flag = False
            flag.save()
            tcp_obj.flag = flag
            tcp_obj.save()


def both():
    web_connectivity_to_tcp()
    tcp_to_flag()


def test():
    t = TCP.objects.all()

    for i in t:
        print i.flag.is_flag
