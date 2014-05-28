#
# -*- coding: utf-8 -*-
#

import traceback

from django.conf import settings
from django.http import HttpResponse

from dtx.core.workflow import *
from dtx.web.core.serializers import *
from dtx.web.server import *

import txgittip

from dtx.core import logger
log = logger.log(__name__)


@inlineCallbacks
def info(request, username=None):
    with log.enter() as tm:
        try:
    	    requests = [txgittip.api.charts(),
                        txgittip.api.paydays(),
                        txgittip.api.stats(),
                       ]
            if (username):
                requests += [txgittip.api.charts(username),
                             txgittip.api.public(username),
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
