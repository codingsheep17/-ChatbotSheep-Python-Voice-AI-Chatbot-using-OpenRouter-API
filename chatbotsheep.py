#Welcome To chatbotsheep by codingsheep17 (SYED HASEEB SHAH)

#Importing modules
import requests
import speech_recognition as sr
import pyttsx3

#class and methods
class ChatBot:
        
        #adding run instead of __init__ to make it reuseable
        def run(self):
            self.api_key = "YOUR_OPEN_ROUTER_API_KEY_HERE"
            print(self.api_key)
            self.api_handling()
            self.speech_getting()

        def api_handling(self):
            self.url = "https://openrouter.ai/api/v1/chat/completions"
            self.headers = {
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
            }

        def speech_getting(self):
            try:         
                self.r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Say something...")
                    print("Listening for 5 seconds. Speak now...")
                    self.question = self.r.listen(source, timeout=5, phrase_time_limit=10)
                    try:
                        #final question asked by speaker
                        self.text = self.r.recognize_google(self.question)
                    except sr.UnknownValueError:
                        print("Sorry, I couldn't understand you.")
                    except sr.RequestError:
                        print("API not working or Check Your Internet.")
                self.api_response()
            except Exception as e:
                print(f"Error {e}")

        def api_response(self):
            #user can be replaced with the name of yours 
            self.data = {
                    "model": "openai/gpt-3.5-turbo",
                    "messages": [{"role": "user", "content": f"{self.text}"}]
            }
            self.res = requests.post(self.url, headers=self.headers, json=self.data)
            self.res_json = self.res.json()
            if "choices" in self.res_json:
                self.command = self.res_json["choices"][0]["message"]["content"]
            else:
                print("❌ API Error:", self.res_json)
                return
            self.voice_response()

        def voice_response(self):
            self.engine = pyttsx3.init()
            print("Bot Response...")
            self.engine.setProperty('rate', 130) # Example: setting rate to 130 words per minute
            self.engine.say(self.command)
            self.engine.runAndWait()

while True:
    chatbot = ChatBot()
    chatbot.run()
    choice = input("Do you want to continue? (y/n): ").lower()
    if choice == 'n' or choice == 'no':
        print("👋 Exiting... Allah Hafiz!")
        break