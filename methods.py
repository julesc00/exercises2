"""
Types of methods
"""


class Music:
    @staticmethod
    def play():
        print("Playing music")

    def stop(self):
        print("stop playing")


Music.play()  # stop() won't execute like this.

obj = Music()
obj.stop()
obj.play()
