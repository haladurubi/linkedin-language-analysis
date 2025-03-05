def calculate_probabilities(company_languages, employee_count): 
    probabilities= dict()
    for company, languages in company_languages.items(): 
        for language in languages: 
            language_count = company_languages[company][language]
            employees = employee_count[company]
            probability = language_count/employees
            
            if company not in probabilities:
                probabilities[company] = {}
            probabilities[company][language]= probability
            
    return probabilities 