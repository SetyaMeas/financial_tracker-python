import pandas as pd

class EntityIDManager:
    __csv_path: str = ""

    @classmethod
    def set_csv_path(cls, csv_path: str) -> None:
        cls.__csv_path = csv_path

    @classmethod
    def get_and_update_user_id(cls) -> int:
        df = pd.read_csv(cls.__csv_path)
        user_id = df.loc[
            df["name"] == "user",
            "available_id"
        ].iloc[0]

        df.loc[df["name"] == "user", "available_id"] = user_id + 1
        df.to_csv(cls.__csv_path, index=False)

        return user_id
    
    @classmethod
    def get_and_update_category_id(cls) -> int:
        df = pd.read_csv(cls.__csv_path)
        category_id = df.loc[
            df["name"] == "category",
            "available_id"
        ].iloc[0]

        df.loc[df["name"] == "category", "available_id"] = category_id + 1
        df.to_csv(cls.__csv_path, index=False)

        return category_id
    
    @classmethod
    def get_and_update_transaction_id(cls) -> int:
        df = pd.read_csv(cls.__csv_path)
        transaction_id = df.loc[
            df["name"] == "transaction",
            "available_id"
        ].iloc[0]

        df.loc[df["name"] == "transaction", "available_id"] = transaction_id + 1
        df.to_csv(cls.__csv_path, index=False)

        return transaction_id
        