import speech_recognition as sr

class SpeechHandler:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

        #check for background noise
        print("Adjusting for background noise...")
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
        print("Ready for voice commands!")

    def listen_for_command(self, timeout=8):
        """
            Listen for voice commands and return text
        """
        try:
            print("Listening... Say your command!")
            
            with self.microphone as source:
                audio = self.recognizer.listen(source, timeout=timeout)


            print("processing you command...")

            command = self.recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        
        except sr.WaitTimeoutError:
            print("No speech detected. Please try again.")
            return None
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that. please try again")
            return None
        except sr.RequestError as e:
            print(f"Error with speech service: {e}")

class VoiceCommandMapper:
    def __init__(self):
        self.offensive_commands = {
            # Hassan's offensive moves
            "turbo start": "Turbo Start",
            "start": "Turbo Start",
            "mercedes charge": "Mercedes Charge", 
            "mercedes": "Mercedes Charge",
            "charge": "Mercedes Charge",
            "corner mastery": "Corner Mastery",
            "corner": "Corner Mastery",
            "mastery": "Corner Mastery",
            
            # Alternative pronunciations
            "turbo boost":     "Turbo Start",
            "mercedes attack": "Mercedes Charge",
            "corner expert":   "Corner Mastery"
        }

        self.defensive_commands = {
            # Hassan's defensive moves
            "slipstream cut": "Slipstream Cut",
            "slipstream": "Slipstream Cut", 
            "cut": "Slipstream Cut",
            "aggressive block": "Aggressive Block",
            "aggressive": "Aggressive Block",
            "block": "Aggressive Block",
            
            # Alternative pronunciations
            "slip":    "Slipstream Cut",
            "defense": "Slipstream Cut",
            "defend":  "Slipstream Cut"
        }
    
    def map_offensive_command(self, voice_command):
        for keyword, move_name in self.offensive_commands.items():
            if keyword in voice_command:
                return move_name
        return None
    
    def map_defensive_command(self, voice_command):
        for keyword, move_name in self.defensive_commands.items():
            if keyword in voice_command:
                return move_name
        return None
    
    def get_available_commands(self):
        """Return list of available voice commands"""
        print("\nAVAILABLE VOICE COMMANDS:")
        print("\nOFFENSIVE MOVES:")
        print("- Say 'Turbo Start' or 'start'")
        print("- Say 'Mercedes Charge' or 'Mercedes' or 'charge'") 
        print("- Say 'Corner Mastery' or 'Corner' or 'corner expert'")
        
        print("\nDEFENSIVE MOVES:")
        print("- Say 'Slipstream Cut' or 'Slipstream' or 'cut'")
        print("- Say 'Aggressive Block' or 'Block'")
        
        print("\nTIP: Speak clearly!!")