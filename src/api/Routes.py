from fastapi import APIRouter, HTTPException
from models.Schemas import MensagemRequest, MensagemResponse
from services.ClassificationService import classify_message
router = APIRouter()

@router.post("/classify", response_model=MensagemResponse, description="Este endpoint classifica uma mensagem do usuário em 5 categorias: \n- **PEDIDO_CARDAPIO** - Para pedidos ou dúvidas sobre o cardápio \n- **STATUS_ENTREGA** - Para perguntas sobre status de entrega \n - **RECLAMACAO** - Para reclamações ou problemas \n - **ELOGIO** - Para elogios e feedbacks positivos \n - **OUTROS** - Para conversas gerais ou não categorizáveis", tags=["classify"], summary="Classificar uma mensagem do usuário")
def classify(message: MensagemRequest):
    if message is None:
        raise HTTPException(
        status_code=400,
        detail="Bad Request"
    )
    return classify_message(message)