import datetime

# Store the next availabale id for all new notes
last_id = 0


class Note:
    """Represent a note in teh notebook.
     Match against a string in searches and store tags for each note"""

    def __init__(self, memo, tags=""):
        """Inititalize a note with memo and optional
        space-separated tags. Automatically set the note's createion date and a unique id."""
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_idea += 1
        self.id = last_idea

    def match(self, filter):
        """Determine if this note matches the filter
        text. Return True if it matches, False otherwise."""
        
        """Search is case sensitive and matches both text and tags."""
        return filter in self.memo or filter in self.tags


