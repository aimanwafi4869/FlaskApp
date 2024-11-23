
from ultralytics import YOLO

class Ultralytics:

    def __init__(self):
        print('init')

    def createModel(self):
        pass
        

    # def preprocess(self, image):
    #     image = tf.image.resize(image, (self.image_size, self.image_size))
        
    #     return tf.cast(image, tf.float32) / 255.0
    
    # def infer(self, image=None):
    #     tensor_image = tf.convert_to_tensor(image, dtype=tf.float32)
    #     tensor_image = self.preprocess(tensor_image)
    #     shape = tensor_image.shape
    #     tensor_image = tf.reshape(tensor_image,[1, shape[0],shape[1], shape[2]])
    #     return self.predict(tensor_image)['conv2d_transpose_4']
    
    def train(self):
        train_results = self.model.train(
                                        data="coco8.yaml",  # path to dataset YAML
                                        epochs=100,  # number of training epochs
                                        imgsz=640,  # training image size
                                        device="cpu",  # device to run on, i.e. device=0 or device=0,1,2,3 or device=cpu

                                )