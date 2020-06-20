
# MGR system
This code reproduces the work of **Albert Jiménez, Ferran José "MUSIC GENRE RECOGNITION WITH DEEP NEURAL NETWORKS".** and other models.

## Dataset 
GTZAN dataset. It includes the tags of blues, classical, country, disco, hiphop, jazz, metal, pop, reggae, rock.

## Usage 
Technology: Python 3.5+ with Flask and tensorflow2, and MySQL.

### Prerequisites:
- Have pip, virtualenv
- Install requirements.txt:
	Create environment: ```virtualenv env_mgc```
	Activate environment ```source env_song/bin/activate```
	Install dependencies ```	pip install -r requirements.txt```


#### How to run:
```
1. mysql>source Music_Genre_classification.sql
2. python run.py
```

### Test: 
>Hit url: [http://0.0.0.0:5001/[song_path]](http://0.0.0.0:5001/[song_path])
Example: [http://0.0.0.0:5001/classical.00018.wav](http://0.0.0.0:5001/classical.00018.wav)
Currently, the system merely classified songs in the folder dataset/set
