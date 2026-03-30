from repository.abstract.category_repo import CategoryRepo
from model.category import Category
from shared.result import Result
import pandas as pd
from repository.abstract.transaction_repo import TransactionRepo
from model import CategoryType

class CategoryRepoCSV(CategoryRepo):
    __csv_path: str = ""

    def __init__(self, csv_path: str, transaction_repo: TransactionRepo):
        self.__csv_path = csv_path
        self.__transaction_repo = transaction_repo

    def create(self, category: Category) -> Result:
        df = pd.read_csv(self.__csv_path)
        existed_category = df[
            (df["name"] == category.get_name()) &
            (df["user_id"] == category.get_user_id()) &
            (df["type"] == category.get_type().value)
        ]

        if not existed_category.empty:
            return Result.fail("category name already existed")

        # category.set_id(EntityIDManager.get_and_update_category_id())

        new_category = pd.DataFrame([{
            "id": category.get_id(),
            "name": category.get_name(),
            "user_id": category.get_user_id(),
            "type": category.get_type().value
        }])

        df = pd.concat([df, new_category], ignore_index=True)
        df.to_csv(self.__csv_path, index=False)

        return Result.success(category)
    
    def delete(self, id: int, user_id: int) -> Result:
        df = pd.read_csv(self.__csv_path)
        target = df[(df["id"] == id) & (df["user_id"] == user_id)]

        if target.empty:
            return Result.fail("id not found")
        
        # check if there are any transaction with these category id
        existed_transactions = self.__transaction_repo.is_existed_by_category_id(id)
        if existed_transactions:
            return Result.fail("can not delete this category")

        df = df.drop(target.index)
        df.to_csv(self.__csv_path, index=False)
        return Result.success("deleted category")
    
    def update(self, new_category: Category) -> Result:
        # is category id exisetd for this user?
        existed_id = self.get_by_id(new_category.get_id(), new_category.get_user_id())
        if not existed_id.is_success():
            return Result.fail("id not found")

        # is name existed for this user in another category id and the same type?
        existed_name = self.find_by_name(new_category.get_name(), new_category.get_user_id())
        if existed_name.is_success():
            categories = existed_name.get_value()
            for i in categories:
                if new_category.get_type() == i.get_type() and new_category.get_id() != i.get_id():
                    return Result.fail("name already existed")
                
        df = pd.read_csv(self.__csv_path)
        condition = (
            (df["id"] == new_category.get_id())
        )

        df.loc[condition, "name"] = new_category.get_name()
        df.loc[condition, "type"] = new_category.get_type().value
        df.to_csv(self.__csv_path, index=False)

        return Result.success(new_category)
        
    def find_by_name(self, name: str, user_id) -> Result:
        df = pd.read_csv(self.__csv_path)
        df = df[
            (df["name"] == name) &
            (df["user_id"] == user_id)
        ]

        if df.empty:
            return Result.fail("name not found")
        
        return Result.success(Category(
            i["id"],
            i["user_id"],
            CategoryType(i["type"]),
            i["name"]
        ) for i in df.to_dict("records"))
    
    def find_by_user_id(self, user_id: int) -> Result:
        df = pd.read_csv(self.__csv_path)
        df = df[
            df["user_id"] == user_id
        ]

        if df.empty:
            return Result.fail("user id not found")

        return Result.success(
            Category(i["id"], i["user_id"], CategoryType(i["type"]), i["name"]) 
            for i in df.to_dict("records")
        )
    
    def get_df(self) -> pd.DataFrame:
        return pd.read_csv(self.__csv_path)
    
    def get_by_id(self, category_id, user_id) -> Result:
        df = pd.read_csv(self.__csv_path)
        df = df[
            (df["id"] == category_id) &
            (df["user_id"] == user_id)
        ]

        if df.empty:
            return Result.fail("id not found")
        
        target_df = df.iloc[0]
        return Result.success(Category(
            target_df["id"],
            target_df["user_id"],
            CategoryType(target_df["type"]),
            target_df["name"]
        ))
        