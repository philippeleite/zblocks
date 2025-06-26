class Field:
    def __init__(self, name: str,
                 offset: int,
                 length: int,
                 description: str,
                 content):
        self.name = name
        self.offset = offset
        self.length = length
        self.content = content
        self.description = description
