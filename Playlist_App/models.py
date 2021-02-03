"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""

    __tablename__ = "playlists"

    def __repr__(self):
        p = self
        return f"<Playlist id={p.id}, name={p.name}, description={p.description}>"

    id = db.Column(db.Integer,
            primary_key=True,
            autoincrement=True)

    name = db.Column(db.String(30),
            nullable=True)
    
    description = db.Column(db.String)

    playlist = db.relationship('PlaylistSong', backref="playlist")
    songs = db.relationship('Song', secondary="playlist_songs", backref="playlists")
    
class Song(db.Model):
    """Song."""

    __tablename__ = "songs"

    def __repr__(self):
        s = self
        return f"<Song id={s.id}, title={s.title}, artist={s.artist}>"

    id = db.Column(db.Integer,
            primary_key=True,
            autoincrement=True)

    title = db.Column(db.String(30))
    
    artist = db.Column(db.String(30))

    song = db.relationship('PlaylistSong', backref="song")


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    __tablename__ = "playlist_songs"

    def __repr__(self):
        ps = self
        return f"<PlaylistSong id={ps.id}, playlist_id={ps.playlist_id}, song_id={ps.song_id}>"

    id = db.Column(db.Integer,
            primary_key=True,
            autoincrement=True)

    playlist_id = db.Column(db.Integer,
            db.ForeignKey('playlists.id'))
    
    song_id = db.Column(db.Integer,
            db.ForeignKey('songs.id'))



# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

