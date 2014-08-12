#
# -*- coding: utf-8 -*-
#

from django.conf import settings

from dtx import process, node

from dtx.core import logger
log = logger.log(__name__)

def start(**kwargs):
    node.start('dtx.memcache.client.node')
    
    port = int(kwargs.get('port', None))
    
    if (not port):
        log.err('Port is not specified')
        return
    
    try:
        from setproctitle import setproctitle
        setproctitle('Example: example.urls @ port {}'.format(port))
    except:
        pass

    for host in settings.PUBLIC_ADDRESSES:
        node.start('dtx.web.server.node',
            host=host, 
            port=port,
            sites=settings.DTX_WEB_MASTER_SITES
        )
