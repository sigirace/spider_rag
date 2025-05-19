from typing import Annotated
from fastapi import Depends, Query
from fastmcp import Context
from server import mcp
from tools.application.calculate import CalculateService
from tools.interface.dto.header import CustomHeader
from tools.interface.dto.response import ToolResponse
from log.log_config import get_logger
from utils.http import get_bearer_token


logger = get_logger()


DESCRIPTION = """두 수를 더한 값을 반환합니다."""


@mcp.tool(name="get_sum", description=DESCRIPTION)
async def get_sum(
    a: Annotated[int, Query(description="첫 번째 정수")],
    b: Annotated[int, Query(description="두 번째 정수")],
    ctx: Context,
) -> ToolResponse:

    token = get_bearer_token(ctx)
    logger.info(f"[MCP TOOL] get_sum called for {a} + {b}, headers: {token}")
    result = CalculateService().get_sum(a, b)

    return ToolResponse(response=result)
