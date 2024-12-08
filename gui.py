from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from qr_utils import generate_qr_code

# Ustawienia okna
Window.size = (800, 600)
Window.clearcolor = (0.15, 0.15, 0.15, 1)  # Ciemnoszare tło aplikacji

class QRGeneratorApp(App):
    def build(self):
        self.title = "QR Code Generator"

        # Główny layout w stylu minimalistycznym
        main_layout = AnchorLayout(anchor_x='center', anchor_y='center')
        container = BoxLayout(orientation='vertical', padding=20, spacing=20, size_hint=(0.8, 0.8))

        # Nagłówek
        header = Label(
            text="QR Code Generator",
            font_size="30sp",
            color=(1, 1, 1, 1),
            size_hint=(1, 0.1),
            halign="center",
        )
        container.add_widget(header)

        # Pole tekstowe
        self.input_text = TextInput(
            hint_text="Enter text, URL, or any data to encode",
            size_hint=(1, 0.15),
            background_color=(0.2, 0.2, 0.2, 1),
            foreground_color=(1, 1, 1, 1),
            cursor_color=(1, 1, 1, 1),
            multiline=False,
        )
        container.add_widget(self.input_text)

        # Przycisk do generowania kodu QR
        generate_button = Button(
            text="Generate QR Code",
            size_hint=(1, 0.1),
            background_color=(0.1, 0.5, 0.8, 1),
            color=(1, 1, 1, 1),
        )
        generate_button.bind(on_press=self.on_generate_button_press)
        container.add_widget(generate_button)

        # Obraz kodu QR - niewidoczny na początku
        self.qr_image = Image(size_hint=(1, 0.55), opacity=0)  # Ukryte przez opacity
        container.add_widget(self.qr_image)

        main_layout.add_widget(container)
        return main_layout

    def on_generate_button_press(self, instance):
        data = self.input_text.text.strip()
        if not data:
            self.show_popup("Error", "Please enter some data to encode.")
            return

        try:
            generate_qr_code(data, "assets/qr_code.png")

            self.qr_image.source = "assets/qr_code.png"
            self.qr_image.opacity = 1  # Uwidocznienie obrazu po generacji
            self.qr_image.reload()

            self.show_popup("Success", "QR Code generated successfully!")
        except Exception as e:
            self.show_popup("Error", f"An error occurred: {e}")

    def show_popup(self, title, message):
        popup_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        popup_layout.add_widget(Label(text=message, color=(1, 1, 1, 1)))

        close_button = Button(
            text="Close",
            size_hint=(1, 0.3),
            background_color=(0.5, 0.1, 0.1, 1),
            color=(1, 1, 1, 1),
        )
        popup = Popup(
            title=title,
            content=popup_layout,
            size_hint=(0.6, 0.4),
            auto_dismiss=False,
            background_color=(0.15, 0.15, 0.15, 1),
        )
        close_button.bind(on_press=popup.dismiss)
        popup_layout.add_widget(close_button)
        popup.open()
