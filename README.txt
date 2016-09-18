
Software capable of identifying the name of a brand/company/application from an image containing the logo of a famous brand, company or application.

Install Tensorflow
https://www.tensorflow.org/versions/r0.9/get_started/os_setup.html

TensorFlow for Poets
https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/#0

Install Docker

Get the database
Download the database with the screenshots in the 'BankPhishing' directory
make data directory: mkdir data
run: python makeDB.py in order get the classes from BankPhishing in the data folder(also the images need crop of the logo just)

run docker container
docker run -it -v /path/to/files/BLRS/:/tf_files_blrs  gcr.io/tensorflow/tensorflow:latest-devel

train the model

cd /tensorflow
git pull

python tensorflow/examples/image_retraining/retrain.py \
--bottleneck_dir=/tf_files_blrs/bottlenecks \
--how_many_training_steps 1000 \
--model_dir=/tf_files_blrs/inception \
--output_graph=/tf_files_blrs/retrained_graph.pb \
--output_labels=/tf_files_blrs/retrained_labels.txt \
--image_dir /tf_files_blrs/data


query the model

python /tf_files_blrs/label_image.py /tf_files_blrs/BankPhishing/ing.jpg



