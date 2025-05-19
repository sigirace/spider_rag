from log.log_config import get_logger
from containers import Container
from server import mcp

logger = get_logger()

container = Container()
container.wire(
    modules=[
        "tools.interface.controller.calculate",
        "tools.interface.controller.translation",
    ]
)

# 실행
if __name__ == "__main__":
    logger.info("[MCP] MCP 서버 시작")
    mcp.run(host="0.0.0.0", port=8001, transport="sse")
