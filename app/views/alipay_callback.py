import time
from asyncio import sleep, get_event_loop


async def page_pay_return(request):
    loop = get_event_loop()
    start_t = time.time()
    slp = loop.create_task(sleep(3))
    slp2 = loop.create_task(sleep(3))
    await slp
    await slp2

    end_t = time.time()

    return HttpResponse(f'来了老弟{start_t}，再来啊老弟{end_t}')


import asyncio
from django.http import HttpResponse
from django.views import View


class AsyncView(View):
    async def get(self, request, *args, **kwargs):
        await asyncio.sleep(2)
        return HttpResponse(f"Hello async world!,{time.time()}")
