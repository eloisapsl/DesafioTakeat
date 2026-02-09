from enum import Enum
from pydantic import BaseModel, Field

## Modelos para representação de objetos da aplicação.
class Categories(str, Enum):
    PEDIDO_CARDAPIO = "PEDIDO_CARDAPIO"
    STATUS_ENTREGA = "STATUS_ENTREGA"
    RECLAMACAO = "RECLAMACAO"
    ELOGIO = "ELOGIO"
    OUTROS = "OUTROS"

class MensagemRequest(BaseModel):
    message: str

class MensagemResponse(BaseModel):
    category: Categories
    confidence: float = Field(ge=0, le=1)