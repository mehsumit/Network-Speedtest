from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
import speedtest
import threading

class SpeedTestApp(App):
    def build(self):
        Window.clearcolor = (1, 0.8, 0.9, 1)  # light pink background

        self.layout = BoxLayout(orientation='vertical', padding=30, spacing=20)

        self.title_label = Label(
            text=" Internet Speed Test",
            font_size='24sp',
            bold=True,
            color=(0,0,0,1)
        )
        self.layout.add_widget(self.title_label)

        self.download_label = Label(
            text="Download: 00 Mbps",
            font_size='20sp',
            color=(0.2,0.2,0.8,1)
        )
        self.layout.add_widget(self.download_label)

        self.upload_label = Label(
            text="Upload: 00 Mbps",
            font_size='20sp',
            color=(0.8,0.2,0.2,1)
        )
        self.layout.add_widget(self.upload_label)

        self.button = Button(
            text=" Check Speed",
            size_hint=(1, 0.2),
            background_color=(1,0,0,1),
            font_size='18sp',
            bold=True
        )
        self.button.bind(on_press=self.start_speedcheck)
        self.layout.add_widget(self.button)

        return self.layout

    def start_speedcheck(self, instance):
        # Show temporary status
        self.download_label.text = "Download: Checking..."
        self.upload_label.text = "Upload: Checking..."

        # Run speedtest in background thread (UI freeze na ho)
        threading.Thread(target=self.speedcheck).start()

    def speedcheck(self):
        st = speedtest.Speedtest()
        st.get_servers()
        down = str(round(st.download()/(10**6),2)) + " Mbps"
        up = str(round(st.upload()/(10**6),2)) + " Mbps"

        # Update labels after test
        self.download_label.text = "Download: " + down
        self.upload_label.text = "Upload: " + up

if __name__ == "__main__":
    SpeedTestApp().run()
