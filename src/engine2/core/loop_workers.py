import asyncio
import logging
import threading
import itertools
from pprint import pprint,pformat
from time import sleep

from core.lib import get_tid
import random

logging.basicConfig(level=logging.INFO)

class ActionsMockThread(threading.Thread):
    def __init__(self, name, queue_actions : asyncio.queues.PriorityQueue, max_random_sleep=5, queue_master=None):
        threading.Thread.__init__(self)
        self.counter = itertools.count()
        self.name = name
        self.stop = False
        self.queue_actions = queue_actions
        try:
            assert(type(queue_actions) == asyncio.queues.PriorityQueue)
        except AssertionError as e:
            logging.error('queue_actions is not priority async queue')
            raise AssertionError

        self.queue_master = queue_master
        self.max_random_sleep = max_random_sleep

    def run(self):
        self.tid = get_tid()
        logging.warning("starting thread: {} (TID {})".format(self.name, self.tid))
        # while self.stop is not True:
        #     self.sample_actions()
        for _ in range(3):
            self.sample_actions()
            sleep_time = random.randrange(1, self.max_random_sleep * 100) / 100.0
            sleep(sleep_time)
            if self.stop is not True:
                break


    def add_action(self,id_action,*args,priority=10,**kwargs, ):

        count = next(self.counter)
        print(f"new_action: {id_action}")
        d_action = {'id_action': id_action,
                    'args': args,
                    'kwargs': kwargs,
                    }
        pprint(d_action)
        self.queue_actions.put_nowait((priority,count,d_action))

    def domains_list(self,hyp_id):
        self.add_action('domains_list',
                        hyp_id = hyp_id)

    def dir_ls(self,hyp_id,path_dir):
        self.add_action('dir_ls',
                        hyp_id=hyp_id,
                        path_dir=path_dir)

    def restart_engine(self):
        self.add_action('restart_engine',priority=1)

    def sample_actions(self):
        self.domains_list('vdesktop1')
        self.domains_list('vdesktop2')
        self.domains_list('vdesktop5')
        self.dir_ls('vdesktop1','/tmp')
        self.restart_engine()




async def producer(iterable, queue: asyncio.Queue, shutdown_event: asyncio.Event):
    for i in iterable:
        if shutdown_event.is_set():
            break
        try:
            queue.put_nowait(i)
            await asyncio.sleep(0)

        except asyncio.QueueFull as err:
            logging.warning("The queue is too full. Maybe the worker are too slow.")
            raise err

    shutdown_event.set()


async def worker(name, handler, queue: asyncio.Queue, shutdown_event: asyncio.Event):
    while not shutdown_event.is_set() or not queue.empty():
        try:
            priority,count,d_action = queue.get_nowait()
            work = d_action['id_action']
            # Simulate work
            handler(await asyncio.sleep(1.0, work))
            logging.info(f"worker {name}: {work}")
            #pprint((priority,count,d_action))


        except asyncio.QueueEmpty:
            await asyncio.sleep(0)


async def async_main(queue):
    n, handler, iterable = 10, lambda val: None, [i for i in range(500)]
    shutdown_event = asyncio.Event()
    #queue = asyncio.Queue()
    worker_coros = [worker(f"worker_{i}", handler, queue, shutdown_event) for i in range(n)]
    #producer_coro = producer(iterable, queue, shutdown_event)

    coro = asyncio.gather(
        #producer_coro,
        *worker_coros,
        return_exceptions=True
    )

    try:
        await  coro
    except KeyboardInterrupt:
        shutdown_event.set()
        coro.cancel()



def launch_thread_mock():
    q = asyncio.PriorityQueue()
    # t = threading.Thread(name='worker_'+hyp_id,target=hyp_worker_thread, args=(hyp_id,q,queue_master))
    t = ActionsMockThread(name='mock_actions',
                          queue_actions=q,
                          )
    t.daemon = True
    t.start()
    return t, q

def main():
    # execute only if run as a script
    t, q = launch_thread_mock()
    sleep(1)
    try:
        asyncio.run(async_main())
    except KeyboardInterrupt:
        # It bubbles up
        logging.info("Pressed ctrl+c...")