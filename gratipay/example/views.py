#
# -*- coding: utf-8 -*-
#

import traceback

from django.conf import settings
from django.http import HttpResponse

from dtx.core.workflow import *
from dtx.web.core.serializers import *
from dtx.web.server import *

import txgratipay

from dtx.core import logger
log = logger.log(__name__)


@inlineCallbacks
def info(request, username=None):
    with log.enter() as tm:
        try:
    	    requests = [txgratipay.api.charts(),
                        txgratipay.api.paydays(),
                        txgratipay.api.stats(),
                       ]
            if (username):
                requests += [txgratipay.api.charts(username),
                             txgratipay.api.public(username),
                            ]
            results = yield gatherResults(requests)
            def extract_results(gcharts, gpaydays, gstats, ucharts=None, upublic=None):
                return (gcharts, gpaydays, gstats, ucharts, upublic)
            gcharts, gpaydays, gstats, ucharts, upublic = extract_results(*results)
            returnValue(render_to_response('json', {
                'status': 'success',
                'about': {
                    'charts': gcharts,
                    'paydays': gpaydays,
                    'stats': gstats,
                },
                'user': {
                    'name': username,
                    'charts': ucharts,
                    'public': upublic,
                },
            }))
        except _DefGen_Return:
            raise
        except BaseException, ex:
            log.err(traceback.format_exc())
            returnValue(render_to_response('json', {
                'status': 'error',
            }, status=500))


@inlineCallbacks
def update(request):
    with log.enter() as tm:
        sender = None
        recepient = None
        apikey = None
        tips = [
            { 'username': recepient,
              'platform': 'gratipay',
              'amount': '0.01',
            },
        ]
        try:
            if ((not sender) or (not recepient) or (not apikey)):
                returnValue(u'No sender/recepient/apikey have been specified')
            result = yield txgratipay.api.tips(sender, apikey, tips)
            returnValue(render_to_response('json', {
                'status': 'success',
                'result': result
            }))
        except _DefGen_Return:
            raise
        except BaseException, ex:
            log.err(traceback.format_exc())
            returnValue(render_to_response('json', {
                'status': 'error',
            }, status=500))
