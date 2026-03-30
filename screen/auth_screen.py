from utils import AuthScreenValidator, Formatter
from model import User
from shared import *
from repository import UserRepo
import getpass

class AuthScreen():

    def __init__(self, user_repo: UserRepo):
        self.__user_repo: UserRepo = user_repo

    def register(self) -> Result:
        user: User = User.get_blank_object()

        while True:
            email = AuthScreenValidator.validate_email(
                input(Formatter.input("Enter email: "))
            )
            if email.is_success():
                user.set_email(email.get_value())
                break
            print(Formatter.error(email.get_error_msg()))

        while True:
            pwd = AuthScreenValidator.validator_pwd(
                getpass.getpass(Formatter.input("Enter password: "))
            )
            if pwd.is_success():
                user.set_pwd(pwd.get_value())
                break
            print(Formatter.error(pwd.get_error_msg()))

        user.set_id(EntityIDManager.get_and_update_user_id())
        create_new_user = self.__user_repo.create(user)

        if create_new_user.is_success():
            return Result.success("created user")
        return Result.fail(create_new_user.get_error_msg())
    
    def login(self) -> Result:
        email = ""
        pwd = ""

        while True:
            email_input = AuthScreenValidator.validate_email(
                input(Formatter.input("Enter email: "))
            )
            if email_input.is_success():
                email = email_input.get_value()
                break
            print(Formatter.error(email_input.get_error_msg()))

        while True:
            pwd_input = AuthScreenValidator.validator_pwd(
                getpass.getpass(Formatter.input("Enter password: "))
            )
            if pwd_input.is_success():
                pwd = pwd_input.get_value()
                break
            print(Formatter.error(pwd_input.get_error_msg()))

        user = self.__user_repo.find_by_email(email)
        if not user.is_success():
            return Result.fail("Invalid email or password")
        
        if user.get_value().get_pwd() != pwd:
            return Result.fail("Invalid email or password")
        
        Session.login(user.get_value().get_id())
        return Result.success("Login success")

    def logout(self) -> None:
        Session.logout()
    
    def run(self) -> None:
        print()
        print(Formatter.section_seperator("Authentication/Authorization"))
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        print()
        option = Formatter.option_picker(1, 3)

        if option == 1:
            screen = self.register()
            if screen.is_success():
                print(Formatter.success(screen.get_value()))
            else:
                print(Formatter.error(screen.get_error_msg()))
        elif option == 2:
            screen = self.login()
            if screen.is_success():
                print(Formatter.success(screen.get_value()))
            else:
                print(Formatter.error(screen.get_error_msg()))
        else:
            exit(0)