# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

# DATA STRUCTURES AND ALGORITHMS
# ASSIGNMENT NO. 3
# PROGRAMMED BY: Nikka Pauline D. Generalao
# BSCOE 2-2

# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
# personal data
personal_data = {}
info = {}

# display a menu options
def menu():
      print("\n           \033[1;3mBRGY. 143 CONTACT TRACING\033[0m")
      print("\n-------------------- MENU ----------------------\n"
            "|                                              |\n"
            "|   (1) -> Add an Item                         |\n"
            "|   (2) -> Search                              |\n"
            "|   (3) -> Exit                                |\n"
            "|                                              |\n"
            "------------------------------------------------")

# perform the selected option
##  Option 1 Ask the personal data for Add an Item Option
def add():
      print("\n==============================================\n"
            "||     \033[1;3mCONTACT TRACING INFORMATION FORM\033[0m     ||\n"
            "==============================================\n")

      full_name = input("Enter full name (FN, M.I., SN): ")
      email = input("Enter active email address: ")
      phone = input("Enter your active phone number: ")
      address = (input("Enter your current address: "))
      emergency_name = (input("Name of the person to call in case of emergency (FN, M.I., SN): "))
      emergency_contact = (input("Enter the emergency contact active phone number: "))
      diagnosed = (input("Are you diagnosed with COVID-19? (Yes/No): "))
      symptoms = (input("Have you shown symptoms of COVID-19? (Yes/No): "))
      public_place = (input("Have you recently been in a public or crowded place?: "))
      where = (input("Where? Enter complete address: "))

      info["Email Address"] = email
      info["Phone Number"] = phone
      info["Address"] = address
      info["Name of Emergency Contact Person"] = emergency_name
      info["Emergency Contact Phone Number"] = emergency_contact
      info["Diagnosed with COVID-19"] = diagnosed
      info["Shown Symptoms of COVID-19"] = symptoms
      info["Recently been in a Public or Crowded Place"] = phone
      info["Public Place Location"] = where
      personal_data[full_name] = info

##  Option 2 Search by full name
def search():
      print("\n==============================================\n"
            "||     \033[1;3mSEARCH OUR CONTRACT TRACING SYSTEM\033[0m   ||\n"
            "==============================================\n")

      name = input("Enter full name: ")
      if name in personal_data:
            convert_key = list(info.keys())
            convert_value = list(info.values())
            separator_key = " " * 5
            separator_value = " " * 10
            for key in personal_data.keys():
                  print("\n               ||  Showing information of ", key, "  ||")
            print("=============================================================================================\n")
            for convert_key, convert_value in zip(convert_key, convert_value):
                  print(f"{convert_key : >42}", ":", convert_value)
            print("\n=============================================================================================")
      else:
            print("\n==================================================\n"
                  "||     \033[1;3mThis name doesn't exist in our system\033[0m    ||\n"
                  "==================================================\n")



# allow use to select item in the menu, check of valid
while True:
      menu()

      select_item = input("\nWhat do you want to do?: ")
      if select_item in ("1", "2", "3"):
            if select_item == "1":
                  add()
                  print("\n===================================================================================================\n"
                        "||   Your information has been added!!                                                           ||\n"
                        "||                                                                                               ||\n"
                        '||\033[1;3m' + '   We will not, in any circumstances, share your personal information with other' + '\033[0m               ||\n'
                        '||\033[1;3m' + '   individuals or organizations without your permission, including public organizations,' + '\033[0m       ||\n'
                        '||\033[1;3m' + '   corporations or individuals, except when applicable by law.' + '\033[0m                                 ||\n'
                        "||                                                                                               ||\n"
                        "||   Thank you and stay safe!!                                                                   ||\n"
                        "===================================================================================================")

            elif select_item == "2":
                  search()

            ##  Option 3 Ask the user if they want to exi
            elif select_item == "3":
                  exit = input("Do you want to exit? (y/n): ")
                  if exit == "y":
                        print("Thank you. Stay safe!")
                        break
                  elif exit == "n":
                        continue
                  else:
                        print(">>> Enter a valid answer <<<")

      else:
            print("\n>>> I'm sorry. You entered an invalid number <<<")
            try_again = input("\nWould you like to try again? (y/n): ")
            if try_again == "y":
                  continue

            elif try_again == "n":
                  break

            else:
                  print("\n>>> Please try again some other day. <<<")
