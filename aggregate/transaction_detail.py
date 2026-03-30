from model.category_type import CategoryType
from model.transaction import Transaction
import datetime

class TransactionDetail(Transaction):

    __category_name: str = ""
    __category_type: CategoryType = CategoryType.INCOME

    def get_category_name(self) -> str:
        return self.__category_name
    
    def get_category_type(self) -> CategoryType:
        return self.__category_type
    
    def set_cateory_name(self, name: str) -> None:
        self.__category_name = name

    def set_category_type(self, type: CategoryType) -> None:
        self.__category_type = type

