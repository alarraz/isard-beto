from core.loop_workers import *
t, q = launch_thread_mock()

try:
    asyncio.run(async_main(q))
except KeyboardInterrupt:
    # It bubbles up
    logging.info("Pressed ctrl+c...")