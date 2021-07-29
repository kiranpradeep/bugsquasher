import logging
import asyncio
from azure.iot.device.aio import IoTHubModuleClient


def message_handler(msg):
    logging.info(f"message received on input: {msg.data}")


async def main():
    module_client = IoTHubModuleClient.create_from_edge_environment()
    await module_client.connect()
    module_client.on_message_received = message_handler

    while True:
        await asyncio.sleep(1)


logging.basicConfig(format="%(asctime)s %(levelname).3s [%(filename)s:%(lineno)d] %(message)s", level=logging.DEBUG)
asyncio.run(main())
