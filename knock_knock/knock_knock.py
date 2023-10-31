class KnockKnock:
    def react_to_user(self):
        while True:
            user_input = input("> ")
            if "Who" in user_input:
                print("Cow")
                break
            if "Cow" in user_input:
                print("Cow don't whoo, cow moo! :-D")
                break
            
            
    def decider(self):
        while True:
            first_input = input("> ").upper()
            if first_input == "NO":
                print("Sorry to hear... :-(")
                break
            else:
                print("Great!\n'Knock knock!?!'")
                self.react_to_user()

