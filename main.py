from repository import *
from shared import *
from screen import *
from utils import Formatter

class Main:

    def __init__(self):
        self.__transaction_repo: TransactionRepo = TransactionRepoCSV("./data/transaction.csv")
        self.__category_repo: CategoryRepo = CategoryRepoCSV(
            csv_path="./data/category.csv", 
            transaction_repo=self.__transaction_repo
        )
        self.__user_repo: UserRepo = UserRepoCSV("./data/user.csv")
        
        self.__auth_screen = AuthScreen(self.__user_repo)
        self.__category_screen = CategoryScreen(self.__category_repo)
        self.__transaction_screen = TransactionScreen(
            self.__transaction_repo,
            self.__category_repo,
            self.__category_screen
        )
    
    def run(self):
        self.__auth_screen.run()

        # Session.login(1)

        if Session.is_authenticated():
            while True:
                print()
                print("1. Category Management")
                print("2. Transaction Management")
                print("3. Report Viewer")
                print("4. Logout")
                print()

                option = Formatter.option_picker(1, 4)
                    
                if option == 1:
                    self.__category_screen.run()
                elif option == 2:
                    self.__transaction_screen.run()
                elif option == 4:
                    self.__auth_screen.logout()
                    break

EntityIDManager.set_csv_path("./data/entity_id.csv")

main = Main()

while True:
    main.run()