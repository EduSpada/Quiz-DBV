
import PySimpleGUI as sg


class Theme:
    __version__ = "1.0.1"
    
    def themes(background, text):
        sg.theme_text_element_background_color(background)
        sg.theme_background_color(background)
        sg.theme_element_background_color(background)
        sg.theme_input_background_color(background)
        sg.theme_element_text_color(text)
        sg.theme_text_color(text)
        sg.theme_input_text_color(text)