# -*- coding: utf-8 -*-
# from .settings import PORTAL_URL

def students_proc(request):
    portal_url = request.build_absolute_uri('/')
    if portal_url.endswith('/'):
        portal_url = portal_url[:-1]
    return {'PORTAL_URL': portal_url}

