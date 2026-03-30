from repository.abstract.transaction_repo import TransactionRepo
from shared.result import Result
from aggregate import TransactionDetail
import pandas as pd
from shared.session import Session
from model import CategoryType, Transaction
from datetime import datetime

class TransactionRepoCSV(TransactionRepo):

    def __init__(self, csv_path: str):
        self.__csv_path: str = csv_path

    def get_by_category_id(self, category_id: int, category_df: pd.DataFrame) -> Result:
        df = pd.read_csv(self.__csv_path)
        target_df =  df[
            (df["category_id"] == category_id) &
            (df["user_id"] == Session.get_identity())
        ]

        if target_df.empty:
            return Result.fail("id not found")
        
        target_df = target_df.merge(
            category_df,
            left_on="category_id",
            right_on="id",
            how="inner",
            suffixes=("_t", "_c")
        )
        
        categories = []
        unformatted_categories = target_df.to_dict("records")

        for i in unformatted_categories:
            transaction_detail = TransactionDetail()
            transaction_detail.set_id(i["id_t"])
            transaction_detail.set_category_id(i["category_id"])
            transaction_detail.set_user_id(i["user_id_t"])
            transaction_detail.set_cost(i["cost"])
            transaction_detail.set_description(i["description"])
            transaction_detail.set_created_at(i["created_at"])
            transaction_detail.set_cateory_name(i["name"])
            transaction_detail.set_category_type(CategoryType(i["type"]))
            transaction_detail.set_date(i["date"])

            categories.append(transaction_detail)

        return Result.success(categories)
    
    def is_existed_by_category_id(self, category_id: int) -> bool:
        df = pd.read_csv(self.__csv_path)
        df = df[df["category_id"] == category_id]

        if df.empty:
            return False
        return True
    
    def add_transaction(self, new_transaction: Transaction) -> Result:
        df = pd.read_csv(self.__csv_path)

        new_item = pd.DataFrame([{
            "id": new_transaction.get_id(),
            "category_id": new_transaction.get_category_id(),
            "user_id": new_transaction.get_user_id(),
            "cost": new_transaction.get_cost(),
            "description": new_transaction.get_description(),
            "created_at": new_transaction.get_created_at(),
            "date": new_transaction.get_date()
        }])

        df = pd.concat([df, new_item], ignore_index=True)
        df.to_csv(self.__csv_path, index=False)

        return Result.success(True)
    
    def show_all_by_user_id(self, user_id: int, category_df: pd.DataFrame) -> Result:
        df = pd.read_csv(self.__csv_path)
        target_df = df[
            df["user_id"] == user_id
        ]

        if target_df.empty:
            return Result.fail("No category created")
        
        target_df = target_df.merge(
            category_df,
            left_on="category_id",
            right_on="id",
            how="inner",
            suffixes=("_t", "_c")
        )

        unformatted_transaction = target_df.to_dict("records")
        transactions = []
        for i in unformatted_transaction:
            transaction_detail = TransactionDetail()
            transaction_detail.set_id(i["id_t"])
            transaction_detail.set_category_id(i["category_id"])
            transaction_detail.set_user_id(i["user_id_t"])
            transaction_detail.set_cost(i["cost"])
            transaction_detail.set_description(i["description"])
            transaction_detail.set_created_at(i["created_at"])
            transaction_detail.set_cateory_name(i["name"])
            transaction_detail.set_category_type(CategoryType(i["type"]))
            transaction_detail.set_date(i["date"])

            transactions.append(transaction_detail)

        return Result.success(transactions)
    
    def delete(self, id, user_id):
        df = pd.read_csv(self.__csv_path)
        target_df = df[
            (df["id"] == id) &
            (df["user_id"] == user_id)
        ]

        if target_df.empty:
            return Result.fail("ID not found")
        
        df = df.drop(target_df.index)
        df.to_csv(self.__csv_path, index=False)
        return Result.success("Deleted Transaction")
    
    def edit(self, new_transaction: Transaction):
        df = pd.read_csv(self.__csv_path)
        condition = (
            (df["id"] == new_transaction.get_id()) &
            (df["user_id"] == new_transaction.get_user_id())
        )
        target_df = df[condition]

        if target_df.empty:
            return Result.fail("ID not found")
        
        df.loc[condition, "category_id"] = new_transaction.get_category_id()
        df.loc[condition, "cost"] = new_transaction.get_cost()
        df.loc[condition, "date"] = new_transaction.get_date()
        df.loc[condition, "description"] = new_transaction.get_description()

        df.to_csv(self.__csv_path, index=False)
        return Result.success("Updated Transaction")
    
    def get_by_id(self, id, user_id):
        df = pd.read_csv(self.__csv_path)
        condition = (
            (df["id"] == id) &
            (df["user_id"] == user_id)
        )
        target_df = df[condition]

        if target_df.empty:
            return Result.fail("ID not found")
        
        target_df = target_df.iloc[0]
        
        transaction = Transaction()
        transaction.set_id(target_df["id"])
        transaction.set_category_id(target_df["category_id"])
        transaction.set_user_id(target_df["user_id"])
        transaction.set_cost(target_df["cost"])
        transaction.set_date(target_df["date"])
        transaction.set_created_at(target_df["created_at"])
        transaction.set_description(target_df["description"])

        return Result.success(transaction)