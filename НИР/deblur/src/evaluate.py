import numpy as np
from tensorflow.keras.models import load_model
from data_preparation import prepare_data

dataset_path = 'data'
defocused_train, defocused_test, motion_train, motion_test, sharp_train, sharp_test = prepare_data(dataset_path)

model = load_model('models/saved_model.h5')

loss, accuracy = model.evaluate(np.concatenate((defocused_test, motion_test)), 
                                np.concatenate((sharp_test, sharp_test)))
print(f'Test Loss: {loss}')
print(f'Test Accuracy: {accuracy}')
