
from tensorflow import keras
from keras import layers
import tensorflow as tf

class TensorFlow:
    def __init__(self):
        # self.saved_path = 'model_path_location'
        # self.model = tf.saved_model.load(self.saved_path)
        # self.predict = self.model.signatures["serving_default"] 
        pass

    def createModel(self):
        model = keras.Sequential([
        keras.layers.Conv2D(input_shape=(28,28,1), filters=8, kernel_size=3, 
                            strides=2, activation='relu', name='Conv1'),
        keras.layers.Flatten(),
        keras.layers.Dense(10, name='Dense')
        ])
        

    def preprocess(self, image):
        image = tf.image.resize(image, (self.image_size, self.image_size))
        
        return tf.cast(image, tf.float32) / 255.0
    
    def infer(self, image=None):
        tensor_image = tf.convert_to_tensor(image, dtype=tf.float32)
        tensor_image = self.preprocess(tensor_image)
        shape = tensor_image.shape
        tensor_image = tf.reshape(tensor_image,[1, shape[0],shape[1], shape[2]])
        return self.predict(tensor_image)['conv2d_transpose_4']
    
    def train(self):
        print(self.a)
        return 'abc train AI'