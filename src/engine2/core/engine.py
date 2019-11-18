import asyncio
import logging
import threading
import itertools
#import janus
import uuid
import pprint
import time
import functools
import concurrent.futures

from core.threads import ActionsThread
from core.lib import get_tid
import random

from common.exceptions.engine import *
from common.engine_actions import defined_engine_actions
from common.engine_actions import DEFAULT_TIMEOUT_WAITING_ACTION

#from core.actions import *

MAXSIZE_QUEUE_ACTIONS = 1000
TIMEOUT_TO_STOP = 0.5
MAX_WORKERS_POOL_EXECUTOR = 5

class ActionsQueue(asyncio.PriorityQueue):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.counter = itertools.count()

    def enqueue_action(self, action, scope='domain', priority=10, **parameters):
            count = next(self.counter)
            d_action = {'action': action,
                        'scope': scope,
                        'parameters': parameters
                        }
            item = (priority, count, d_action)
            pprint.pprint(item)
            self.put_nowait(item)
            self._loop._write_to_self()

class BlockingTasks():
    def __init__(self,loop,executor):
        self.loop = loop
        self.executor = executor
        self.tasks_definition = list()
        self.blocking_tasks = None

    def add_task(self,func,*args,**kwargs):
        self.tasks_definition.append(functools.partial(func, *args, **kwargs))

    async def run_blocking_tasks(self):
        log = logging.getLogger('run_blocking_tasks')
        log.info('starting')
        log.info('creating executor tasks')

        self.blocking_tasks = [
            self.loop.run_in_executor(self.executor, task)
            for task in self.tasks_definition
        ]

        log.info('waiting for executor tasks')
        completed, pending = await asyncio.wait(blocking_tasks)
        results = [t.result() for t in completed]
        log.info('results: {!r}'.format(results))
        log.info('exiting')



class BootEngine():
    def __init__(self,engine):
        self.main_thread = ActionsThread(name='actions_thread',engine=engine)
        pass

    def run_main_thread(self):
        self.main_thread.daemon = True
        self.main_thread.start()

class Engine():
    def __init__(self):
        pass

    def config_loop(self,loop):
        self.loop = loop

    def init_queues_and_events(self):
        # Creating queue
        self.q_main = ActionsQueue(maxsize=MAXSIZE_QUEUE_ACTIONS,
                                       loop=self.loop)
        self.q_domain_actions = ActionsQueue(maxsize=MAXSIZE_QUEUE_ACTIONS,
                                       loop=self.loop)
        self.q_disk_actions = ActionsQueue(maxsize=MAXSIZE_QUEUE_ACTIONS,
                                       loop=self.loop)
        self.q_hypervisors_actions = ActionsQueue(maxsize=MAXSIZE_QUEUE_ACTIONS,
                                       loop=self.loop)

        self.stop = asyncio.Event(loop=self.loop)

    def init_thread_pool(self):
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=5,
                                                              thread_name_prefix='x_')



    def update_hypervisor_queues(self):
        pass



    def run_loop(self):

        self.init_queues_and_events()

        #CREATE TASKS
        self.wait_actions_task = self.loop.create_task(self.wait_actions())

        #GATHER TASKS
        tasks = list()
        tasks.append(self.wait_actions_task)
        # tasks.append(self.random_actions())
        self.gathered_tasks = asyncio.gather(*tasks,loop=self.loop)

        #RUN
        self.loop.run_until_complete(self.gathered_tasks)

    def enqueue_action(self,action,scope='domain',priority=10,**parameters):
        count = next(self.counter)
        d_action = {'action': action,
                    'scope':  scope,
                    'parameters': parameters
                    }
        item = (priority, count, d_action)
        pprint.pprint(item)
        self.q_main.put_nowait(item)
        self.q_main._loop._write_to_self()

    def start_domain(self,domain_id):
        self.q_main.enqueue_action('ACTION_START',domain_id=domain_id)

    async def domain_action_dispatcher(self):
        while not self.stop.is_set():
            pop_item = await asyncio.wait_for(self.q_main.get(),
                                                   TIMEOUT_TO_STOP)

    async def wait_actions(self):
        #assert self.loop == asyncio.get_running_loop()
        item = (10,
                0,
                {'action': 'ACTION_START',
                 'parameters': {'domain_id': '_prova_prova'},
                 'scope': 'domain'})
        self.q_main.put_nowait(item)

        while not self.stop.is_set():
            try:
                #print('antes de get')
                #self.pop_item = await self.q_main.get()
                self.pop_item = await asyncio.wait_for(self.q_main.get(),
                                                       TIMEOUT_TO_STOP)
                print('después de get')
                (priority, count, d_action) = self.pop_item
                # priority, count, d_action = await self.q_main.get()
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
                #print('Timeout')
                pass

            except asyncio.QueueEmpty:
                print('queue empty')
                await asyncio.sleep(0)

        logging.info('STOP event is set, waiting actions finalished')


def main():
    engine = Engine()
    b = BootEngine(engine=engine)
    b.run_main_thread()
    return b

if __name__ == "__main__":
    print('running engine')
    main()

    # def add_action(self,id_action,*args,priority=10,**kwargs, ):
    #
    #     count = next(self.counter)
    #     print(f"new_action: {id_action}")
    #     d_action = {'id_action': id_action,
    #                 'args': args,
    #                 'kwargs': kwargs,
    #                 }
    #     pprint.pprint(d_action)
    #     self.queue_actions.put_nowait((priority,count,d_action))
    #
    # def domains_list(self,hyp_id):
    #     self.add_action('domains_list',
    #                     hyp_id = hyp_id)
    #
    # def dir_ls(self,hyp_id,path_dir):
    #     self.add_action('dir_ls',
    #                     hyp_id=hyp_id,
    #                     path_dir=path_dir)
    #
    # def restart_engine(self):
    #     self.add_action('restart_engine',priority=1)
    #
    # def sample_actions(self):
    #     self.domains_list('vdesktop1')
    #     self.domains_list('vdesktop2')
    #     self.domains_list('vdesktop5')
    #     self.dir_ls('vdesktop1','/tmp')
    #     self.restart_engine()