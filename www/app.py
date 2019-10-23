#!/usr/bin/env python3
# -*- codding: utf-8 -*-

__author__ = 'Murphy Zheng'

'''
async web application
'''

import logging; logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time
from datetime import datetime
from aiohttp import web

def index(request):
	return web.Response(body=b'<h1>Welcome and enjoy python3</h1>',content_type='text/html')

async def init():
	app = web.Application()
	app.add_routes([web.get('/',index)])

	host = 'localhost'
	port = '9000'

	runner = web.AppRunner(app)
	await runner.setup()
	site = web.TCPSite(runner, host, port)
	await site.start()
	print('服务器启动成功！')
	print('host:' + host)
	print('port:' + port)

loop = asyncio.get_event_loop()
loop.run_until_complete(init())
loop.run_forever()