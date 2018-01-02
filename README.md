## Synopsis

This program recongnizes the genre of a music by listening directly to the sound files. Once the program is run an output.txt file is obtained which contains the name of the songs and the genre of the music. This can be used by any individual to organize their music library or this can be used for building recommender systems. The model was trained using keras on tensorflow to obtain an accuracy of about 75% on the FMA dataset. 
## Usage


Use it as:

`python genre_classification location extension`

`python genre_classification.py data/genres mp3`



## Acknowledgements

* This project uses a lot of code from: https://github.com/deepsound-project/genre-recognition Many thanks to  Piotr Kozakowski & Bartosz Michalak
* The model was trained using an architecture very similar to http://benanne.github.io/2014/08/05/spotify-cnns.html
* The model was trained using the FMA small data set: https://github.com/mdeff/fma
* Model was trained and tested as part of the neural networks project of COMPSCI 682 at UMASS Amherst. https://compsci682.github.io/

## Contact info

Please contact me: nikhiltitusk@gmail.com if you need any more info.
## License

This code is released under MIT license: https://opensource.org/licenses/MIT