from repository import CategoryRepo
from prettytable import PrettyTable
from shared import Result, Session, EntityIDManager
from utils import Formatter, CategoryScreenValidator
from model import Category

class CategoryScreen:
    def __init__(self, category_repo: CategoryRepo):
        self.__category_repo: CategoryRepo = category_repo

    def show_all(self) -> None:
        categories = self.__category_repo.find_by_user_id(Session.get_identity())
        if not categories.is_success():
            print(Formatter.result("No Category Created"))
            return

        table = PrettyTable()
        table.field_names = ["ID", "NAME", "TYPE"]

        for i in categories.get_value():
            table.add_row([
                i.get_id(),
                i.get_name(),
                i.get_type().value
            ])

        print()
        print(Formatter.section_seperator("All Categories"))
        print(table)

    def create(self) -> None:
        category = Category.get_blank_object()

        while True:
            category_input = CategoryScreenValidator.validate_name(
                input(Formatter.input("Enter name: "))
            )
            if category_input.is_success():
                category.set_name(category_input.get_value())
                break

            print(Formatter.error(category_input.get_error_msg()))

        while True:
            type_input = CategoryScreenValidator.validate_type(
                input(Formatter.input("Enter type(INCOME/EXPENSE): "))
            )
            if type_input.is_success():
                category.set_type(type_input.get_value())
                break

            print(Formatter.error(type_input.get_error_msg()))

        category.set_id(EntityIDManager.get_and_update_category_id())
        category.set_user_id(Session.get_identity())

        create_new = self.__category_repo.create(category)
        if create_new.is_success():
            print(Formatter.success("Created New Category"))
        else:
            print(Formatter.error(create_new.get_error_msg()))

    def delete(self) -> None:
        id = 0
        while True:
            id_input = CategoryScreenValidator.validate_id(input(
                Formatter.input("Enter ID: ")
            ))
            if id_input.is_success():
                id = id_input.get_value()
                break
            else:
                print(Formatter.error(id_input.get_error_msg()))

        delete_category = self.__category_repo.delete(id, Session.get_identity())
        if delete_category.is_success():
            print(Formatter.success("Deleted Category"))
        else:
            print(Formatter.error(delete_category.get_error_msg()))

    def update(self) -> None:
        id = 0
        while True:
            id_input = CategoryScreenValidator.validate_id(input(
                Formatter.input("Enter ID: ")
            ))
            if id_input.is_success():
                id = id_input.get_value()
                break
            else:
                print(Formatter.error(id_input.get_error_msg()))

        existing_category = self.__category_repo.get_by_id(id, Session.get_identity())
        if not existing_category.is_success():
            print(Formatter.error(existing_category.get_error_msg()))
        else:
            category: Category = existing_category.get_value()

            while True:
                name_input = CategoryScreenValidator.validate_name(input(
                    Formatter.input("Enter name: ")
                ))
                if name_input.is_success():
                    category.set_name(name_input.get_value())
                    break
                print(Formatter.error(name_input.get_error_msg()))

            while True:
                type_input = CategoryScreenValidator.validate_type(
                    input(Formatter.input("Enter type(INCOME/EXPENSE): "))
                )
                if type_input.is_success():
                    category.set_type(type_input.get_value())
                    break
                print(Formatter.error(type_input.get_error_msg()))

            update_category = self.__category_repo.update(category)
            if update_category.is_success():
                print(Formatter.success("Updated Category"))
            else:
                print(Formatter.error(update_category.get_error_msg()))

    def run(self):
        while True:
            print()
            print(Formatter.section_seperator("Category Management"))
            print("1. Show All")
            print("2. Create")
            print("3. Delete")
            print("4. Update")
            print("5. Exit")
            print()

            option = Formatter.option_picker(1, 5)

            if option == 1:
                self.show_all()
            elif option == 2:
                self.create()
            elif option == 3:
                self.delete()
            elif option == 4:
                self.update()
            else:
                break
