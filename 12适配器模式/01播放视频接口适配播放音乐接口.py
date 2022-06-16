from abc import ABCMeta, abstractmethod

"""
适配器模式（Adapter Pattern）是作为两个不兼容的接口之间的桥梁。
这种类型的设计模式属于结构型模式，它结合了两个独立接口的功能。

这种模式涉及到一个单一的类，该类负责加入独立的或不兼容的接口功能。
举个真实的例子，读卡器是作为内存卡和笔记本之间的适配器。
您将内存卡插入读卡器，再将读卡器插入笔记本，这样就可以通过笔记本来读取内存卡。

我们通过下面的实例来演示适配器模式的使用。其中，音频播放器设备只能播放 mp3 文件，
通过使用一个更高级的音频播放器来播放 vlc 和 mp4 文件。
"""


# 为媒体播放器和更高级的媒体播放器创建接口。
class MediaPlayer(metaclass=ABCMeta):
    @abstractmethod
    def play(self, audiotype, filename):
        pass


class AdvancedMediaPlayer(metaclass=ABCMeta):
    @abstractmethod
    def playVlc(self, filename):
        pass

    def playMp4(self, filename):
        pass


# 创建实现了 AdvancedMediaPlayer 接口的实体类。
class VlcPlayer(AdvancedMediaPlayer):
    def playVlc(self, filename):
        print('播放vlc: {}'.format(filename))

    def playMp4(self, filename):
        # 什么都不做
        pass


class Mp4Player(AdvancedMediaPlayer):
    def playMp4(self, filename):
        print('播放mp4: {}'.format(filename))

    def playVlc(self, filename):
        # 什么都不做
        pass


# 创建实现了 MediaPlayer 接口的适配器类。
class MediaAdapter(MediaPlayer):
    def __init__(self, audiotype):
        if audiotype.lower() == "vlc":
            self.advancedMusicPlayer = VlcPlayer()
        elif audiotype.lower() == "mp4":
            self.advancedMusicPlayer = Mp4Player()

    def play(self, audiotype, filename):
        if audiotype.lower() == "vlc":
            self.advancedMusicPlayer.playVlc(filename)
        elif audiotype.lower() == "mp4":
            self.advancedMusicPlayer.playMp4(filename)


class AudioPlayer(MediaPlayer):
    def __init__(self):
        pass

    def play(self, audiotype, filename):
        if audiotype.lower() == 'mp3':
            print('播放mp3: {}'.format(filename))
        elif audiotype.lower() in ["vlc", "mp4"]:
            media_adapter = MediaAdapter(audiotype)
            media_adapter.play(audiotype, filename)
        else:
            raise RuntimeError("Invalid media. {}\t{}".format(audiotype, filename))


if __name__ == '__main__':
    audioPlayer = AudioPlayer()
    audioPlayer.play('mp3', "beyond horizaon")
    audioPlayer.play("mp4", "alone.mp4")
    audioPlayer.play("vlc", "away.vlc")
    audioPlayer.play("avi", "secret.avi")
