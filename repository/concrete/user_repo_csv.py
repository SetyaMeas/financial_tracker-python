from repository.abstract.user_repo import UserRepo
import pandas as pd
from shared.result import Result
from model.user import User
from shared.entity_id_manager import EntityIDManager

class UserRepoCSV(UserRepo):

    def __init__(self, csv_path: str):
        self.__csv_path = csv_path

    def create(self, user: User) -> Result:
        existed_user = self.find_by_email(user.get_email())
        if existed_user.is_success():
            return Result.fail("email already existed")

        # user.set_id(EntityIDManager.get_and_update_user_id())
        new_user = pd.DataFrame([{
            "id": user.get_id(),
            "email": user.get_email(),
            "pwd": user.get_pwd()
        }])

        df = pd.read_csv(self.__csv_path)
        df = pd.concat([df, new_user], ignore_index=True)
        df.to_csv(self.__csv_path, index=False)

        return Result.success(user)
    
    def find_by_email(self, email: str) -> Result:
        df = pd.read_csv(self.__csv_path)
        user = df.loc[
            df["email"] == email
        ]

        if user.empty:
            return Result.fail("email not found")
        
        user = user.iloc[0]
        return Result.success(
            User(user["id"], user["email"], user["pwd"])
        )