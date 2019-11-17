# Copyright 2019 the Isard-vdi project authors:
#      Alberto Larraz Dalmases
#      Josep Maria Viñolas Auquer
# License: AGPLv3
#
# coding=utf-8

"""Threads running in engine"""

import asyncio
import logging
import threading
import itertools
import random

from core.lib import get_tid
from common.exceptions.engine import *

TIMEOUT_TO_STOP = 0.5
MAXSIZE_QUEUE_ACTIONS = 1000

class ActionsThread(threading.Thread):
    """Thread that waits actions in asyncio queue and dispatch to other tasks.



    Attributes:
        tid (int): Thread ID, useful if you want to identify with htop.
        loop: asyncio loop running in thread
        q:    asyncio priority queue
        stop: asyncio Event to stop queue

    """
    def __init__(self, name):
        threading.Thread.__init__(self)

        self.name = name
        self.stop = asyncio.Event()

        # try:
        #     assert(type(queue_actions) == asyncio.queues.PriorityQueue)
        # except AssertionError as e:
        #     logging.error('queue_actions is not priority async queue')
        #     raise AssertionError

        self.max_random_sleep = max_random_sleep

    def run(self) -> None:
        self.tid = get_tid()
        logging.info("starting thread: {} (TID {})".format(self.name, self.tid))

        # Creating loop event (it is mandatory if the loop is running in not main thread)
        # asign loop to this thread
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

        # Creating queue
        self.q = asyncio.PriorityQueue(maxsize=MAXSIZE_QUEUE_ACTIONS)

        #TASKS
        wait_actions_task = self.loop.create_task(self.wait_actions())

        tasks = list()
        tasks.append(wait_actions_task)
        # tasks.append(self.random_actions())

        self.gathered_tasks = asyncio.gather(*tasks)
        self.loop.run_until_complete(self.gathered_tasks)
        # asyncio.run(self.main())


    async def random_actions(self):
        counter = itertools.count()
        while True:
            count = next(counter)
            await asyncio.sleep(0.5 + 1 * random.random())
            print(f'random_action {count}')
            item =  (10,
                     count,
                     {'action': 'ACTION_START',
                      'scope': 'domain',
                      'parameters': {'domain_id': '_prova_prova'}})
            # await self.q.put(item)
            self.q.put_nowait(item)

    async def wait_actions(self):
        assert self.loop == asyncio.get_running_loop()
        item = (10,
                0,
                {'action': 'ACTION_START',
                 'parameters': {'domain_id': '_prova_prova'},
                 'scope': 'domain'})
        self.q.put_nowait(item)

        while not self.stop.is_set():
            try:
                print('antes de get')
                #self.pop_item = await self.q.get()
                self.pop_item = await asyncio.wait_for(self.q.get(),
                                                       TIMEOUT_TO_STOP)
                print('después de get')
                (priority, count, d_action) = self.pop_item
                # priority, count, d_action = await self.q.get()
                scope  = d_action['scope']
                action = d_action['action']
                print(f' >>>> SCOPE: scope / ACTION: action')
                # Simulate work
                await asyncio.sleep(0.5 + 1 * random.random())
                print('action finalished')
                pprint.pprint(d_action)
                # logging.info(f"worker {name}: {work}")
                # pprint.pprint((priority,count,d_action))

            except asyncio.TimeoutError:
                print('Timeout')
                pass

            except asyncio.QueueEmpty:
                print('queue empty')
                await asyncio.sleep(0)

        logging.info('STOP event is set, waiting actions finalished')
