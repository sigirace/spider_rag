# containers.py
from dependency_injector import containers, providers
from llms.application.ollama_service import OllamaService
from llms.infra.ollama_api import OllamaLLM
from tools.application.translation_service import TranslationService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "llms.application.ollama_service",
            "tools.application.translation_service",
        ],
    )

    ollama_llm = providers.Singleton(OllamaLLM)
    ollama_service = providers.Factory(
        OllamaService,
        llm=ollama_llm,
    )
    translation_service = providers.Factory(
        TranslationService,
        ollama_service=ollama_service,
    )
