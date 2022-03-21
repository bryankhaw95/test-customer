from typing import Any, Dict, Optional, Set, Tuple

from django.db import models
from django.db.backends.base.base import BaseDatabaseWrapper
from django.db.models.query import QuerySet

class MigrationRecorder:
    class Migration(models.Model):
        app: Any = ...
        name: Any = ...
        applied: Any = ...
    connection: BaseDatabaseWrapper = ...
    def __init__(self, connection: BaseDatabaseWrapper) -> None: ...
    @property
    def migration_qs(self) -> QuerySet: ...
    def has_table(self) -> bool: ...
    def ensure_schema(self) -> None: ...
    def applied_migrations(self) -> Dict[Tuple[str, str], Migration]: ...
    def record_applied(self, app: str, name: str) -> None: ...
    def record_unapplied(self, app: str, name: str) -> None: ...
    def flush(self) -> None: ...
