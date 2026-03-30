class Formatter:
    @staticmethod
    def input(label: str) -> str:
        return f"* [INPUT] {label}"
    
    @staticmethod
    def success(label: str) -> str:
        return f"+ [SUCCESS] {label}"
    
    @staticmethod
    def error(label: str) -> str:
        return f"- [ERORR] {label}"
    
    @staticmethod
    def result(label: str) -> str:
        return f"^ [RESULT] {label}"
    
    @staticmethod
    def section_seperator(section_name: str) -> None:
        return f"=== {section_name} ==="

    @staticmethod
    def option_picker(min: int, max: int) -> int:
        option = 0

        while True:
            try:
                option = int(
                    input(Formatter.input("Enter option: "))
                )
                if not (option < min and option > max):
                    break

                print(Formatter.error(f"Option must between {min} and {max}"))
            except ValueError:
                print(Formatter.error("Option must be a number"))

        return option
