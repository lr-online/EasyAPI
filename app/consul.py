import httpx
from loguru import logger

from settings import CONSUL_HOST, CONSUL_PORT, SERVER_HOST, SERVER_PORT, SERVER_NAME

check = {
    # "GRPC": f"{SERVER_HOST}:{SERVER_PORT}",
    # "GRPCUseTLS": False,
    "HTTP": f"http://{SERVER_HOST}:{SERVER_PORT}/health",
    "Timeout": "5s",
    "Interval": "5s",
    "DeregisterCriticalServiceAfter": "15s"
}


async def register():
    url = f"http://{CONSUL_HOST}:{CONSUL_PORT}/v1/agent/service/register"
    async with httpx.AsyncClient() as client:
        response = await client.put(
            url,
            headers={
                "contentType": "application/json"
            },
            json={
                "Name": SERVER_NAME,
                "ID": SERVER_NAME,
                "Tags": ["python", "http", "fastapi"],
                "Address": SERVER_HOST,
                "Port": SERVER_PORT,
                "Check": {
                    "HTTP": f"http://{SERVER_HOST}:{SERVER_PORT}/health",
                    "Timeout": "5s",
                    "Interval": "5s",
                    "DeregisterCriticalServiceAfter": "15s"
                }
            }
        )
        if response.status_code == 200:
            logger.info("注册成功")
        else:
            logger.info(f"注册失败：{response.status_code}")


async def deregister():
    url = f"http://{CONSUL_HOST}:{CONSUL_PORT}/v1/agent/service/deregister/{SERVER_NAME}"
    async with httpx.AsyncClient() as client:
        rsp = await client.put(
            url,
            headers={
                "contentType": "application/json"
            },
        )

    if rsp.status_code == 200:
        logger.info("注销成功")
    else:
        logger.info(f"注销失败：{rsp.status_code}")


if __name__ == "__main__":
    import asyncio

    asyncio.run(register())
