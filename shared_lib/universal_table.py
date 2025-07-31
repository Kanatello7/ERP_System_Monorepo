# shared_lib/universal_table.py
from __future__ import annotations
from typing import Any, Dict, Iterable, List, Literal
from pydantic import BaseModel, Field

CellType = Literal["string", "number", "date", "bool"]  


class Column(BaseModel):
    key: str = Field(..., description="Уникальный идентификатор колонки (совпадает с полем модели)")
    title: str = Field(..., description="Человекочитаемый заголовок для UI")
    type: CellType = "string"
    width: int | None = Field(default=None, description="Необязательная ширина в пикселях")


class Row(BaseModel):
    values: Dict[str, Any]

class UniversalTable(BaseModel):

    columns: List[Column]
    rows: List[Row]

    @classmethod
    def from_instances(
        cls,
        instances: Iterable[Any],
        schema: dict[str, tuple[str, CellType]],
    ) -> "UniversalTable":
        """
        schema — Ordered‑dict‑like mapping:
            field_name -> (title, type)
        """
        columns = [
            Column(key=field, title=title, type=cell_type)
            for field, (title, cell_type) in schema.items()
        ]
        rows = [
            Row(values={field: getattr(obj, field) for field in schema})
            for obj in instances
        ]
        return cls(columns=columns, rows=rows)
