import pandas as pd
from model.category import Category
from abc import ABC, abstractclassmethod
from shared.result import Result
from pandas import DataFrame

class CategoryRepo(ABC):
    @abstractclassmethod
    def create(self, category: Category) -> Result:
        pass

    @abstractclassmethod
    def find_by_name(self, name: str, user_id: int) -> Result:
        pass

    @abstractclassmethod
    def find_by_user_id(self, user_id: int) -> Result:
        pass

    @abstractclassmethod
    def delete(self, id: int, user_id: int) -> Result:
        pass

    @abstractclassmethod
    def update(self, new_category: Category) -> Result:
        pass

    @abstractclassmethod
    def get_df(self) -> DataFrame:
        pass

    @abstractclassmethod
    def get_by_id(self, category_id: int, user_id: int) -> Result:
        pass