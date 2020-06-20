from flask import request, render_template, make_response
from datetime import datetime as dt
from flask import current_app as app
from .models import db, Song
from flask import jsonify 


@app.route('/<song_path>', methods=['GET'])
def get_song(song_path):
    song = Song.get_by_path(song_path)
    genre = ''
    if song==None:
        tags = ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']
        
        genre = Song.run_network(song_path)

        # song path does not exist
        if genre==None:
            return jsonify({
            'status': 0,
            'genre_id': None,
            'song_path':song_path,
            'message': 'Song does not exit in db'
            })

        
        new_song = Song(
            genre_id=str(tags[genre]),
            path=song_path
        ) 
        db.session.add(new_song)
        db.session.commit() 

        genre = str(tags[genre])
    else:
        genre = song.genre_id
    return jsonify({
            'status': 1,
            'genre_id': genre,
            'song_path':song_path,
            'message': 'genre classified'
            })