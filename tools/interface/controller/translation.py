from typing import Annotated
from fastapi import Query
from fastmcp import Context
from llms.domain.ollama_schema import PromptRequest, PromptResponse
from server import mcp
from tools.application.translation_service import TranslationService
from tools.interface.dto.header import CustomHeader
from tools.interface.dto.response import ToolResponse
from log.log_config import get_logger
from dependency_injector.wiring import inject

from utils.http import get_bearer_token

logger = get_logger()

DESCRIPTION = """문장을 요청한 언어로 번역하여 반환합니다."""

PROMPT = """당신은 사용자가 말하는 문장을 {target}로 번역하는 번역 전문 에이전트입니다.
사용자가 제공하는 문장의 번역 결과만을 1회 작성하세요.

사용자가 제공하는 문장

{text}

사용자가 제공하는 문장의 번역 결과:
"""


@inject
@mcp.tool(
    name="translate",
    description=DESCRIPTION,
)
async def translate(
    text: Annotated[str, Query(description="번역할 문장")],
    target: Annotated[str, Query(description="번역할 언어")],
    ctx: Context,
) -> ToolResponse:

    token = get_bearer_token(ctx)
    logger.info(f"[MCP TOOL] translate called headers: {token}")
    from containers import Container

    translation_service: TranslationService = Container.translation_service()
    prompt = PROMPT.format(text=text, target=target)
    result = translation_service.translate(PromptRequest(prompt=prompt))

    return ToolResponse(
        response=result.response,
    )
