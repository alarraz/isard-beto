import asyncio
import logging
import threading
import itertools
import uuid
from pprint import pprint,pformat
import time


from core.lib import get_tid
import random

from common.exceptions.engine import *
from common.engine_actions import defined_engine_actions
from common.engine_actions import DEFAULT_TIMEOUT_WAITING_ACTION

class EngineAction():
    def __init__(self, action, timeout=None, **options):
        # verify action is defined
        self.event = threading.Event()
        if timeout is None:
            self.timeout = DEFAULT_TIMEOUT_WAITING_ACTION
        self.start_time = False
        self.time_elapsed = False
        self.q_action = False

        if action not in defined_engine_actions.keys():
            raise UnAcceptedEngineAction('Action notvalid, undefined', action)
        #
        self.action = action

        # verify mandatory arguments
        if all([mandatory in options.keys()
                for mandatory
                in defined_engine_actions[action]]) is False:
            raise UnAcceptedEngineAction('Mandatory arguments not in action', action, options.keys())
        self.options = options

        self.id_action = uuid.uuid4()
        self.d_action = {'action': self.action,
                         'id_action': self.id_action,
                         'options': self.options,
                         'timeout': self.timeout,
                         'event': self.event
                         }

    def launch(self, q_action, count, priority=100):
        self.q_action = q_action
        self.start_time = time.time()
        try:
            self.queue_actions.put_nowait((priority, count, self.d_action))
        except  asyncio.QueueFull as e:
            self.ActionQueueFull(e)

    def wait(self):
        done = self.event.wait(self.timeout + 1)
        self.time_elapsed = time.time() - self.start_time
        if done is True:
            return True
        if done is False:
            raise ActionWaitTimeout(self.timeout, self.action, self.options)