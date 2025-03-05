import json
import os

def load_profiles(directory): 
    profiles = []
    for f in os.listdir(directory) : 
        file_path = os.path.join(directory, f) 
        with open(file_path, 'r') as file:
            profiles.append(json.load(file))
            
    return profiles 
