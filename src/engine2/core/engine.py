import asyncio
import logging
import threading
import itertools
#import janus
import uuid
import pprint
import time

from core.threads import ActionsThread
from core.lib import get_tid
import random

from common.exceptions.engine import *
from common.engine_actions import defined_engine_actions
from common.engine_actions import DEFAULT_TIMEOUT_WAITING_ACTION

#from core.actions import *

class Engine():
    def __init__(self):
        self.counter = itertools.count()
        self.main_thread = ActionsThread(name='actions_thread')
        pass

    def run_main_thread(self):
        self.main_thread.daemon = True
        self.main_thread.start()

    def enqueue_action(self,action,scope='domain',priority=10,**parameters):
        count = next(self.counter)
        d_action = {'action': action,
                    'scope':  scope,
                    'parameters': parameters
                    }
        item = (priority,count,d_action)
        pprint.pprint(item)
        self.main_thread.q.put_nowait(item)
        self.main_thread.q._loop._write_to_self()

    def start_domain(self,domain_id):
        self.enqueue_action('ACTION_START',domain_id=domain_id)



def main():
    e = Engine()
    e.run_main_thread()
    return e

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