from time import sleep

peopleDictionary = {
    '1111111111': 'Amal',
    '2222222222': 'Mohammed',
    '3333333333': 'Khadijah',
    '4444444444': 'Abdullah',
    '5555555555': 'Rawan',
    '6666666666': 'Faisal',
    '7777777777': 'Layla'
}


def is_valid_phone_number(phone_number: str) -> bool:
    return len(phone_number) == 10 and phone_number.isdigit()


def find_person(phone_number: str) -> str:
    return peopleDictionary.get(phone_number, 'Number not found')


def main() -> None:
    while True:
        if input("Enter 'ok' to add a new person or anything else to continue\n-->").lower() == "ok":
            name_of_the_person = input("Name of the person -->")
            person_number = input("Person number -->")

            if is_valid_phone_number(person_number):
                peopleDictionary[person_number] = name_of_the_person
            else:
                print("Invalid number. Please enter a 10-digit number.")
        else:
            for number, name in peopleDictionary.items():
                print(f"Number --> {number}, Name --> {name}")
            break

    person_number_to_find = input("Enter the phone number to find --> ")

    if is_valid_phone_number(person_number_to_find):
        result = find_person(person_number_to_find)
        print(result)
    else:
        print("Invalid number. Please enter a 10-digit number.")


if __name__ == "__main__":
    main()
    sleep(2)
