import MessagesByCountry
import re
import ErrorCatch

VenzuelanCode = "+58"
ArgentinaCode = "+54"
ColombiaCode = "+57"
ChileanCode = "+56"
MexicanCode = "+52"

Message = ""

Errors = []

def NumberProcessing (Number):
  if Number.startswith(VenzuelanCode):
    if re.search(r"\+58\s?\d{10}", Number) == None:
      Errors.append("No es un numero venezolano valido")
    else:
      MessagesByCountry.MessageToSend = MessagesByCountry.VenezuelanMessage
  elif Number.startswith(ArgentinaCode):
    if re.search(r"^\+?54\s?9?\d{2}\s?\d{4}\s?\d{4}$", Number) == None:
      Errors.append("No es un numero argentino valido")
    else:
      MessagesByCountry.MessageToSend = MessagesByCountry.ArgentinaMessage
  elif Number.startswith(ColombiaCode):
    if re.search(r"^\+?57\s?\d{3}\s?\d{3}\s?\d{3}$", Number) == None:
      Errors.append("No es un numero colombiano valido")
    else:
      MessagesByCountry.MessageToSend = MessagesByCountry.ColombiaMessage 
  elif Number.startswith(ChileanCode):
    if re.search(r"^\+?56\s?\d{3}\s?\d{3}\s?\d{3}$", Number) == None:
      Errors.append("No es un numero chileno valido")
    else:
      MessagesByCountry.MessageToSend = MessagesByCountry.ChileanMessage
  elif Number.startswith(MexicanCode):
    if re.search(r"^\+?52\s?\d{3}\s?\d{3}\s?\d{4}$", Number) == None:
      Errors.append("No es un numero mexicano valido")
    else:
      MessagesByCountry.MessageToSend = MessagesByCountry.MexicanMessage
  else:
    if re.search(r"\+?\d{1,3}\s?\d{4,14}", Number) == None:
      Errors.append("No es un numero valido")
    else:
      MessagesByCountry.MessageToSend = MessagesByCountry.VenezuelanMessage
  ErrorCatch.ErrorCatched(Errors)