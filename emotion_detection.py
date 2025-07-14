import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, headers=headers, json=payload)
    response_json = response.json()

    # Extract emotion scores
    emotion_data = response_json["emotionPredictions"][0]["emotion"]

    # Pull only required emotions
    anger = emotion_data.get("anger", 0)
    disgust = emotion_data.get("disgust", 0)
    fear = emotion_data.get("fear", 0)
    joy = emotion_data.get("joy", 0)
    sadness = emotion_data.get("sadness", 0)

    # Determine dominant emotion
    emotions = {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness
    }
    dominant_emotion = max(emotions, key=emotions.get)

    # Build result dictionary
    result = {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant_emotion
    }

    return result
