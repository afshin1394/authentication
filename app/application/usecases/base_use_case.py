from abc import abstractmethod,ABC
from typing import Any


class BaseUseCase(ABC):
    @abstractmethod
    async def execute(self, **kwargs)->Any:
        pass
