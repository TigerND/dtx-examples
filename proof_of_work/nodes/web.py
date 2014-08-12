#
# -*- coding: utf-8 -*-
#

from django.conf import settings

from dtx import process, node

from dtx.core import logger
log = logger.log(__name__)

def start(**kwargs):

    try:
        from setproctitle import setproctitle
        setproctitle('Example: Main process')
    except:
        pass

    def startNodes(cnt, base_port, node_module):
        for p in range(cnt):
            port = base_port + p
            process.start(node_module,
                logfile='{}.{}.log'.format(node_module, port),
                port=port,
                uid=settings.DTX_WEB_UID
            )
            
    startNodes(settings.DTX_WEB_EXAMPLE_PROCESS_COUNT,
               settings.DTX_WEB_EXAMPLE_BASE_PORT,
               'nodes.web_example')
               
    startNodes(settings.DTX_WEB_CRYPTO_PROCESS_COUNT,
               settings.DTX_WEB_CRYPTO_BASE_PORT,
               'nodes.web_crypto')
               
