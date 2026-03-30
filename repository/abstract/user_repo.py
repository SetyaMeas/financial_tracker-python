from abc import ABC, abstractclassmethod
from shared.result import Result
from model.user import User

class UserRepo(ABC):
    @abstractclassmethod
    def create(self, user: User) -> Result:
        pass

    @abstractclassmethod
    def find_by_email(self, email: str) -> Result:
        pass
