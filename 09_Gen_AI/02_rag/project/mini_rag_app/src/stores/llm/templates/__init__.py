"""
Prompt templates package.

Structure:
- locales/<lang>/<template>.py  (e.g. locales/en/rag.py)
- template_parser.py            (loads templates by language)
"""

from .template_parser import TemplateParser

__all__ = ["TemplateParser"]

