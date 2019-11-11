

import threading
from pprint import pprint

import asyncio, asyncssh, sys

class MySSHClientSession(asyncssh.SSHClientSession):
    def data_received(self, data, datatype):
        print(data, end='')

    def connection_lost(self, exc):
        if exc:
            print('SSH session error: ' + str(exc), file=sys.stderr)

async def create_chan_session(hostname='isard-hypervisor'):
    async with asyncssh.connect(hostname) as conn:
        chan, session = await conn.create_session(MySSHClientSession, 'ls abc')
        return chan,session

async def create_conn(hostname='isard-hypervisor'):
    return await asyncssh.connect(hostname)

async def open_process():
    conn = await create_conn()
    process = await conn.create_process()
    process.stdin.write("date")
    process.stdin.write_eof()
    print('>>>>>' + process. collect_output())
    #result = await process.wait()
    stdout_data, stderr_data = await process.communicate()



async def test_order(command):
    conn = await create_conn()
    process = await conn.create_process()
    process.stdin.write(command)
    process.stdin.write_eof()
    print('>>>>>')
    from pprint import pprint
    pprint(process.collect_output())
    #result = await process.wait()
    return process,conn

async def get_command_result(process):
    process.communicate()
    result = False
    stdout_data = False
    stderr_data = False
    #result = await process.wait()
    stdout_data, stderr_data = await process.communicate()
    return result, stdout_data, stderr_data


class AsyncsRunThread(threading.Thread):
    def __init__(self, name, command):
        threading.Thread.__init__(self)
        self.command = command
        self.name = name
        self.ok = False

    def run(self) -> None:
        #self.loop = asyncio.get_running_loop()
        #Creating loop event
        self.loop = asyncio.new_event_loop()
        #asign loop to this thread
        asyncio.set_event_loop(self.loop)

        asyncio.run(self.main())
        self.get_result()

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

    def set_next_command(self,command):
        self.command = command

    def get_result(self):
        result, stdout_data, stderr_data = get_command_result(self.process)
        pprint(result)
        pprint(stdout_data)
        pprint(stderr_data)

    async def main(self):
        self.send_cmd_event = asyncio.Event()
        self.conn_ok = asyncio.Event()
        self.shutdown_event = asyncio.Event()
        queue = asyncio.Queue()

        await asyncio.gather(self.open_ssh_process(),
                             self.send_command(),
                             self.cmd_event_launch(),
                             )

    async def worker(name, handler, queue: asyncio.Queue,
                     shutdown_event: asyncio.Event):
        while not shutdown_event.is_set() or not queue.empty():
            try:
                work = queue.get_nowait()
                # Simulate work
                handler(await
                asyncio.sleep(1.0, work))
                #logging.debug(f"worker {name}: {work}")
            except asyncio.QueueEmpty:
                await asyncio.sleep(0)

if __name__ == '__main__':
    t = AsyncsRunThread(name='jaja',command='date')
    t.daemon = True
    t.start()
    sleep(2)
    t.ok = True