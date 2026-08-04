from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
from kivy.core.window import Window
import random

Window.clearcolor = (0.53, 0.81, 0.98, 1)

sm = ScreenManager()


class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = FloatLayout()

        title = Label(
            text="❤️ Chirry My Love Will You Go On A Date With Me? ❤️",
            font_size=28,
            color=(0.5,0,0.5,1),
            size_hint=(0.8,0.2),
            pos_hint={"center_x":0.5,"top":0.95}
        )

        yes = Button(
            text="YES ❤️",
            size_hint=(0.3,0.12),
            pos_hint={"x":0.15,"y":0.2},
            background_color=(0.5,0,0.5,1)
        )

        no = Button(
            text="NO 😅",
            size_hint=(0.3,0.12),
            pos_hint={"x":0.55,"y":0.2},
            background_color=(0.5,0,0.5,1)
        )

        yes.bind(on_press=lambda x: setattr(sm,"current","food"))
        no.bind(on_touch_down=self.move_button)

        layout.add_widget(title)
        layout.add_widget(yes)
        layout.add_widget(no)

        self.add_widget(layout)

    def move_button(self, instance, touch):
        if instance.collide_point(*touch.pos):
            instance.pos_hint={
                "x":random.random()*0.7,
                "y":random.random()*0.6
            }
            return True


class FoodScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=10
        )

        layout.add_widget(Label(
            text="🥰 What would you like to eat Princess?",
            font_size=24
        ))

        grid = GridLayout(
            cols=2,
            spacing=10
        )

        for item in ["🍕 Pizza","🍔 Burger","🍗 Chicken","🍝 Pasta","🍟 Fries","🍣 Sushi"]:
            btn=Button(text=item)
            btn.bind(on_press=lambda x:setattr(sm,"current","fee"))
            grid.add_widget(btn)

        layout.add_widget(grid)
        self.add_widget(layout)


class FeeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout=BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=20
        )

        layout.add_widget(Label(
            text="😂 Just One Small Fee...\n\nSend KSh 1000 to confirm the date 😜",
            font_size=22
        ))

        btn=Button(
            text="💳 Send M-Pesa"
        )

        btn.bind(on_press=lambda x:setattr(sm,"current","date"))

        layout.add_widget(btn)
        self.add_widget(layout)


class DateScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout=BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=20
        )

        layout.add_widget(Label(
            text="""
❤️ OUR DATE ❤️

👧 Chirry       Ronoo 👦

☕────────☕

🍰    🍕

📅 26th August

📍 China Square, Nairobi

❤️ Can't wait to see you ❤️
""",
            font_size=22
        ))

        btn=Button(
            text="❤️ Continue ❤️"
        )

        btn.bind(
            on_press=lambda x:setattr(sm,"current","girlfriends")
        )

        layout.add_widget(btn)

        self.add_widget(layout)


class GirlfriendsDayScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout=BoxLayout(
            orientation="vertical",
            padding=20
        )

        scroll=ScrollView()

        label=Label(
            text="""
❤️ Happy Girlfriend's Day ❤️

To My Beautiful Chirry,

You bring light to my darkest days,
calm to my storms,
and love to my heart.

You are my greatest blessing.

I love you endlessly.

Forever Yours,

Ronoo
""",
            font_size=22,
            size_hint_y=None
        )

        label.bind(
            texture_size=lambda instance,value:setattr(instance,"height",value[1])
        )

        scroll.add_widget(label)

        layout.add_widget(scroll)

        btn=Button(
            text="❤️ View Our Photo ❤️",
            size_hint=(1,0.15)
        )

        btn.bind(
            on_press=lambda x:setattr(sm,"current","photo")
        )

        layout.add_widget(btn)

        self.add_widget(layout)


class PhotoScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout=BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=20
        )

        layout.add_widget(Label(
            text="❤️ Our Beautiful Memory ❤️",
            font_size=28
        ))

        image=Image(
            source="love_photo.jpg",
            allow_stretch=True,
            keep_ratio=True
        )

        layout.add_widget(image)

        btn=Button(
            text="❤️ Continue ❤️",
            size_hint=(1,0.15)
        )

        btn.bind(
            on_press=lambda x:setattr(sm,"current","final")
        )

        layout.add_widget(btn)

        self.add_widget(layout)


class FinalScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(Label(
            text="""
♥ ♥ ♥

My Dearest Chirry

With your sweet YES,
you made my heart skip a beat.

I can't wait to hold your hand,
laugh with you,
and make beautiful memories.

Forever Yours,

Ronoo

♥ ♥ ♥
""",
            font_size=22
        ))


sm.add_widget(FirstScreen(name="first"))
sm.add_widget(FoodScreen(name="food"))
sm.add_widget(FeeScreen(name="fee"))
sm.add_widget(DateScreen(name="date"))
sm.add_widget(GirlfriendsDayScreen(name="girlfriends"))
sm.add_widget(PhotoScreen(name="photo"))
sm.add_widget(FinalScreen(name="final"))

sm.current="first"


class DateApp(App):
    def build(self):
        return sm


DateApp().run()			