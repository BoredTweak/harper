class Release():
    releaseUrl: str
    releaseNotes: str
    version: str
    publishDate: str

    def to_json(self):
        return self.__dict__  
