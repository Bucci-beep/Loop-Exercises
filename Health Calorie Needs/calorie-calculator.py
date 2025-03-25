# Store each person's details in a dictionary
people = [
    {
        "name": "Alice",
        "weight":65,
        "height": 165,
        "age": 30,
        "gender":"female",
        "activity": "moderately active"
    },
    {
        "name": "Bob",
        "weight": 80,
        "height": 180,
        "age": 37,
        "gender": "male",
        "activity": "lightly active"
    },
    {
        "name": "Peris",
        "weight": 80,
        "height": 180,
        "age": 25,
        "gender": "female",
        "activity": "sedentary"
    },
    {
        "name": "Chaska",
        "weight": 60,
        "height": 170,
        "age": 25,
        "gender": "male",
        "activity": "very active"
    }
]

# Define activity multipliers
activity_multipliers = {
    "sedentary": 1.2,
    "lightly_active": 1.375,
    "moderately active": 1.55,
    "very active": 1.725
}

#Calculate the BMR for both sexes
def calculate_bmr(person):
    weight = person["weight"]
    height = person["height"]
    age = person["age"]
    gender = person["gender"]

    if gender.lower() == "male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    elif gender.lower() == "female":
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    else:
        raise ValueError("Gender must be 'male' or 'female'")

    return bmr

for person in people:
    try:
        bmr = calculate_bmr(person)
        multiplier = activity_multipliers.get(person["activity"].lower(), None)

        if multiplier is None:
            print(f"Unknown activity level for {person['name']}.")
            continue

        daily_calories = bmr * multiplier
        print(f"{person['name']} needs approximately {daily_calories:.2f} calories per day.")
    except ValueError as e:
        print(f"Error for {person['name']}: {e}")


