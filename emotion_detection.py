import json
import requests

def emotion_detector(text_to_analyze):
    ''' Send the emotion detection request and return the results
    '''

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/' /
          'NlpService/EmotionPredict'

    myobj = {"raw_document": {"text": text_to_analyze}}

    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json=myobj, headers=header, timeout=10)

    formatted_response = json.loads(response.text)
    emotion_scores = formatted_response["emotionPredictions"][0]['emotion']
    return {
        'anger': emotion_scores["anger"],
        'disgust': emotion_scores["disgust"],
        'fear': emotion_scores["fear"],
        'joy': emotion_scores["joy"],
        'sadness': emotion_scores["sadness"],
        'dominant_emotion': max(emotion_scores, key=emotion_scores.get)
    }
