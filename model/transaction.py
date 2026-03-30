import datetime

class Transaction:
    # def __init__(
    #     self,
    #     transaction_id: int,
    #     category_id: int,
    #     user_id: int,
    #     cost: float,
    #     description: str,
    #     created_at: datetime
    # ) -> None:
    #     self.__id: int = transaction_id
    #     self.__category_id: int = category_id
    #     self.__cost: float = cost
    #     self.__description: str = description
    #     self.__created_at: datetime = created_at
    #     self.__user_id =user_id

    __id: int = 0
    __category_id: int = 0
    __cost: float = 0.0
    __description: str = ""
    __created_at: str = ""
    __user_id: int = 0
    __date: str = ""

    def get_id(self) -> int:
        return self.__id

    def get_category_id(self) -> int:
        return self.__category_id

    def get_cost(self) -> float:
        return self.__cost

    def get_description(self) -> str:
        return self.__description

    def get_created_at(self) -> str:
        return self.__created_at
    
    def get_user_id(self) -> int:
        return self.__user_id
    
    def get_date(self) -> str:
        return self.__date
    
    def set_date(self, date: str) -> None:
        self.__date = date

    def set_category_id(self, category_id: int) -> None:
        self.__category_id = category_id

    def set_cost(self, cost: float) -> None:
        self.__cost = cost

    def set_description(self, description: str) -> None:
        self.__description = description

    def set_created_at(self, created_at: str) -> None:
        self.__created_at = created_at

    def set_id(self, id: int) -> None:
        self.__id = id

    def set_user_id(self, user_id: int) -> None:
        self.__user_id = user_id