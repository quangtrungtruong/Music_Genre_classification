from . import db
import time
import h5py
import numpy as np
from application.network.utils import extract_melgram
import tensorflow as tf
from tensorflow import keras
from application.network.model import RCNN

class Song(db.Model):
    __tablename__ = 'song'
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.Unicode(255))
    genre_id = db.Column(db.Integer)

    def __init__(self, path, **params):
        self.path = path
        self.genre_id = params['genre_id'] if ('genre_id' in params) else None

    @staticmethod
    def get_by_path(path):
        return Song.query.filter_by(path=path).first()

    @staticmethod
    def run_network(path):
        LOAD_MODEL = 0
        LOAD_WEIGHTS = 1
        MULTIFRAMES = 0
        PARENT_PATH = 'dataset/test/'

        # load dataset and convert
        song_path = PARENT_PATH + path
        X_test, num_frames_test= extract_melgram(song_path, MULTIFRAMES)

        # define model
        #model = RCNN()
        
        #load model and weight
        model = keras.models.load_model('RCNN_model.h5')

        model.compile(optimizer='adam',
                      loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
                      metrics=['accuracy'])
        frame = X_test[0:1, :, :, :]
        frame = frame.reshape((1, 96, 1366, 1))

        probability_model = tf.keras.Sequential([model, 
                                                 tf.keras.layers.Softmax()])
        predictions = probability_model.predict(frame)
        result = np.argmax(predictions[0])

        return result
class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.Unicode(255))

    def __init__(self, tag, **params):
        self.tag = tag

    @staticmethod
    def get_by_id(id):
        return Genre.query.filter_by(id=id).first()