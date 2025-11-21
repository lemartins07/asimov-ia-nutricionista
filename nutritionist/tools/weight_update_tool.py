from langchain.tools import BaseTool
from nutritionist.repositories import UserRepository, WeightHistoryRepository


class WeightUpdateTool(BaseTool):
    name: str = "weight_update"
    description: str = (
        "Use esta ferramenta para registrar o peso de um usuário. "
        "Entrada: telegram_id do usuário e weight_kg."
    )

    def __init__(self):
        super().__init__()
        self._user_repository = UserRepository()
        self._weight_history_repository = WeightHistoryRepository()

    def _run(self, telegram_id: int, weight_kg: float) -> str:
        try:
            user = self._user_repository.get_user_by_telegram_id(telegram_id)
            if not user:
                return f"Usuário com telegram_id {telegram_id} não encontrado."

            self._weight_history_repository.add_weight_entry(user.id, weight_kg)
            return f"Peso de {weight_kg} kg registrado com sucesso para o usuário {user.name}."
        except Exception as e:
            return f"Ocorreu um erro ao registrar o peso: {str(e)}"

    async def _arun(self, weight_kg: float) -> str:
        raise NotImplementedError("Execução assíncrona não suportada.")
