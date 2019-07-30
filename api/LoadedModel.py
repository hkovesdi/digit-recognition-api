import tensorflow as tf
from keras import backend as K
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json

#K.clear_session()
global graph
graph = tf.get_default_graph()
json_file = open('/app/model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("/app/model.h5")
print("Loaded model from disk")
loaded_model._make_predict_function()
loaded_model.compile(loss='categorical_crossentropy',optimizer='adam', metrics=['accuracy'])