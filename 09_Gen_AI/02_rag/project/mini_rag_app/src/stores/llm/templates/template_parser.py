from __future__ import annotations

import importlib
from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass(frozen=True)
class LoadedTemplate:
    language: str
    name: str
    prompts: Dict[str, Any]


class TemplateParser:
    """
    Loads prompt templates from src/stores/llm/templates/locales/<lang>/<name>.py

    Each template module should expose a dict named PROMPTS.
    """

    def __init__(self, default_language: str = "en"):
        self.default_language = default_language

    def load(self, name: str, language: Optional[str] = None) -> LoadedTemplate:
        lang = (language or self.default_language or "en").strip().lower()
        module_path = f"stores.llm.templates.locales.{lang}.{name}"

        try:
            module = importlib.import_module(module_path)
        except ModuleNotFoundError:
            if lang != self.default_language:
                # Fallback to default language if requested language missing.
                return self.load(name=name, language=self.default_language)
            raise

        prompts = getattr(module, "PROMPTS", None)
        if not isinstance(prompts, dict):
            raise ValueError(f"Template module '{module_path}' must define dict PROMPTS")

        return LoadedTemplate(language=lang, name=name, prompts=prompts)

