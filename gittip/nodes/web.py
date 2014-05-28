#
# -*- coding: utf-8 -*-
#

from django.conf import settings

from dtx import process, node

from dtx.core import logger
log = logger.log(__name__)

def start(**kwargs):
    node.start('dtx.memcache.client.node')
    
    node.start('dtx.telnet.server.node',
        host='localhost',
        port=9100,
        colored=True
    )
    
    for host in settings.PUBLIC_ADDRESSES:
        node.start('dtx.web.server.node',
            host=host, 
            port=8000 if (settings.DEBUG) else 80,
            sites=settings.DTX_WEB_MASTER_SITES
        )
