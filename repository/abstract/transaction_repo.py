from abc import ABC, abstractclassmethod
from shared.result import Result
from pandas import DataFrame
from model import Transaction

class TransactionRepo(ABC):
    @abstractclassmethod
    def get_by_category_id(self, category_id: int, category_df: DataFrame) -> Result:
        pass

    @abstractclassmethod
    def is_existed_by_category_id(self, category_id: int) -> bool:
        pass

    @abstractclassmethod
    def add_transaction(self, new_transaction: Transaction) -> Result:
        pass

    @abstractclassmethod
    def show_all_by_user_id(self, user_id: int, category_df: DataFrame) -> Result:
        pass

    @abstractclassmethod
    def delete(self, id: int, user_id: int) -> Result:
        pass

    @abstractclassmethod
    def edit(self, new_transaction: Transaction) -> Result:
        pass

    @abstractclassmethod
    def get_by_id(self, id: int, user_id: int) -> Result:
        pass