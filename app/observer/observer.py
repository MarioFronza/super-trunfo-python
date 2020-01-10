from abc import ABC, abstractmethod
from app.models.player import Player


class Observer(ABC):
    @abstractmethod
    def winner(self, player: Player) -> None:
        pass
