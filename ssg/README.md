To Train the ssg:

python train_ssg.py -i "data_folder" -b "batch_size" -e "number of epochs" -o "output folder"

To run the prediction:

python ssg_prediction.py -i "data_folder" -m "model_address" -th list_of_thresholds

To evaluate the predictions:

python evaluate_set_ssg.py -i "prediction file"