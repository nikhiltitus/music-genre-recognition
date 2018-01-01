import os
import numpy as np
from common import load_track
import fnmatch
import matplotlib
matplotlib.use('Agg')
import librosa as lbr
import pickle

DEFAULT_SHAPE=(647,128)
class GenreClassifier:
    def __init__(self,data_set_path):
        ##
        self.data_set_path=data_set_path
        self.file_meta=file = open('meta.txt','w')

    def create_data_pickle(self):
        output=np.array([])
        id=1
        for root, dirnames, filenames in os.walk(self.data_set_path):
            for filename in fnmatch.filter(filenames, '*.au'):
                full_file_path=os.path.join(root, filename)
                print('Processing '+full_file_path)
                self.file_meta.write(str(id)+'|'+full_file_path+'\n')
                mel_output,_=load_track(full_file_path,DEFAULT_SHAPE)
                mel_output=np.expand_dims(mel_output, axis=0)
                if output.shape[0] == 0:
                    output=mel_output
                else:
                    output=np.vstack((output,mel_output))
        print(output.shape)
        return output


genre_classifier=GenreClassifier('../genre-recognition-master/data/genres/rock')
genre_classifier.create_data_pickle()

