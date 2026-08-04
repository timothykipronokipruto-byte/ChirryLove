from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.properties import NumericProperty
import random
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

Window.clearcolor = get_color_from_hex("#FFF0F5")

sm = ScreenManager(
    transition=FadeTransition(duration=0.45)
)


class ImageButton(ButtonBehavior, Image):
    pass


class FloatingHeart(Widget):

    size_value = NumericProperty(20)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.size = (self.size_value, self.size_value)

        with self.canvas:
            Color(1, 0.3, 0.6, random.uniform(0.3, 0.8))
            self.heart = Ellipse(
                pos=self.pos,
                size=self.size
            )

        self.bind(
            pos=self.update_graphics,
            size=self.update_graphics
        )

    def update_graphics(self, *args):
        self.heart.pos = self.pos
        self.heart.size = self.size


class RomanticBackground(FloatLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.bg = Image(
            source=os.path.join(
                BASE_DIR,
                "assets",
                "background.png"
            ),
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(1, 1)
        )

        self.add_widget(self.bg)

        Clock.schedule_interval(
            self.spawn_heart,
            0.6
        )

    def spawn_heart(self, dt):

        heart = FloatingHeart()

        heart.pos = (
            random.randint(
                0,
                int(Window.width)
            ),
            -40
        )

        heart.size = (
            random.randint(12, 28),
            random.randint(12, 28)
        )

        self.add_widget(heart)

        anim = Animation(
            y=Window.height + 40,
            duration=random.uniform(
                5,
                9
            )
        )

        anim.bind(
            on_complete=lambda *x:
            self.remove_widget(heart)
        )

        anim.start(heart)


class FirstScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = RomanticBackground()

        title = Label(
            text="❤️\nChirry My Love\n\nWill You Go On A Date With Me?\n❤️",
            font_size=33,
            bold=True,
            color=get_color_from_hex("#7B1FA2"),
            size_hint=(0.9, 0.25),
            pos_hint={
                "center_x": 0.5,
                "top": 0.95
            },
            halign="center",
            valign="middle"
        )

        title.bind(
            size=lambda i, v:
            setattr(
                i,
                "text_size",
                (i.width, i.height)
            )
        )

        root.add_widget(title)

        self.photo = Image(
            source=os.path.join(
                BASE_DIR,
                "love_photo.jpg"
            ),
            allow_stretch=True,
            keep_ratio=True,
            size_hint=(0.55, 0.35),
            pos_hint={
                "center_x": 0.5,
                "center_y": 0.52
            }
        )

        root.add_widget(self.photo)

        self.yes = ImageButton(
            source=os.path.join(
                BASE_DIR,
                "assets",
                "yes_heart.png"
            ),
            size_hint=(0.25, 0.18),
            pos_hint={
                "x": 0.12,
                "y": 0.08
            }
        )

        self.no = Button(
            text="NO 😅",
            font_size=20,
            bold=True,
            background_normal="",
            background_color=get_color_from_hex("#F06292"),
            color=(1, 1, 1, 1),
            size_hint=(0.24, 0.11),
            pos_hint={
                "x": 0.62,
                "y": 0.11
            }
        )

        self.yes.bind(
            on_press=self.go_yes
        )

        self.no.bind(
            on_touch_down=self.move_no
        )

        root.add_widget(self.yes)
        root.add_widget(self.no)

        self.add_widget(root)

        Clock.schedule_interval(
            self.beat,
            0.8
        )
    def beat(self, dt):

        anim = Animation(
            size_hint=(0.27, 0.20),
            duration=0.35
        ) + Animation(
            size_hint=(0.25, 0.18),
            duration=0.35
        )

        anim.start(self.yes)

    def move_no(self, instance, touch):

        if self.no.collide_point(*touch.pos):

            self.no.pos_hint = {
                "x": random.uniform(0.05, 0.75),
                "y": random.uniform(0.05, 0.75)
            }

            return True

        return False

    def go_yes(self, *args):

        sm.current = "food"


class FoodScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = RomanticBackground()

        box = BoxLayout(
            orientation="vertical",
            spacing=20,
            padding=30
        )

        title = Label(
            text="🍽️\nWhat would you like us to eat?",
            font_size=30,
            bold=True,
            color=get_color_from_hex("#C2185B"),
            size_hint=(1, .2)
        )

        box.add_widget(title)

        grid = GridLayout(
            cols=2,
            spacing=20,
            size_hint_y=None
        )

        grid.bind(
            minimum_height=grid.setter("height")
        )

        meals = [
            "🍕 Pizza",
            "🍔 Burger",
            "🍗 Chicken",
            "🍝 Pasta",
            "🥩 Steak",
            "🍣 Sushi",
            "🌮 Tacos",
            "🍨 Ice Cream"
        ]

        for meal in meals:

            btn = Button(
                text=meal,
                font_size=22,
                background_normal="",
                background_color=get_color_from_hex("#F48FB1"),
                color=(1, 1, 1, 1),
                height=70,
                size_hint_y=None
            )

            btn.bind(
                on_press=self.pick_food
            )

            grid.add_widget(btn)

        scroll = ScrollView()

        scroll.add_widget(grid)

        box.add_widget(scroll)

        root.add_widget(box)

        self.add_widget(root)

    def pick_food(self, button):

        App.get_running_app().selected_food = button.text

        sm.current = "date"
class DateScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = RomanticBackground()

        card = BoxLayout(
            orientation="vertical",
            spacing=20,
            padding=35,
            size_hint=(0.88, 0.82),
            pos_hint={
                "center_x": 0.5,
                "center_y": 0.5
            }
        )

        title = Label(
            text="💌 Our Date Invitation 💌",
            font_size=30,
            bold=True,
            color=get_color_from_hex("#AD1457"),
            size_hint=(1, .18)
        )

        self.details = Label(
            text="",
            font_size=22,
            halign="center",
            valign="middle",
            color=get_color_from_hex("#6A1B9A")
        )

        self.details.bind(
            size=lambda i, v:
            setattr(
                i,
                "text_size",
                (i.width, i.height)
            )
        )

        btn = Button(
            text="I'm Excited ❤️",
            font_size=24,
            bold=True,
            background_normal="",
            background_color=get_color_from_hex("#EC407A"),
            color=(1, 1, 1, 1),
            size_hint=(1, .16)
        )

        btn.bind(
            on_press=lambda x:
            setattr(
                sm,
                "current",
                "gallery"
            )
        )

        card.add_widget(title)
        card.add_widget(self.details)
        card.add_widget(btn)

        root.add_widget(card)

        self.add_widget(root)

    def on_pre_enter(self):

        food = getattr(
            App.get_running_app(),
            "selected_food",
            "Anything"
        )

        self.details.text = (
            "📅 Saturday\n\n"
            "🕓 4:00 PM\n\n"
            "📍 Our Favorite Place\n\n"
            f"🍽️ {food}\n\n"
            "✨ It will be a beautiful day together ❤️"
        )
class GalleryScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = RomanticBackground()

        layout = BoxLayout(
            orientation="vertical",
            spacing=20,
            padding=20
        )

        title = Label(
            text="📸 Beautiful Memories",
            font_size=30,
            bold=True,
            color=get_color_from_hex("#C2185B"),
            size_hint=(1, .15)
        )

        layout.add_widget(title)

        photo = Image(
            source=os.path.join(
                BASE_DIR,
                "love_photo.jpg"
            ),
            allow_stretch=True,
            keep_ratio=True,
            size_hint=(1, .70)
        )

        layout.add_widget(photo)

        btn = Button(
            text="Continue ❤️",
            font_size=24,
            bold=True,
            background_normal="",
            background_color=get_color_from_hex("#EC407A"),
            color=(1, 1, 1, 1),
            size_hint=(1, .15)
        )

        btn.bind(
            on_press=lambda x:
            setattr(
                sm,
                "current",
                "letter"
            )
        )

        layout.add_widget(btn)

        root.add_widget(layout)

        self.add_widget(root)


class LetterScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = RomanticBackground()

        layout = BoxLayout(
            orientation="vertical",
            spacing=20,
            padding=30
        )

        title = Label(
            text="💌 A Letter For You",
            font_size=30,
            bold=True,
            color=get_color_from_hex("#AD1457"),
            size_hint=(1, .15)
        )

        layout.add_widget(title)

        letter = Label(
            text=(
                "Every moment with you feels like a beautiful dream.\n\n"
                "Your smile brightens my darkest days,\n"
                "your laughter fills my heart with joy,\n"
                "and every second spent with you\n"
                "becomes a memory I'll treasure forever.\n\n"
                "Thank you for being amazing.\n\n"
                "❤️"
            ),
            font_size=22,
            halign="center",
            valign="middle",
            color=get_color_from_hex("#6A1B9A")
        )

        letter.bind(
            size=lambda i, v:
            setattr(
                i,
                "text_size",
                (i.width, i.height)
            )
        )

        layout.add_widget(letter)

        btn = Button(
            text="One Last Surprise 🎁",
            font_size=24,
            bold=True,
            background_normal="",
            background_color=get_color_from_hex("#EC407A"),
            color=(1, 1, 1, 1),
            size_hint=(1, .15)
        )

        btn.bind(
            on_press=lambda x:
            setattr(
                sm,
                "current",
                "final"
            )
        )

        layout.add_widget(btn)

        root.add_widget(layout)

        self.add_widget(root)
class FinalScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = RomanticBackground()

        layout = BoxLayout(
            orientation="vertical",
            spacing=25,
            padding=35
        )

        title = Label(
            text="❤️ The Final Surprise ❤️",
            font_size=34,
            bold=True,
            color=get_color_from_hex("#AD1457"),
            size_hint=(1, .15)
        )

        layout.add_widget(title)

        final_photo = Image(
            source=os.path.join(
                BASE_DIR,
                "love_photo.jpg"
            ),
            allow_stretch=True,
            keep_ratio=True,
            size_hint=(1, .45)
        )

        layout.add_widget(final_photo)

        message = Label(
            text=(
                "Chirry ❤️\n\n"
                "From the very first moment,\n"
                "you made my world brighter.\n\n"
                "Thank you for your smile,\n"
                "your kindness,\n"
                "and for simply being you.\n\n"
                "Will you make more beautiful\n"
                "memories with me?\n\n"
                "❤️ I Like You ❤️"
            ),
            font_size=24,
            halign="center",
            valign="middle",
            color=get_color_from_hex("#6A1B9A")
        )

        message.bind(
            size=lambda i, v:
            setattr(
                i,
                "text_size",
                (i.width, i.height)
            )
        )

        layout.add_widget(message)

        finish = Button(
            text="Forever Starts Here 💍",
            font_size=24,
            bold=True,
            background_normal="",
            background_color=get_color_from_hex("#EC407A"),
            color=(1, 1, 1, 1),
            size_hint=(1, .14)
        )

        finish.bind(
            on_press=self.finish_app
        )

        layout.add_widget(finish)

        root.add_widget(layout)

        self.add_widget(root)

    def finish_app(self, *args):

        App.get_running_app().stop()


sm.add_widget(FirstScreen(name="home"))
sm.add_widget(FoodScreen(name="food"))
sm.add_widget(DateScreen(name="date"))
sm.add_widget(GalleryScreen(name="gallery"))
sm.add_widget(LetterScreen(name="letter"))
sm.add_widget(FinalScreen(name="final"))


class ChirryLoveApp(App):

    selected_food = "Pizza 🍕"

    def build(self):

        self.title = "Chirry Love ❤️"

        return sm


if __name__ == "__main__":
    ChirryLoveApp().run()
