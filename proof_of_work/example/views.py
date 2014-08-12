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


@inlineCallbacks
def hello(request):
    with log.enter() as tm:
        try:
            from crypto.views import sha256
            result = yield sha256(request, 'Hello World!!!', 0, 1000000)
            returnValue(render_to_response('json', {
                'status': 'success',
                'result': result,
                }))
            '''
            index = None
            digest = None
            for i in range(100000 * 100):
                m = hashlib.sha256()
                m.update('Hello World!!!' + str(i))
                d = m.hexdigest()
                if (not digest) or (digest > d):
                    index = i
                    digest = d
            returnValue(render_to_response('json', {
                'index': index,
                'digest': digest,
                }))
            '''
        except _DefGen_Return:
            raise
        except BaseException, ex:
            log.err(traceback.format_exc())
            returnValue(render_to_response('json', {
                'status': 'error',
            }, status=500))
    yield

