from dependency_injector.wiring import inject, Provide
from llms.application.ollama_service import OllamaService
from llms.domain.ollama_schema import PromptRequest, PromptResponse


class TranslationService:
    @inject
    def __init__(
        self,
        ollama_service: OllamaService = Provide["ollama_service"],
    ):
        self.ollama_service = ollama_service

    def translate(self, prompt: PromptRequest) -> PromptResponse:
        return self.ollama_service.chat(prompt)
