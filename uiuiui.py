from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from weather import Weather

Builder.load_file('my.kv')

class SigninPage(Screen):
    def go_to_knowledge(self, trail_code):
        self.manager.current = 'knowledge'
        self.manager.get_screen('knowledge').update_data(trail_code)

class GuestScreen(Screen):
    def print_passcode(self, passcode):
        print(f'Entered passcode is: {passcode}')

class KnowledgeScreen(Screen):
    def __init__(self, **kwargs):
        super(KnowledgeScreen, self).__init__(**kwargs)
        self.trail_code = '' 

    def update_data(self, trail_code_input):
        self.ids.trail_code_display.text = 'Trail Code: ' + trail_code_input
        weather = Weather()
        if trail_code_input == '123':
            weather_condition, weather_temp = weather.get_weather("denver")
            self.ids.weather.text = str(weather_temp) + "  oF" + "\n" + weather_condition
            self.ids.alert.text = "Alert: " + "Strong winds"
            self.ids.more_info.text = "More Info: " + "Nice trail ahead !"
            self.ids.warning.text = "Warning: " + "Beware of Bears"
            self.ids.map_image.source = "cherry-creek.png"

# class MapWidget(Screen):
#     def __init__(self, **kwargs):
#         super(MapWidget, self).__init__(**kwargs)
#         self.size_hint = (1, 1)
#         self.bind(size=self.update)
        
#         # Example map data
#         self.add_widget(Label(text="Map Data: Latitude = 40.7128, Longitude = -74.0060", color=(0, 0, 0, 1)))

#         with self.canvas:
#             Color(1, 1, 1, 1)  # White background
#             self.rect = Rectangle(pos=self.pos, size=self.size)
    
#     def update(self, *args):
#         self.rect.pos = self.pos
#         self.rect.size = self.size
        
class ScreenManagement(ScreenManager):
    pass

class TrailApp(App):
    def build(self):
        return ScreenManagement()

if __name__ == '__main__':
    TrailApp().run()

