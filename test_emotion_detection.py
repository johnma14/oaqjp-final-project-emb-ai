import unittest

from EmotionDetection import emotion_detection

class TestEmotionDetection(unittest.TestCase):
    def test_dominant_emotion_joy(self):
        emotion = emotion_detection.emotion_detector("I am glad this happened")
        self.assertEqual(emotion["dominant_emotion"], "joy")
    
    def test_dominant_emotion_znger(self):
        emotion = emotion_detection.emotion_detector("I am really mad about this")
        self.assertEqual(emotion["dominant_emotion"], "anger")

    def test_dominant_emotion_disgust(self):
        emotion = emotion_detection.emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(emotion["dominant_emotion"], "disgust")
    
    def test_dominant_emotion_sadness(self):
        emotion = emotion_detection.emotion_detector("I am so sad about this")
        self.assertEqual(emotion["dominant_emotion"], "sadness")
    
    def test_dominant_emotion_fear(self):
        emotion = emotion_detection.emotion_detector("I am really afraid that this will happen")
        self.assertEqual(emotion["dominant_emotion"], "fear")

if __name__ == "__main__":
    unittest.main()