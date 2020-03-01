from win10toast import ToastNotifier
from playsound import playsound

from multiprocessing import Process
import time


class Water:

    def __init__(self, toaster):
        self.toaster = toaster

    def toast(self):
        self.toaster.show_toast
        (
        "Drink your water", 
        "Please drink your water!\n\n", 
        duration=10, 
        icon_path="water.ico"
        )

    def music(self):
        playsound('audio.mp3')

    def start(self, toast, music):
        if __name__ == "__main__":

            toast.start()
            music.start()

            return toast_process, music_process

water = Water(ToastNotifier())

time.sleep(3600)

toast_process = Process(target=water.toast)
music_process = Process(target=water.music)



water.start(toast_process, music_process)


