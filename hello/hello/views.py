#
# -*- coding: utf-8 -*-
#

from django.conf import settings
from django.http import HttpResponse

from dtx.core.workflow import *
from dtx.web.core.serializers import *
from dtx.web.server import *

from dtx.core import logger
log = logger.log(__name__)


@inlineCallbacks
def say(request, message):
    with log.enter() as tm:
        returnValue(HttpResponse(message, content_type='text/plain', status=200))
    yield
