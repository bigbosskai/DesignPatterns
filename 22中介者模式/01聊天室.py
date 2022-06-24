import time


class ChatRoom:
    @staticmethod
    def show_msg(user, message):
        print(time.strftime('%Y-%m-%d %H:%M:%S:' + '[{}]:{}'.format(user.getName(), message)))


class User:
    def __init__(self, name):
        self.name = name

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def send_msg(self, msg):
        ChatRoom.show_msg(self, msg)


if __name__ == '__main__':
    robert = User("robert")
    john = User("john")

    robert.send_msg("hello! I am rebert.")
    john.send_msg("i love you robert")