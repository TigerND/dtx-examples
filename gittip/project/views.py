#
# -*- coding: utf-8 -*-
#

from django.conf import settings
from django.http import HttpResponseRedirect

from dtx.core.workflow import *
from dtx.web.core.serializers import *
from dtx.web.server import *

from dtx.core import logger
log = logger.log(__name__)


def home(request):
    with log.enter() as tm:
        return HttpResponseRedirect('/gittip/info/')
