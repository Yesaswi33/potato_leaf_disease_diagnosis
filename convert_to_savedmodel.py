import tensorflow as tf

model = tf.keras.models.load_model(
    "/Users/yesaswimadabattula/Documents/potato_disease_detection/saved_models/potatoes_model/1/1.keras",
    compile=False
)

tf.saved_model.save(
    model,
    "/Users/yesaswimadabattula/Documents/potato_disease_detection/saved_models/potatoes_model/1"
)
