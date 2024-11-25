from crewai.tools import tool

@tool ("Multiplication Tool")
def multiplicationTool ( primeiro_numero : int, segundo_numero : int) -> str:

resultado = primeiro_numero * segundo_numero

return f"""O resultado da multiplicação de
{ primeiro_numero } e { segundo_numero } é { resultado }. """

