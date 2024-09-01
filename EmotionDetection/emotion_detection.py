import requests

def emotion_detector(text_to_analyze):
    if text_to_analyze == "":
        return {'anger' : None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze }}
    response = requests.post(url, json=input_json, headers=headers)
    emotions = response.json()
    emotion = emotions.get("emotionPredictions")[0].get("emotion")
    anger_score = emotion.get("anger")
    disgust_score = emotion.get("disgust")
    fear_score = emotion.get("fear")
    joy_score = emotion.get("joy")
    sadness_score = emotion.get("sadness")
    dominant_emotion = "joy"
    if (anger_score>joy_score) and (anger_score>disgust_score) and \
       (anger_score>fear_score) and (anger_score>sadness_score):
       dominant_emotion = "anger"
    elif (disgust_score>joy_score) and (disgust_score>anger_score) and \
       (disgust_score>fear_score) and (disgust_score>sadness_score):
       dominant_emotion = "disgust"
    elif (fear_score>joy_score) and (fear_score>anger_score) and \
       (fear_score>disgust_score) and (fear_score>sadness_score):
       dominant_emotion = "fear"
    elif (joy_score>fear_score) and (joy_score>anger_score) and \
         (joy_score>disgust_score) and (joy_score>sadness_score):
       dominant_emotion = "joy"
    elif (sadness_score>fear_score) and (sadness_score>anger_score) and \
       (sadness_score>disgust_score) and (sadness_score>joy_score):
       dominant_emotion = "sadness"
    return {
                'anger' : anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion
    }