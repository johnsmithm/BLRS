
Software capable of identifying the name of a brand/company/application from an image containing the logo of a famous brand, company or application.

Install Tensorflow
https://www.tensorflow.org/versions/r0.9/get_started/os_setup.html

the model should be train as follow:
python train.py <images/path> <model/save/to>
<images/path> - the path to read the images, each folder in the path will be a class, and the images from that folder will be the samples.
<model/save/to> - we will save the weigths of the cnn to a file in order to not train the model every time

we will query the model using :
python <path/to/model> <path/to/folder>
or
python <path/to/model> <path/to/image>
or
python <path/to/model> <path/to/file.txt>
<path/to/model> path to the weigths
folder/image/file.txt will be the image/images to clasify
