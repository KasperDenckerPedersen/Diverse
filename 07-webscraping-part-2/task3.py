import requests
import json

def get_data(start):
    url = "https://www.boligportal.dk/api/search/list"

    querystring = {"offset": start}

    payload = "{\"categories\":{\"values\":null},\"city_level_1\":{\"values\":[\"aarhus\"]},\"city_level_2\":{\"values\":null},\"city_level_3\":{\"values\":null},\"rooms\":null,\"min_size_m2\":null,\"max_monthly_rent\":null,\"min_rental_period\":null,\"max_available_from\":\"\",\"company_filter_key\":null,\"company_key\":null,\"street_name\":{\"values\":null},\"social_housing\":null,\"min_lat\":null,\"min_lng\":null,\"max_lat\":null,\"max_lng\":null,\"shareable\":false,\"furnished\":false,\"student_only\":false,\"pet_friendly\":false,\"balcony\":false,\"senior_friendly\":false,\"parking\":false,\"elevator\":false,\"electric_charging_station\":null,\"dishwasher\":null,\"dryer\":null,\"washing_machine\":null,\"newbuild\":null,\"include_units\":true,\"order\":\"DEFAULT\"}"

    response = requests.request("POST", url, data=payload, params=querystring)

    data = json.loads(response.text)

    #search = {'city': 'Aarhus'}
    #city = htmlDocument.find('fin-streamer', search).text.strip()

    return data

boligere = []
number_results = 0

for i in range(1, 5):
    data = get_data(i)
    boligere.extend(data['results'])
    number_results = data['result_count']

search = input("What city do you want to search for?\n>")

for bolig in boligere:
    if bolig['city'] == search:
        print(f"City: {bolig['city']}")
        print(f"Area: {bolig['city_area']}")
        print(f"Monthly rent: {bolig['monthly_rent']}")
        print(f"Deposit: {bolig['deposit']}")
        print()
    else:
        print("Nothing matches the search")

print(f"Number of results: {number_results}")