from event.models import State, Country, ISP, Plan
from measurement.models import Metric, Probe


def dict_compare(d1, d2):
    d1_keys = set(d1.keys())
    d2_keys = set(d2.keys())
    intersect_keys = d1_keys.intersection(d2_keys)
    added = d1_keys - d2_keys
    removed = d2_keys - d1_keys
    modified = {o: (d1[o], d2[o]) for o in intersect_keys if d1[o] != d2[o]}
    same = set(o for o in intersect_keys if d1[o] == d2[o])
    return added, removed, modified, same


def give_probes_to_metrics():
    metrics = Metric.objects.all()
    for metric in metrics:
        probe = Probe.objects.all().order_by('?').first()
        metric.annotations['probe'] = probe.identification
        metric.save()


def create_isps():
    isp1 = ISP(
        name='Cantv'
    )
    isp1.save()
    isp2 = ISP(
        name='Digitel'
    )
    isp2.save()
    isp3 = ISP(
        name='Inter'
    )
    isp3.save()
    isp4 = ISP(
        name='NetUno'
    )
    isp4.save()
    isp5 = ISP(
        name='Movistar'
    )
    isp5.save()


def create_plans():
    isps = ISP.objects.all()
    for isp in isps:
        p1 = Plan(
            name='12Mb',
            isp=isp,
            upload='3Mb',
            download='8Mb'
        )
        p1.save()
        p2 = Plan(
            name='10Mb',
            isp=isp,
            upload='2Mb',
            download='6Mb'
        )
        p2.save()
        p3 = Plan(
            name='6Mb',
            isp=isp,
            upload='1Mb',
            download='3Mb'
        )
        p3.save()
        p4 = Plan(
            name='4Mb',
            isp=isp,
            upload='500Kb',
            download='1Mb'
        )
        p4.save()


def create_probes():

    country = Country.objects.get(name='Venezuela')
    for i in range(1000, 1400):
        state = State.objects.filter(country=country).order_by('?').first()
        isp = ISP.objects.order_by('?').first()
        plan = Plan.objects.filter(isp=isp).order_by('?').first()
        p = Probe(
            identification=i,
            region=state,
            country=country,
            city='Generic City',
            isp=isp,
            plan=plan
        )
        try:
            p.save()
        finally:
            print(i)


def probes_pls():
    create_isps()
    create_plans()
    create_probes()
