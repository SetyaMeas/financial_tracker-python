from model import Transaction
from shared import *
from repository import TransactionRepo, CategoryRepo
from utils import Formatter, InputValidator
from aggregate import TransactionDetail
from prettytable import PrettyTable
from screen.category_screen import CategoryScreen
from datetime import datetime

class TransactionScreen:
    def __init__(self, transaction_repo: TransactionRepo, category_repo: CategoryRepo, category_screen: CategoryScreen):
        self.__transaction_repo: TransactionRepo = transaction_repo
        self.__category_repo: CategoryRepo = category_repo
        self.__category_screen = category_screen
        self.__datetime_format = "%Y-%m-%d"

    def show_transactions(self) -> None:
        transcations_result = self.__transaction_repo.show_all_by_user_id(
            Session.get_identity(),
            self.__category_repo.get_df()
        )
        if not transcations_result.is_success():
            print(Formatter.result(transcations_result.get_error_msg()))
        else:
            table = PrettyTable()
            table.field_names = ["ID", "CATEGORY", "COST", "TYPE", "DESCRIPTION", "DATE", "CREATED AT"]

            transcations: list[TransactionDetail] = transcations_result.get_value()
            for i in transcations:
                table.add_row([
                    i.get_id(),
                    i.get_category_name(),
                    f"$ {i.get_cost()}",
                    i.get_category_type().value,
                    i.get_description(),
                    i.get_date(),
                    i.get_created_at(),
                ])

            print()
            print(Formatter.section_seperator("All Transactions"))
            print(table)

    def add_transaction(self) -> None:
        transaction = Transaction()

        self.__category_screen.show_all()
        while True:
            category_id_input = InputValidator.is_int(
                input(Formatter.input("Enter category id: "))
            )
            if category_id_input.is_success():
                existed_category = self.__category_repo.get_by_id(
                    category_id_input.get_value(), 
                    Session.get_identity()
                    )
                
                if existed_category.is_success():
                    transaction.set_category_id(category_id_input.get_value())
                    break
                else:
                    print(Formatter.error(existed_category.get_error_msg()))
            else:
                print(Formatter.error(category_id_input.get_error_msg()))

        while True:
            cost_result = InputValidator.is_float_and_greater_than_zero(
                input(Formatter.input("Enter cost($): "))
            )
            if cost_result.is_success():
                transaction.set_cost(cost_result.get_value())
                break
            print(Formatter.error(cost_result.get_error_msg()))

        while True:
            date_input = InputValidator.valid_date(input(
                Formatter.input("Enter date (YYYY-MM-DD): ")
            ), self.__datetime_format)
            if date_input.is_success():
                transaction.set_date(date_input.get_value())
                break
            print(date_input.get_error_msg())

        description = input(Formatter.input("Enter description: "))

        transaction.set_description(description)
        transaction.set_user_id(Session.get_identity())
        transaction.set_id(EntityIDManager.get_and_update_transaction_id())
        transaction.set_created_at(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        new = self.__transaction_repo.add_transaction(transaction)
        if new.is_success():
            print(Formatter.success("Created Transaction"))
        else:
            print(Formatter.error(new.get_error_msg()))

    def delete(self) -> None:
        while True:
            id_input = InputValidator.is_int(input(
                Formatter.input("Enter id: ")
            ))
            if id_input.is_success():
                delete_transaction = self.__transaction_repo.delete(id_input.get_value(), Session.get_identity())
                if delete_transaction.is_success():
                    print(Formatter.success(delete_transaction.get_value()))
                else:
                    print(Formatter.error(delete_transaction.get_error_msg()))
                break
            print(Formatter.error(id_input.get_error_msg()))

    def edit(self):
        new_transaction = Transaction()

        while True:
            id_input = InputValidator.is_int(input(
                Formatter.input("Enter id: ")
            ))
            if id_input.is_success():
                existed_transaction = self.__transaction_repo.get_by_id(id_input.get_value(), Session.get_identity())
                if existed_transaction.is_success():
                    transaction: Transaction = existed_transaction.get_value()
                    new_transaction.set_id(transaction.get_id())
                    new_transaction.set_user_id(transaction.get_user_id())
                    new_transaction.set_created_at(transaction.get_created_at())
                    break
                else:
                    print(Formatter.error(existed_transaction.get_error_msg()))
                    return
            else:
                print(Formatter.error(id_input.get_error_msg()))

        self.__category_screen.show_all()
        while True:
            category_id_input = InputValidator.is_int(
                input(Formatter.input("Enter category id: "))
            )
            if category_id_input.is_success():
                existed_category = self.__category_repo.get_by_id(
                    category_id_input.get_value(), 
                    Session.get_identity()
                    )
                
                if existed_category.is_success():
                    new_transaction.set_category_id(category_id_input.get_value())
                    break
                else:
                    print(Formatter.error(existed_category.get_error_msg()))
            else:
                print(Formatter.error(category_id_input.get_error_msg()))

        while True:
            cost_result = InputValidator.is_float_and_greater_than_zero(
                input(Formatter.input("Enter cost($): "))
            )
            if cost_result.is_success():
                new_transaction.set_cost(cost_result.get_value())
                break
            print(Formatter.error(cost_result.get_error_msg()))

        while True:
            date_input = InputValidator.valid_date(input(
                Formatter.input("Enter date (YYYY-MM-DD): ")
            ), self.__datetime_format)
            if date_input.is_success():
                new_transaction.set_date(date_input.get_value())
                break
            print(date_input.get_error_msg())

        description = input(Formatter.input("Enter description: "))
        new_transaction.set_description(description)

        edit_transaction = self.__transaction_repo.edit(new_transaction)
        if edit_transaction.is_success():
            print(Formatter.success("Updated Transaction"))
        else:
            print(Formatter.error(edit_transaction.get_error_msg()))

    def run(self):
        while True:
            print()
            print(Formatter.section_seperator("Trasaction Management"))
            print("1. Add Transaction")
            print("2. Delete Transaction")
            print("3. Edit Transaction")
            print("4. View Transaction")
            print("5. Exit")
            print()

            option = Formatter.option_picker(1, 5)
            if option == 1:
                self.add_transaction()
            elif option == 2:
                self.delete()
            elif option == 3:
                self.edit()
            elif option == 4:
                self.show_transactions()
            elif option == 5:
                break