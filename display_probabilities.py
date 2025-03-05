def display_probabilities(probabilities): 
    for company, languages in probabilities.items(): 
        for language, probability in languages.items(): 
            print(f"P({language}|{company}) = {probability}")