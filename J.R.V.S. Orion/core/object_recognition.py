import cv2
import numpy as np
import tensorflow as tf

class ObjectRecognizer:
    def __init__(self, model_path="ssd_mobilenet_v2.pb", label_map_path="label_map.txt"):
        # Załaduj model TensorFlow
        self.model = tf.saved_model.load(model_path)
        with open(label_map_path, "r") as f:
            self.labels = {i: line.strip() for i, line in enumerate(f.readlines())}

    def recognize(self, frame):
        """Rozpoznaje obiekty na podstawie klatki."""
        input_tensor = tf.convert_to_tensor(frame)
        input_tensor = input_tensor[tf.newaxis, ...]

        detections = self.model(input_tensor)
        detection_classes = detections["detection_classes"].numpy()[0].astype(np.int32)
        detection_scores = detections["detection_scores"].numpy()[0]

        recognized_objects = []
        for class_id, score in zip(detection_classes, detection_scores):
            if score > 0.5:  # Próg pewności
                recognized_objects.append(self.labels.get(class_id, "Unknown"))
        return recognized_objects
