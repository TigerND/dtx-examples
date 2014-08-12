#
# -*- coding: utf-8 -*-
#

import traceback

from django.conf import settings
from django.http import HttpResponse

from dtx.core.workflow import *
from dtx.web.core.serializers import *
from dtx.web.server import *

import hashlib


from dtx.core import logger
log = logger.log(__name__)


def sha256(request, message, s, e):
    return deferToRemote(request, sha256_view).post(
        message=message, s=s, e=e
    )
    

@inlineCallbacks
def sha256_view(request, message, s, e):
    with log.enter() as tm:
        try:
            index = None
            digest = None
            for i in xrange(s, e):
                m = hashlib.sha256()
                m.update(message + str(i))
                d = m.hexdigest()
                if (not digest) or (digest > d):
                    index = i
                    digest = d
            returnValue(render_to_response('json', {
                'index': index,
                'digest': digest,
                }))
        except _DefGen_Return:
            raise
        except BaseException, ex:
            log.err(traceback.format_exc())
            returnValue(render_to_response('json', {
                'status': 'error',
            }, status=500))
    yield
