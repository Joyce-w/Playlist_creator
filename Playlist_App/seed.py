from models import Playlist, Song, PlaylistSong, db
from app import app


#create all tables
db.drop_all()
db.create_all()



s1 = Song(title="Somewhere over the Rainbow", artist="Israel Kamakawiwo'ole")
s2 = Song(title="I'm Yours", artist="Jason Mraz")
    
db.session.add(s1)
db.session.add(s2)

p1 = Playlist(name="Ukeleles/Guitars", description="Guitars & ukelele songs!")

db.session.add(p1)

ps1 = PlaylistSong(playlist_id=1, song_id=1)
ps2 = PlaylistSong(playlist_id=1, song_id=2)

db.session.add(ps1)
db.session.add(ps2)

db.session.commit()