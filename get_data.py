def get_data(profiles): 
    employee_count = dict()
    company_languages = dict()

    for profile in profiles: 
        companies = profile.get("companies", [])
        languages = profile.get("skills", [])

        if len(companies) < 3:
            continue  

        for company in companies: 
            if company not in employee_count:
                employee_count[company] = 0
            employee_count[company] += 1

            if company not in company_languages:
                company_languages[company] = dict()

            for language in languages:
                if language not in company_languages[company]:
                    company_languages[company][language] = 0
                company_languages[company][language] += 1
    
    return company_languages, employee_count

