import tensorflow as tf
from tensorflow.keras import layers, models

def RCNN():
	channel_axis = 3
	freq_axis = 1
	time_axis = 2
	input_shape = (96, 1366, 1)

	model = models.Sequential()

	model.add(tf.keras.Input(shape=input_shape))

	# Convolutional layers
	model.add(layers.ZeroPadding2D(padding=(0, 37)))
	model.add(layers.BatchNormalization(axis=time_axis, name='bn_0_freq'))

	model.add(layers.Conv2D(64, (3, 3), padding="same", activation="relu", name='conv1'))
	model.add(layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2), name='pool1'))
	model.add(layers.Dropout(0.1))

	model.add(layers.Conv2D(128, (3, 3), padding="same", activation="relu", name='conv2'))
	model.add(layers.MaxPooling2D(pool_size=(3, 3), strides=(3, 3), name='pool2'))
	model.add(layers.Dropout(0.1))

	model.add(layers.Conv2D(128, (3, 3), padding="same", activation="relu", name='conv3'))
	model.add(layers.MaxPooling2D(pool_size=(4, 4), strides=(4, 4), name='pool3'))
	model.add(layers.Dropout(0.1))

	model.add(layers.Conv2D(128, (3, 3), padding="same", activation="relu", name='conv4'))
	model.add(layers.MaxPooling2D(pool_size=(4, 4), strides=(4, 4), name='pool4'))
	model.add(layers.Dropout(0.1))
	model.add(layers.Reshape((15, 128)))

	# GRU
	model.add(layers.GRU(32, return_sequences=True, name='gru1'))
	model.add(layers.GRU(32, return_sequences=False, name='gru2'))
	model.add(layers.Dropout(0.3))

	model.add(layers.Dense(10, activation='sigmoid', name='output'))

	return model
	
def load_model(path):
	loaded_model = models.load(path)
	return loaded_model