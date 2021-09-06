"""
Services
----------------

An example showing how to fetch all services and print them.
获取所以服务并打印他们
Updated on 2019-03-25 by hbldh <henrik.blidh@nedomkull.com>

"""

import sys
import asyncio
import platform

from bleak import BleakClient

ADDRESS = (
    "54:B7:E5:79:F4:49"
    if platform.system() != "Darwin"
    # else "B9EA5233-37EF-4DD6-87A8-2A875E821C46"
    else "FFF0"
)
if len(sys.argv) == 2:
    ADDRESS = sys.argv[1]


async def print_services(mac_addr: str):
    async with BleakClient(mac_addr) as client:
        svcs = await client.get_services()
        print("Services:")
        for service in svcs:
            print(service)


loop = asyncio.get_event_loop()
loop.run_until_complete(print_services(ADDRESS))
