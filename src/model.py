from tensorflow.keras import models, layers

def build_cnn(input_shape=(128, 128, 3), num_classes=2, dropout_rate=0.5):
    """
    Builds a CNN model.
    
    Args:
        input_shape: tuple, input image shape.
        num_classes: int, number of output classes.
        dropout_rate: float, dropout rate to prevent overfitting.
    
    Returns:
        model: compiled Keras model
    """
    model = models.Sequential([
        layers.Conv2D(32, (3,3), activation='relu', input_shape=input_shape),
        layers.MaxPooling2D((2,2)),

        layers.Conv2D(64, (3,3), activation='relu'),
        layers.MaxPooling2D((2,2)),

        layers.Conv2D(128, (3,3), activation='relu'),
        layers.MaxPooling2D((2,2)),

        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dropout(dropout_rate),
        layers.Dense(num_classes, activation='softmax')
    ])
    
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',  # works with integer labels
        metrics=['accuracy']
    )
    
    return model
