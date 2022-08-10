from time import sleep
peopleDictionary = {'1111111111': 'Amal', '2222222222': 'Mohammed', '3333333333': 'Khadijah', '4444444444': 'Abdullah', '5555555555': 'Rawan', '6666666666': 'Faisal', '7777777777': 'Layla'}



def Check_The_Number(phone_number:str) -> bool:
     return len(phone_number)==10 and phone_number.isdigit()

def Check_The_Dictionary(phone_number:str) -> str:
    for number in peopleDictionary:
        if number == phone_number:
            return peopleDictionary.get(phone_number,False)

def main() -> None:

    while True:
         if input("Enter ok to add a new person or put anything to continue\n-->").lower()=="ok":

            NameOfThePerson = input("name of the person-->")

            PersonNumber = input("person number -->")

            peopleDictionary.update({ PersonNumber : NameOfThePerson }) 
         else:

            for number ,name in peopleDictionary.items():
                print(f"number -->  {number}, name --> {name}")
            break
            
    PersonNumber2 = input(" phone_number ==> ")  
    
    if Check_The_Number(PersonNumber2): 

        name_or_False = Check_The_Dictionary(PersonNumber2)    

        if name_or_False : print(name_or_False)

        else:
            print("Sorry, the number is not found")
    else:
        print("This is invalid number")




if __name__=="__main__":

        main()
        sleep(2)

