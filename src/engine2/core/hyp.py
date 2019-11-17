# Copyright 2019 the Isard-vdi project authors:
#      Alberto Larraz Dalmases
#      Josep Maria Viñolas Auquer
# License: AGPLv3

import libvirt

from engine2.common.exceptions import UnAcceptedValueConnectionHypParameters



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
        self.alive_libvirt


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
        if all(x.find(' ')<0 for x in hostname.split('.')):
            raise UnAcceptedValueConnectionHypParameters(f"Hostname as space characters: {hostname}")

        if all(x.find(' ')<0 for x in username.split('.')):
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

