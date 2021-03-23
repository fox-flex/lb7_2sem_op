""" module for working with documents """


class DocumentError(Exception):
    pass


class GoOutOfDoc(DocumentError):
    pass


class WrongCharacterType(DocumentError, TypeError):
    pass


class WrongCharacterValue(DocumentError, ValueError):
    pass


class Document:
    """ class Document """
    def __init__(self):
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = ""

    def insert(self, character):
        """ insert character into position of cursor """
        if not hasattr(character, "character"):
            character = Character(character)
        self.characters.insert(self.cursor.position, character)
        self.cursor.forward()

    def delete(self):
        """ delete character into position of cursor """
        del self.characters[self.cursor.position]

    def save(self):
        """ save document into file """
        with open(self.filename, "w") as file_to_write:
            file_to_write.write("".join(self.characters))

    def __str__(self):
        return "".join(str(x.character) for x in self.characters)

    @property
    def string(self):
        """ convert class into str """
        return "".join((str(c) for c in self.characters))


class Cursor:
    """ class Cursor """
    def __init__(self, document):
        self.document = document
        self.position = 0

    def forward(self):
        """ increase position by 1 """
        if self.position < len(self.document.characters):
            self.position += 1
        else:
            raise GoOutOfDoc

    def back(self):
        """ reduce position by 1 """
        if self.position > 0:
            self.position -= 1
        else:
            raise GoOutOfDoc

    def home(self):
        """ go to the beginning of the line """
        while self.document.characters[self.position - 1].character != "\n":
            self.position -= 1
            if self.position == 0:
                # Got to beginning of file before newline
                break

    def end(self):
        """ go to the end of the line """
        while (self.position < len(self.document.characters)
               and self.document.characters[self.position].character != "\n"):
            self.position += 1


class Character:
    """ class Character """
    def __init__(self, character: str, bold=False,
                 italic=False, underline=False):
        if isinstance(character, str):
            if len(character) != 1:
                raise WrongCharacterValue('it should be exactly one character')
        else:
            raise WrongCharacterType('type of character should be str')
        self.character = character
        self.bold = bold
        self.italic = italic
        self.underline = underline

    def __str__(self):
        """ return str(self) """
        bold = "*" if self.bold else ""
        italic = "/" if self.italic else ""
        underline = "_" if self.underline else ""
        return bold + italic + underline + self.character


if __name__ == '__main__':
    doc = Document()
    doc.insert(Character('a', italic=True))
    doc.insert('b')
    doc.insert('\n')
    doc.insert('a')
    print(doc)
    print('__________')
    print(doc.string)
    print('__________')
