from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation


class MatdoushApp(App):
    def build(self):
        layout = FloatLayout()

        button = Button(
            text="DONT PRESS",
            font_size=30,
            size_hint=(None, None),
            size=(300, 100),
            pos=(0, 0)
        )

        def center_button(*args):
            button.center = layout.center

        layout.bind(size=center_button, pos=center_button)

        def press_button(instance):
            Animation.cancel_all(instance)

            start_x = instance.x

            anim = Animation(x=start_x + 50, duration=0.10)
            anim += Animation(x=start_x - 50, duration=0.10)
            anim += Animation(x=start_x + 30, duration=0.08)
            anim += Animation(x=start_x - 20, duration=0.06)
            anim += Animation(x=start_x, duration=0.10)

            anim.start(instance)

        button.bind(on_press=press_button)
        layout.add_widget(button)

        return layout


if __name__ == "__main__":
    MatdoushApp().run()