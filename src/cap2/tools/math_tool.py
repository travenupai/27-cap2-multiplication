from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Description of the argument.")

class MultiplicationTool(BaseTool):
    name: str = "Ferramenta de Multiplicação"
    description: str = (
        "Ütil para quando você precisa multiplicar dois números."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, primeiro_numerot: int, segundo_numero: int) -> str:
        resultado = primeiro_numerot * segundo_numero
        return f"""Ö resultado da multiplicação de {primeiro_numerot} 
        e {segundo_numero} é {resultado}."""