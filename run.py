from menu import Menu
from app import App


def main():
    app = App()
    menu = Menu()
    menu.menu_select_mode(app)


if __name__ == "__main__":
    main()
