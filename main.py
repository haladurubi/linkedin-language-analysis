from calculate_probabilities import calculate_probabilities
from display_probabilities import display_probabilities
from get_data import get_data
from load_profiles import load_profiles

def main():
    directory = "profiles"  
    profiles = load_profiles(directory)
    company_languages, employee_count = get_data(profiles)
    probabilities = calculate_probabilities(company_languages, employee_count)
    display_probabilities(probabilities)

if __name__ == "__main__":
    main()