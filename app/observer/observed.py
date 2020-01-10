from abc import ABC, abstractmethod
from app.observer.observer import Observer
from app.models.player import Player


class Observed(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify_winner(self, player: Player) -> None:
        pass
