# [check] Get control of keyboard and hit checks (check w/ virtual keyboard, text)
# [check] Get input from microphone non-exclusively (is that even a thing) and hit keys on command
# interpret language of PIE commands
import threading
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Process, Lock
from queue import Queue

from pynput.keyboard import Key, Listener
import pydirectinput
import speech_recognition as sr
from time import sleep
from commands import COMMANDS

CREDENTIALS_FILE = '.credentials'


def listen(text_queue: Queue) -> None:
    recognizer = sr.Recognizer()
    with sr.Microphone() as microphone:
        audio = recognizer.listen(microphone, timeout=5)
    text = recognizer.recognize_google_cloud(audio, credentials_json=CREDENTIALS_FILE).strip().lower()
    text_queue.put(text)


def print_text(queue: Queue):
    while text := queue.get():
        # TODO: Match two statements in the same text
        try:
            commands = COMMANDS[text]
            for command in commands:
                print(f"Match: {text} to {command}")
                pydirectinput.press(command)
        except KeyError:
            print(f"No match: {text}")


class SpeechAgent:
    trigger_key: Key = Key.home

    executor: ThreadPoolExecutor
    text_queue: Queue
    actor: threading.Thread

    def __init__(self):
        self.text_queue = Queue()
        self.executor = ThreadPoolExecutor()
        self.actor = threading.Thread(target=print_text, args=[self.text_queue])
        self.actor.start()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.executor.__exit__(exc_type, exc_val, exc_tb)

    def on_press(self, key: Key) -> None:
        if key != self.trigger_key:
            return

        self.executor.submit(listen, self.text_queue)
        print("Listener started")


if __name__ == '__main__':
    agent = SpeechAgent()
    with Listener(on_press=agent.on_press) as listener:
        listener.join()
