import grpc
from engine.grpc.proto import base_pb2
from engine.grpc.proto import base_pb2_grpc

import rethinkdb as r
from rethinkdb.errors import (
    ReqlAuthError,
    ReqlCursorEmpty,
    ReqlDriverError,
    ReqlError,
    ReqlInternalError,
    ReqlNonExistenceError,
    ReqlOpFailedError,
    ReqlOpIndeterminateError,
    ReqlPermissionError,
    ReqlQueryLogicError,
    ReqlResourceLimitError,
    ReqlRuntimeError,
    ReqlServerCompileError,
    ReqlTimeoutError,
    ReqlUserError)
from engine.grpc.lib.database import rdb
from engine.grpc.template import TemplateServicer
# ~ .TemplateAndBaseFromDesktop as TemplateAndBaseFromDesktop
# ~ from engine.grpc.grpc_actions import GrpcActions

from engine.grpc.statemachines.base_sm import BaseSM, StateInvalidError

MIN_TIMEOUT = 5  # Start/Stop/delete
MAX_TIMEOUT = 10 # Creations...

class BaseServicer(base_pb2_grpc.BaseServicer):
    """
    gRPC server for Templates Service
    """
    def __init__(self, app):
        # ~ self.grpc = GrpcActions(self.manager)
        self.base_sm = BaseSM()
    

    def List(self, request, context):
        ''' Checks '''
        try:
            with rdb() as conn:
                bases = list(r.table('domains').get_all('base', index='kind').pluck('id').run(conn))
                bases = [t['id'] for t in bases]
            return base_pb2.ListResponse(bases=bases)
        except Exception as e:
            print(e)
            context.set_details('Unable to access database.')
            context.set_code(grpc.StatusCode.INTERNAL)               
            return base_pb2.ListResponse()  

    def Get(self, request, context):
        ''' Checks '''
        try:
            with rdb() as conn:
                base = r.table('domains').get(request.base_id).run(conn)
            if len(base) == 0:
                context.set_details(request.base_id+'  not found in database.')
                context.set_code(grpc.StatusCode.UNKNOWN)
                return base_pb2.GetResponse()                     
            # ~ desktop['next_actions']=self.domain_actions.for_desktop(request.template_id,desktop['status'])
            return base_pb2.GetResponse(template=template)
        except ReqlNonExistenceError:
            context.set_details(request.template_id+' not found in database.')
            context.set_code(grpc.StatusCode.UNKNOWN)
            return base_pb2.GetResponse()             
        except Exception as e:
            context.set_details('Unable to access database.')
            context.set_code(grpc.StatusCode.INTERNAL)               
            return base_pb2.GetResponse() 
            
    def FromDesktop(self, request, context):
        return TemplateAndBaseFromDesktop('base', request, context)
                
    # ~ def TemplateAndBaseFromDesktop(self, kind, request, context):
        # ~ ''' Checks '''
        # ~ try:
            # ~ with rdb() as conn:
                # ~ template = r.table('domains').get(request.template_id).pluck('id').run(conn)
            # ~ context.set_details(request.template_id+' already exists in system.')
            # ~ context.set_code(grpc.StatusCode.FAILED_PRECONDITION)                
            # ~ return base_pb2.TemplateFromDesktopResponse()                
        # ~ except ReqlNonExistenceError:
            # ~ pass        
        # ~ except Exception as e:
            # ~ context.set_details('Unable to access database.')
            # ~ context.set_code(grpc.StatusCode.INTERNAL)               
            # ~ return base_pb2.TemplateFromDesktopResponse()
        # ~ try:
            # ~ with rdb() as conn:
                # ~ desktop = r.table('domains').get(request.desktop_id).without('history_domain').run(conn)
            # ~ if desktop['status'] not in ['Stopped']: 
                # ~ context.set_details(request.desktop_id+' it is not stopped.')
                # ~ context.set_code(grpc.StatusCode.FAILED_PRECONDITION)                
                # ~ return base_pb2.TemplateFromDesktopResponse()
            # ~ elif desktop['kind'] != 'desktop':
                # ~ context.set_details(request.desktop_id+' it is not a desktop.')
                # ~ context.set_code(grpc.StatusCode.FAILED_PRECONDITION)                
                # ~ return base_pb2.TemplateFromDesktopResponse()                
        # ~ except ReqlNonExistenceError:
            # ~ context.set_details(request.desktop_id+' not found in database.')
            # ~ context.set_code(grpc.StatusCode.UNKNOWN)
            # ~ return base_pb2.TemplateFromDesktopResponse()         
        # ~ except Exception as e:
            # ~ context.set_details('Unable to access database.')
            # ~ context.set_code(grpc.StatusCode.INTERNAL)               
            # ~ return base_pb2.TemplateFromDesktopResponse()
        
        # ~ ''' OPTIONAL HARDWARE VALUES | GET FROM DESKTOP '''
        # ~ hardware = {}
        # ~ hardware['vcpus'] = int(desktop['create_dict']['hardware']['vcpus']) if request.hardware.vcpus == 0 else request.hardware.vcpus
        # ~ hardware['memory'] = int(desktop['create_dict']['hardware']['memory']) if request.hardware.memory == 0 else request.hardware.memory
        # ~ hardware['videos'] = desktop['create_dict']['hardware']['videos'] if len(request.hardware.videos) == 0 else request.hardware.videos
        # ~ hardware['graphics'] = desktop['create_dict']['hardware']['graphics'] if len(request.hardware.graphics) == 0 else request.hardware.graphics
        # ~ hardware['boot_order'] = desktop['create_dict']['hardware']['boot_order'] if len(request.hardware.boots) == 0 else request.hardware.boots
        # ~ hardware['interfaces'] = desktop['create_dict']['hardware']['interfaces'] if len(request.hardware.interfaces) == 0 else request.hardware.interfaces
        # ~ hardware['isos'] = desktop['create_dict']['hardware']['isos'] if len(request.hardware.isos) == 0 and 'isos' in desktop['create_dict']['hardware'].keys() else request.hardware.isos
        # ~ hardware['floppies'] = desktop['create_dict']['hardware']['floppies'] if len(request.hardware.floppies) == 0  and 'floppies' in desktop['create_dict']['hardware'].keys() else request.hardware.floppies
        # ~ ## Check for .qcow in boot_disk_rpath??   
        # ~ hardware['disks']=[{'file': request.template_id + '.qcow2' if request.hardware.boot_disk_rpath == '' else request.hardware.boot_disk_rpath,
                            # ~ 'parent':''}]    
        # ~ ### ~ if request.hardware.boot_disk_bus == '': request.hardware.boot_disk_bus = 'virtio'
                           
        # ~ ''' Create a new minimal domain inside template_dict '''
        # ~ create_dict=desktop['create_dict']
        # ~ create_dict['origin']=request.desktop_id
        # ~ create_dict['template_dict']={ 'id': request.template_id,
                                        # ~ 'kind': kind,
                                        # ~ 'hypervisors_pools': desktop['hypervisors_pools'],
                                        # ~ 'create_dict': {'hardware': hardware}}
                                        
        # ~ ''' Add template_id '''
        # ~ try:
            # ~ ''' DIRECT TO ENGINE '''
            # ~ ### ~ self.grpc.add_template_from_desktop(request.desktop_id)
            # ~ ''' DATABASE '''
            # ~ with rdb() as conn:
                # ~ r.table('domains').get(request.desktop_id).update({'create_dict':create_dict,'status':'CreatingTemplate'}).run(conn)
                # ~ c=r.table('domains').get(request.desktop_id).changes().filter({'new_val':{'status':'Stopped'}}).run(conn) 
                # ~ c.next(MAX_TIMEOUT)
                # ~ next_actions = action[state['new_val']['status'].capitalize()]
                # ~ return base_pb2.TemplateFromDesktopResponse(state='STOPPED', next_actions=next_actions)
        # ~ except ReqlTimeoutError:
            # ~ context.set_details('Unable to create the domain '+request.template_id)
            # ~ context.set_code(grpc.StatusCode.INTERNAL)             
            # ~ return base_pb2.TemplateFromDesktopResponse()            
        # ~ except Exception as e:
            # ~ context.set_details(str(e))
            # ~ context.set_code(grpc.StatusCode.INTERNAL)             
            # ~ return base_pb2.TemplateFromDesktopResponse()


