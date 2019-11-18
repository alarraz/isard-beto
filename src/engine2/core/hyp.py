# Copyright 2019 the Isard-vdi project authors:
#      Alberto Larraz Dalmases
#      Josep Maria Viñolas Auquer
# License: AGPLv3

import sys
import logging
import libvirt

from models.domain import Domain
from common.exceptions.engine import UnAcceptedValueConnectionHypParameters

def hostname_to_uri(hostname, user='root', port=22):
    if (hostname == '127.0.0.1') or (hostname == 'localhost'):
        uri = 'qemu:///system'
    else:
        uri = 'qemu+ssh://{}@{}:{}/system'.format(user, hostname, port)
    return uri



class Hyp(object):
    """Operates with libvirt hypervisor

    Try connect with ssh with detailed error, create connexions, register stats.

    Args:
        hostname (str): valid hostname to connect via ssh.
        username (Optional[str]): Defaults to 'root'.
        port (Optional[int]): Defaults to 22.

    Attributes:
        conn: Libvirt connection if established

    """
    def __init__(self, hostname: str, username: str = 'root', port: int = 22):
        """Try to connect to hypervisor
        Raises:
            UnAcceptedValueConnectionHypParameters: if port or hostname are invalid"""

        self.verify_parameters_ssh(port,hostname,username)
        self.port = port
        self.hostname = hostname
        self.username = username
        self.alive_ssh = False
        self.alive_libvirt = False
        self.conn = False

    def open_libvirt_connection(self):
        """ create libvirt hypervisor connecton"""
        self.uri = hostname_to_uri(self.hostname, user=self.username, port=self.port)

        try:
            self.conn = libvirt.open(self.uri)
        except libvirt.libvirtError as e:
            self.conn = False
            logging.error()
            raise e

    def get_xml(self,domain_id):
        try:
            xml = Domain.get_xml(domain_id)
            return xml
        except Exception as e:
            raise e

    def start_domain(self,domain_id):
        xml = self.get_xml()
        self.start_domain()

    def libvirt_conn_is_alive(self):
        if self.conn is not False:
            try:
                if self.conn.isAlive():
                    self.alive_libvirt = True
                else:
                    self.alive_libvirt = False
            except:
                self.alive_libvirt = False

    def start_from_xml(self,xml):
        try:
            d = self.conn.createXML(xml)
        except libvirt.libvirtError as e:
            #if create fail, we can test if xml sintax is ok
            try:
                d = self.conn.defineXML(xml)
                d.undefine()
            except libvirt.libvirtError as e:
                raise e
            raise e
        except Exception as e:
            raise e
        else:
            return d

    def start_from_xml(self,xml):
        try:
            d = self.conn.createXML(xml, flags=libvirt.VIR_DOMAIN_START_PAUSED)
            xml_started = d.XMLDesc()
            xml_stopped = d.XMLDesc(libvirt.VIR_DOMAIN_XML_INACTIVE)
            d.destroy()
        except libvirt.libvirtError as e:
            #if create fail, we can test if xml sintax is ok
            try:
                d = self.conn.defineXML(xml)
                d.undefine()
            except libvirt.libvirtError as e:
                raise e
            raise e
        except Exception as e:
            raise e
        else:
            return True, xml_started, xml_stopped

    def get_domains(self):
        """
        return dictionary with domain objects of libvirt
        keys of dictionary are names
        domains can be started or paused
        """
        if self.connected:
            self.domains = {}
            try:
                for d in self.conn.listAllDomains(libvirt.VIR_CONNECT_LIST_DOMAINS_ACTIVE):
                    try:
                        domain_name = d.name()
                    except:
                        log.info('unkown domain fail when trying to get his name, power off??')
                        continue
                    if domain_name[0] == '_':
                        self.domains[domain_name] = d
            except:
                log.error('error when try to list domain in hypervisor {}'.format(self.hostname))
                self.domains = {}

    def verify_parameters_ssh(self,port,hostname,username):
        if type(port) is not int:
            raise UnAcceptedValueConnectionHypParameters("Port for ssh connection must be integer")
        if type(hostname) is not str:
            raise UnAcceptedValueConnectionHypParameters("Hostname for ssh connection must be string")
        if type(username) is not str:
            raise UnAcceptedValueConnectionHypParameters("Username for ssh connection must be string")

        #port between 1 and 2^16
        if 1 < port < pow(2, 16):
            port = int(port)
        else:
            log.error("port to connect hypervisor {} is not valid: {port}")
            raise UnAcceptedValueConnectionHypParameters("Port innvalid, must be between 1 and 2^16: {port}")

        #test if hostame is valid
        if hostname[-1] == ".":
            hostname = hostname[:-1]  # strip exactly one dot from the right, if present
        #allowed = re.compile("(?!-)[A-Z\d-]{1,63}(?<!-)$", re.IGNORECASE)
        #if all(allowed.match(x) for x in hostname.split(".")) is False:
        if hostname.find('.') >= 0:
            if all(x.find(' ')<0 for x in hostname.split('.')):
                raise UnAcceptedValueConnectionHypParameters(f"Hostname as space characters: {hostname}")

        if username.find(' ')>=0:
            raise UnAcceptedValueConnectionHypParameters(f"Username as space characters: {username}")

    async def open_ssh_process(self):
        print('antes de conexion')
        self.conn = await create_conn()
        self.process = await self.conn.create_process()
        print('conexión ok')
        self.conn_ok.set()
        self.send_cmd_event.set()

    async def cmd_event_launch(self):
        while not self.shutdown_event.is_set():
            if self.ok == True:
                print('voy a poner a ok el evento send_cmd')
                self.send_cmd_event.set()
                self.ok = False
            #print('antes del sleep')
            await asyncio.sleep(0.1)
            #print('despues del sleep')

    async def send_command(self):
        await self.conn_ok.wait()
        print('salgo del await evento de conexión')

        while not self.shutdown_event.is_set():
            print('dentro del bucle que espera a send_cmd_event')
            await self.send_cmd_event.wait()
            print(f'se ha activado el evento cmd_event ')
            print(f'el comando es: {self.command}')
            self.process.stdin.write(self.command)
            self.process.stdin.write('\n')
            #self.process.stdin.write_eof()
            print('comando enviado')
            #stdout_data, stderr_data = await self.process.communicate()
            stdout_data = await self.process.stdout.readline()
            #stderr_data = await self.process.stderr.read()
            print('datos recogidos:')
            pprint(stdout_data)
            #pprint(stderr_data)
            await asyncio.sleep(0.1)
            self.send_cmd_event.clear()

