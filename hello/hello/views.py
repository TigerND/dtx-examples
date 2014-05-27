#
# -*- coding: utf-8 -*-
#

import traceback

from django.conf import settings
from django.http import HttpResponse

from dtx.core.workflow import *
from dtx.web.core.serializers import *
from dtx.web.server import *
from twisted.web.client import getPage

from dtx.core import logger
log = logger.log(__name__)


@inlineCallbacks
def say(request, message):
    with log.enter() as tm:
        returnValue(HttpResponse(message, content_type='text/plain', status=200))
    yield


@inlineCallbacks
def gw2test(request, item_id):
    with log.enter() as tm:
        try:
            x = yield getPage('https://api.guildwars2.com/v1/item_details.json?item_id=' + str(item_id))
            details = json.loads(x)
            returnValue(HttpResponse(str(details['name']), content_type='text/plain'))
        except _DefGen_Return:
            raise
        except BaseException, ex:
            log.err(traceback.format_exc())
            returnValue(HttpResponse('Unknown', content_type='text/plain', status=404))
