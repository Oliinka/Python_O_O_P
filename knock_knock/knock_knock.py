class KnockKnock:
    
    def decider(self):
        while True:
            user_input = input("> ").lower()
            if user_input == "no":
                print("Sorry to hear... :-(")
                break
            elif user_input == "yes":
                print("Great.\nKnock knock!?!")
    
            elif "there" in user_input.lower():
                print("Cow")
            elif "cow" in user_input.lower():
                print("Cow don't who cow moo.")
                break
            else:
                print("Pleas repeat your question...")
