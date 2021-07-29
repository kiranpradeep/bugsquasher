import logging
import asyncio
from azure.iot.device.aio import IoTHubModuleClient
from azure.iot.device import Message


async def main():
    module_client = IoTHubModuleClient.create_from_edge_environment()
    await module_client.connect()

    counter = 0
    while True:
        msg = Message(str(counter))
        await module_client.send_message_to_output(msg, "output1")
        logging.info("Sent message #" + str(counter))
        counter += 1
        await asyncio.sleep(5)


logging.basicConfig(format="%(asctime)s %(levelname).3s [%(filename)s:%(lineno)d] %(message)s", level=logging.INFO)
asyncio.run(main())
