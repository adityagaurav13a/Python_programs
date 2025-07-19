

# def cat_hat():
#     '''
#     Input : can provide any string, in which it will find the substring "cat and "hat"
#             If both are equal number of time then it will return "Ture" else "False"
#
#           Using inbuild substing function to find the work
#           Syntex : string[start:end] 
#     '''
#     string = input("enter string without space : ")
#     if string.count("cat") == string.count("hat"):
#         print("True")
#         return True
#     else:
#         print("False")
#         return False

def cat_hat():
    '''
        Approch 2 using loop
        Syntex : string[start:end] 
    '''
    string = input("enter string without space : ").lower()
    cat_count = 0
    hat_count = 0
    
    for i in range(len(string) - 2):
        substring = string[i:i+3]
        if substring == "cat":
            cat_count += 1
        elif substring == "hat":
            hat_count += 1
            
    if cat_count == hat_count:
        print("True")
    else:
        print("false")
            
            
if __name__ == "__main__":
    cat_hat()
