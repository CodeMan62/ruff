from collections.abc import Callable, Sequence
from contextvars import Context
from typing import Any, Final

from . import futures

__all__ = ()

# asyncio defines 'isfuture()' in base_futures.py and re-imports it in futures.py
# but it leads to circular import error in pytype tool.
# That's why the import order is reversed.
from .futures import isfuture as isfuture

_PENDING: Final = "PENDING"  # undocumented
_CANCELLED: Final = "CANCELLED"  # undocumented
_FINISHED: Final = "FINISHED"  # undocumented

def _format_callbacks(cb: Sequence[tuple[Callable[[futures.Future[Any]], None], Context]]) -> str:  # undocumented
    """helper function for Future.__repr__"""

def _future_repr_info(future: futures.Future[Any]) -> list[str]:  # undocumented
    """helper function for Future.__repr__"""
