from repository.concrete.user_repo_csv import UserRepoCSV
from repository.concrete.category_repo_csv import CategoryRepoCSV
from repository.concrete.transaction_repo_csv import TransactionRepoCSV

from shared.entity_id_manager import EntityIDManager
# from shared.session import Session
from shared import Session
from model.user import User
from model.category import Category
from model.category_type import CategoryType

user_repo = UserRepoCSV("./data/user.csv")
trans_repo = TransactionRepoCSV("./data/transaction.csv")
category_repo = CategoryRepoCSV("./data/category.csv", trans_repo)

EntityIDManager.set_csv_path("./data/entity_id.csv")

Session.login(12)

update = category_repo.update(Category(
    1, 1, CategoryType.EXPENSE, "second cate"
))

if not update.is_success():
    print(update.get_error_msg())

# a = trans_repo.get_by_category_id(1, category_repo.get_df())

# if a.is_success():
#     b = a.get_value()
#     for i in b:
#         print(i.get_id())
#         print(i.get_category_id())
#         print(i.get_user_id())
#         print(i.get_cost())
#         print(i.get_description())
#         print(i.get_created_at())
#         print(i.get_category_name())
#         print(i.get_category_type().value)
# else:
#     print(a.get_error_msg())

