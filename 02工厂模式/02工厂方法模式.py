from abc import ABCMeta, abstractmethod


class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass


class PersonalSection(Section):
    def describe(self):
        print('Personal section')


class AlbumSection(Section):
    def describe(self):
        print('album section')


class PatentSection(Section):
    def describe(self):
        print('patent section')


class PublicationSectioin(Section):
    def describe(self):
        print('publiccation section')


class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        pass

    def getSections(self):
        return self.sections

    def addSection(self, section):
        self.sections.append(section)

    def showSections(self):
        for s in self.sections:
            s.describe()


class Linkedin(Profile):
    def createProfile(self):
        self.addSection(PersonalSection())
        self.addSection(PatentSection())
        self.addSection(PublicationSectioin())


class Facebook(Profile):
    def createProfile(self):
        self.addSection(PersonalSection())
        self.addSection(AlbumSection())


if __name__ == '__main__':
    eval('Facebook')().showSections()
    eval('Linkedin')().showSections()
