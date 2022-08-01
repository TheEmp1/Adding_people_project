
People_Dictionary={'1111111111': 'Amal', '2222222222': 'Mohammed', '3333333333': 'Khadijah', '4444444444': 'Abdullah', '5555555555': 'Rawan', '6666666666': 'Faisal', '7777777777': 'Layla'}



def check_the_number(phone_number:str) -> bool:
     return len(phone_number)==10 and phone_number.isdigit()

def check_the_dictionary(phone_number:str) -> str:
    for number in People_Dictionary:
        if number==phone_number:
            return People_Dictionary.get(phone_number,False)

def main() -> None:

    while True:
         if input("Enter ok to add a new person or put anything to continue\n-->").lower()=="ok":

            Name_of_the_person=input("Name of the person-->")

            person_number=input("person number -->")

            People_Dictionary.update({person_number:Name_of_the_person})
         else:

            for number ,name in People_Dictionary.items():
                print(f"number -->  {number}, name --> {name}")
            break
            
    phone_number=input(" phone_number ==> ")
    if check_the_number(phone_number):
        name_or_False=check_the_dictionary(phone_number)    

        if name_or_False:print(name_or_False)

        else:
            print("Sorry, the number is not found")
    else:
        print("This is invalid number")




if __name__=="__main__":

        main()

