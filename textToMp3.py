url = 'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/2a390b5b-a390-4885-b3ef-ebb1f5a9dde5'
apikey = 'Ys509onC49Ss3nN-T2arKXHxuHdWrAohSsZxQ72oCXYh'

from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Setup Service
authenticator = IAMAuthenticator(apikey)
# New TTS Service
tts = TextToSpeechV1(authenticator=authenticator)
# Set Service URL
tts.set_service_url(url)


with open('text.txt','r') as f:
    text = f.read()
    

with open('voice.mp3','wb') as audio_file:
    res = tts.synthesize(text, accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
    audio_file.write(res.content)