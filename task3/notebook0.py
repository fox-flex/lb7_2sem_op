"""
notebook class creation
"""
import datetime

LAST_ID = 0


class NotebookErr(Exception):
    pass


class DontFindNotebook(NotebookErr):
    pass


class Note:
    """
    Represent a note in the notebook.
    """
    def __init__(self, memo, tags=''):
        """
        Initialize a note with memo and optional space-separated tags.
        Automatically set the note's creation date and a unique id.
        """
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global LAST_ID
        LAST_ID += 1
        self.id = LAST_ID

    def match(self, filter0):
        """
        Determine if this note matches the filter text. Return True if matches,
        False otherwise. Search matches both-text and tags.
        """
        return filter0 in self.memo or filter0 in self.tags


class Notebook:
    """Represent a collection of notes that can be tagged,
    modified, and searched.
    """

    def __init__(self):
        """
        Initialize a notebook with an empty list.
        """
        self.notes = []

    def new_note(self, memo, tags=''):
        """
        Create a new note and add it to the list.
        """
        self.notes.append(Note(memo, tags))

    def modify_tags(self, note_id, tags):
        """
        Find the note with the given id and change its
        tags to the given value.
        """
        for note in self.notes:
            if note.id == note_id:
                note.tags = tags
                break

    def search(self, filter0):
        """
        Find all notes that match the given filter string.
        """
        return [note for note in self.notes if note.match(filter0)]

    def _find_note(self, note_id):
        """
        Locate the note with the given id.
        """
        for note in self.notes:
            if note.id == note_id:
                return note
        # return None
        raise DontFindNotebook

    def modify_memo(self, note_id, memo):
        """
        Find the note with the given id and change its
        memo to the given value.
        """
        try:
            self._find_note(note_id).memo = memo
        except DontFindNotebook:
            print('don\'t find any note with given note ID')
