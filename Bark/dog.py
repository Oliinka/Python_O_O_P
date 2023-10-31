class Dog:
    def react_to_user_input(self):
        while True:
            user_input = input("> ")

            if user_input.lower() == "exit":
                print("Good bye!")
                break
            if "Rex" in user_input:
                print("Yes, haf, haf!")
                break
            else:
                print("No, vrr haf haf!!!")