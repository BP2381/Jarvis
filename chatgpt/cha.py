import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QLabel, QHBoxLayout
)
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt
import threading
from jarvis_core import process_query  # Your logic in a separate file


class JarvisGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Jarvis AI Assistant")
        self.setGeometry(100, 100, 600, 500)
        self.setStyleSheet("background-color: #0F0F0F; color: #00FFF7; font-size: 14px;")

        self.layout = QVBoxLayout()

        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.chat_display.setStyleSheet("background-color: #1E1E1E; color: #00FFF7;")
        self.layout.addWidget(self.chat_display)

        self.button_layout = QHBoxLayout()

        self.listen_btn = QPushButton("🎙️ Listen")
        self.listen_btn.clicked.connect(self.start_listening)
        self.listen_btn.setStyleSheet("background-color: #222; padding: 10px;")
        self.button_layout.addWidget(self.listen_btn)

        self.mic_animation = QLabel()
        self.mic_movie = QMovie("mic_wave.gif")  # Add an animated GIF for effect
        self.mic_animation.setMovie(self.mic_movie)
        self.button_layout.addWidget(self.mic_animation)

        self.layout.addLayout(self.button_layout)

        self.setLayout(self.layout)

    def start_listening(self):
        self.chat_display.append("🟢 Listening...")
        self.mic_movie.start()
        thread = threading.Thread(target=self.listen_and_respond)
        thread.start()

    def listen_and_respond(self):
        from jarvis_core import takeCommand, speak
        query = takeCommand()
        if query != "None":
            self.chat_display.append(f"🧑 You: {query}")
            response = process_query(query)
            self.chat_display.append(f"🤖 Jarvis: {response}")
            speak(response)
        else:
            self.chat_display.append("❌ Could not understand.")
        self.mic_movie.stop()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = JarvisGUI()
    gui.show()
    sys.exit(app.exec_())
