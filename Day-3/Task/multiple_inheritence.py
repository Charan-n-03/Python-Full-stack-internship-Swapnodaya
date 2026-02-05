class camera:
    def __init__(self, camera_quality):
        self. camera_quality= camera_quality

    def display_camera_details(self):
        print("Camera:",self.camera_quality)

class MusicPlayer:
    def __init__(self, sound_quality):
        self. sound_quality= sound_quality
    
    def display_music_details(self):
        print("Music:",self.sound_quality)

class SmartPhone(camera,MusicPlayer):
    def __init__(self,brand,camera_quality,sound_quality):
        camera.__init__(self,sound_quality)
        MusicPlayer.__init__(self,camera_quality)
        self.brand=brand
    def display_smartphone_details(self):
        print("Phone:",self.brand)
        print("Camera:",self.camera_quality)
        print("Music:",self.sound_quality)

samsung=SmartPhone("SAMSUNG","200MP","50db")
samsung.display_smartphone_details()
