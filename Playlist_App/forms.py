"""Forms for playlist app."""

from wtforms import SelectField, StringField
from flask_wtf import FlaskForm


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField("Playlist Name")
    description = StringField("About this playlist..")


class SongForm(FlaskForm):
    """Form for adding songs."""

    title = StringField("Song name")
    artist = StringField("Artist")


# DO NOT MODIFY 
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
