import threading
from concurrent.futures import ThreadPoolExecutor
from queue import Queue

from pynput.keyboard import Key, Listener
import pydirectinput
import speech_recognition as sr
from commands import COMMANDS, SUBJECTS

CREDENTIALS_FILE = '.credentials'


def listen(text_queue: Queue) -> None:
    recognizer = sr.Recognizer()
    with sr.Microphone() as microphone:
        audio = recognizer.listen(microphone, timeout=5)
    text = recognizer.recognize_google_cloud(audio, credentials_json=CREDENTIALS_FILE).strip().lower()
    text_queue.put(text)


def print_text(queue: Queue):
    while text := queue.get():
        # TODO: Match two statements in the same text, like, elegantly and stuff. This is the dumb way.
        # Major assumption: text = <subject> | <subject> <command> | <command>
        parts = text.split(' ')

        # Look for a subject matching the beginning of the text
        try:
            potential_subject = parts[0]
            pydirectinput.press(SUBJECTS[potential_subject])
            print(f"Match: {potential_subject} to subject {SUBJECTS[potential_subject]}")
            parts = parts[1:]
        except KeyError:
            print(f"No 1-word subject match for {potential_subject}")
            potential_subject = ' '.join(parts[0:2])
            try:
                pydirectinput.press(SUBJECTS[potential_subject])
                print(f"Match: {potential_subject} to subject {SUBJECTS[potential_subject]}")
                parts = parts[2:]
            except KeyError:
                print(f"No 2-word subject match for {potential_subject}")

        # Look for a command matching the remaining text
        potential_command = ' '.join(parts)
        try:
            commands = COMMANDS[potential_command]
            for command in commands:
                print(f"Match: {potential_command} to command {command}")
                pydirectinput.press(command)
        except KeyError:
            print(f"No match: {potential_command}")


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
