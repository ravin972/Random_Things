import requests
import random
import string

while True:
    # Generate a random name of length between 5 and 10 characters
    random_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5, 10)))

    # Generate random values for first_name, last_name, and phone
    random_first_name = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(5, 10)))
    random_last_name = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(4, 8)))
    random_phone = ''.join(random.choice(string.digits) for _ in range(10))

    # Construct the payload with the random values
    payload = {
        "first_name": random_first_name,
        "last_name": random_last_name,
        "email": f"{random_name}@nangia-andersen.com",
        "phone": random_phone,
        "code": "",
        "country": "IN",
        "region": "",
        "zip": "110008",
        "title": "consultant",
        "company": "nangia andersen",
        "consentOptIn": True,
        "essentialsOptIn": False,
        "pid": "",
        "alert_email": "",
        "apps": ["expert"],
        "companySize": "100-249",
        "preferredSiteId": "",
        "tempProductInterest": "Nessus Expert",
        "partnerId": "",
        "gclid": ""
    }

    url = "https://www.tenable.com/evaluations/api/v1/nessus-expert"

    # Send the POST request
    response = requests.post(url, json=payload)

    # Check the response status
    if response.status_code == 200:
        print(f"Email: {random_name}@nangia-andersen.com")
        user_input = input("Press Enter to generate a new email, or any other key to exit: ")
        if user_input != "":
            break  # Exit the loop if the user enters any key other than Enter
    else:
        print("Request failed.")
        break  # Exit the loop if the request fails