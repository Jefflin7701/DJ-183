# Add more import statements as you need them!
from utility import get_four_choices
import billboard
from flask import session

"""
Our dictionary to hold which genres we are giving to our users. Play around with
this dictionary to see how the starter code changes on index.html. The keys
represent the names as they appear on the website, and the values represent the
chart IDs for Billboard to use.

TODO: Add at least two more genres to this dictionary. Information on how to find
      more Billboard chart IDs is on the Billboard library documentation, as
      linked on the core page of the spec. Make sure you only choose charts that
      contain SONGS (not artists, albums, etc.).
"""
GENRES_LIST = {
    "Hot 100": "hot-100",
    "Greatest of All Time Pop Songs": "greatest-of-all-time-pop-songs",
    "Dance Club Hits": "dance-club-play-songs",
    "RapCaviar": "hot-rap-tracks",
    "Holiday Songs": "hot-holiday-songs",
    "R&B": "r-and-b-songs",
    "Jazz Songs": "jazz-songs",
    "Rock Songs": "rock-songs",
    "Latin Songs": "latin-songs",
    "Canada's Hot 100": "canadian-hot-100"
}

"""
REQUIRES: a valid chart name that corresponds to a chart name on Billboard
MODIFIES: nothing
EFFECTS: chooses four random songs from the valid Billboard chart and returns
         result in a list. Uses get_four_choices() and the Billboard library.
         Remember: if you want to use a library in Python, what must we put at
         the top of the file to access its member functions?
"""

def get_four_songs(chart_name):
    CHOICE_LIST = []
    chart = billboard.ChartData(chart_name)
    choices = get_four_choices(chart)

    for x in choices:
        CHOICE_LIST.append(chart[x])
    return CHOICE_LIST


"""
REQUIRES: nothing
MODIFIES: session
EFFECTS: returns a string with the score to print, creates key in session if necessary

If the user has answered 3 questions, 1 correctly and 2 incorrectly,
get_score should return the STRING "1/3" .

If the user has not answered any questions yet,
get_score should return the string "N/A", but NOT the string"0/0".
"""
def get_score():
    if 'total' in session and 'correct' in session:
        pass
    else:
        session['total'] = 0
        session['correct'] = 0
    if 'total' in session and 'correct' in session:
        if session['total'] == 0:
            return 'N/A'
        else:
            return str(session.get('correct')) + "/" + str(session.get('total'))



"""
REQUIRES: nothing
MODIFIES: num_correct, num_total in session
EFFECTS: sets the num_correct and num_total to 0
"""
def clear_score():
    session.pop('total')
    session.pop('correct')
