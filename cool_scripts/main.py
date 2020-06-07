from .apps.color_detection.app import start_script as start_color_detection_app
from simple_term_menu import TerminalMenu

green_color = '\033[94m'
black_color = '\033[0m'


def start_app():
    print(f"{green_color}starting scripts app{black_color}")
    print("available apps: ")
    terminal_options = ['image detection app', 'teste 2', 'teste 3']
    terminal_menu = TerminalMenu(terminal_options)
    selected_option_index = terminal_menu.show()
    
    if selected_option_index == 0:
        start_color_detection_app()

