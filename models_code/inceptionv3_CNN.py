from tensorflow.keras import layers, models
from tensorflow.keras.applications import InceptionV3
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import Precision, Recall, AUC

class InceptionV3_CNN:

    def __init__(self, num_classes, img_size, channels, name="inception"):
        self.name = name
        self.num_classes = num_classes
        self.input_width_height = img_size
        self.channels = channels
        self.input_type = 'images'

    def build(self):
        base_model = InceptionV3(input_shape=(self.input_width_height,
                                             self.input_width_height,
                                             self.channels), include_top=False)

        # Add custom top layers for classification
        x = base_model.output
        x = layers.GlobalAveragePooling2D()(x)
        x = layers.Dense(1024, activation='relu')(x)
        predictions = layers.Dense(self.num_classes, activation='softmax')(x)
 
        model = models.Model(inputs=base_model.input, outputs=predictions)

        # Compile the model
        opt = Adam(learning_rate=0.00001) #originally tried with 0.0001 

        # Compile the model
        model.compile(optimizer=opt,
                    loss='categorical_crossentropy',
                    metrics=['acc', Precision(name="prec"), Recall(name="rec"), AUC(name='auc')])
       
        return model
    