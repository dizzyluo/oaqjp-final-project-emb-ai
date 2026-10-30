import requests
import json

# def emotion_detector (text_to_analyze):
#     url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
#     headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
#     input = { "raw_document": { "text": text_to_analyze } }
#     r = requests.post(url, json=input, headers=headers)
#     if r.status_code == 200:
#         data = json.loads(r.text)
#         dominant = sorted(data['emotionPredictions'][0]['emotion'],  key=lambda k: data['emotionPredictions'][0]['emotion'][k])[-1]

#         emotion_payload = data['emotionPredictions'][0]['emotion']
#         emotion_payload['dominant_emotion'] = dominant
#         return emotion_payload
#     else:
#         print("Error")


def emotion_detector (text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input = { "raw_document": { "text": text_to_analyze } }
    r = requests.post(url, json=input, headers=headers)
    if r.status_code == 200:
        return r.json()
    else:
        print("Error")
