def check_mood_friend(friend1, friend2):
    """ Lets see if you have two friends : Friend1 and Friend2.
         Based on friends mood it will decide if you are in troble

        - if friend1 is angry mood and friend2 is not angry, return "Safe"
        - if friend1 is not angry mood and friend2 is angry, return "Safe"
        - if both friends are angry, return "Trouble"

        - Here angry and not angry represented by True and False respectively.
        - where True means angry and False means not angry.

        Here, we are using ternary operator.
    
     """
    return "Trouble" if friend1 and friend2 else "Safe"

if __name__ == "__main__":
    friend1 = input("Is Friend1 angry? (True/False): ").strip().lower() == 'true'
    friend2 = input("Is Friend2 angry? (True/False): ").strip().lower() == 'true'

    print(f"Based on the mood of your friends, you are in: {check_mood_friend(friend1, friend2)}.")
