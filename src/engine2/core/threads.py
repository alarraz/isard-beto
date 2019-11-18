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
    def __init__(self, name, engine):
        threading.Thread.__init__(self)

        self.engine = engine
        self.name = name
        self.stop = asyncio.Event()

        # try:
        #     assert(type(queue_actions) == asyncio.queues.PriorityQueue)
        # except AssertionError as e:
        #     logging.error('queue_actions is not priority async queue')
        #     raise AssertionError

    def run(self) -> None:
        self.tid = get_tid()
        logging.info("starting thread: {} (TID {})".format(self.name, self.tid))

        # Creating loop event (it is mandatory if the loop is running in not main thread)
        # asign loop to this thread
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        self.engine.config_loop(self.loop)

        self.engine.run_loop()

        # Creating queue
        self.q = asyncio.PriorityQueue(maxsize=MAXSIZE_QUEUE_ACTIONS,loop=self.loop)

        #TASKS
        wait_actions_task = self.loop.create_task(self.wait_actions())

        tasks = list()
        tasks.append(wait_actions_task)
        # tasks.append(self.random_actions())

        self.gathered_tasks = asyncio.gather(*tasks,loop=self.loop)
        self.loop.run_until_complete(self.gathered_tasks)

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

