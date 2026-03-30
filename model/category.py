from model.category_type import CategoryType

class Category:
    def __init__(self, id: int, user_id: int, type: CategoryType, name: str) -> None:
        self.__id: int = id
        self.__user_id: int = user_id
        self.__type: str = type  # "INCOME" or "EXPENSE"
        self.__name: str = name

    def get_id(self) -> int:
        return self.__id

    def get_type(self) -> CategoryType:
        return self.__type

    def get_name(self) -> str:
        return self.__name

    def set_type(self, category_type: CategoryType) -> None:
        self.__type = category_type

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_user_id(self) -> int:
        return self.__user_id
    
    def set_user_id(self, user_id: int) -> None:
        self.__user_id = user_id

    def set_id(self, id: int) -> None:
        self.__id = id

    @staticmethod
    def get_blank_object() -> Category:
        return Category(0, 0, CategoryType.INCOME, "")
    
    def to_string(self) -> str:
        return f"Category(id={self.__id}, user_id={self.__user_id}, type={self.__type}, name='{self.__name}')"