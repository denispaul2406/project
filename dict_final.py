import json
from difflib import get_close_matches
def main():

    def search_word(w):
        if w in data:
            return data[w]
        # for getting close matches of word
        elif len(get_close_matches(w, data.keys())) > 0:
            yn = input("Did you mean % s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
            yn = yn.lower()
            if yn == "y":
                return data[get_close_matches(w, data.keys())[0]]
            elif yn == "n":
                return "The word doesn't exist. Please double check it."
            else:
                return "We didn't understand your entry."   
        else:
            return "The word doesn't exist. Please double check it."


    def loop():
        global search
        search = input("Do You want to use dictionary again? y = yes, n = no \n")
        while search not in ["y", "n","Y","N"]:
            search = input("Do You want use dictionary again? y = yes, n = no \n")
        if search == "y":
            main()
        elif search == "n":
            print("\nThanks For Using The Dictionary ! We expect you back again!")
            exit()       
            
    print("\n\n\nWelcome to the Dictionary\n\n")
    code = input("Press:\n\n 1 for for Markup language\n\n 2 for Coding language \n")
    while True:
        if code=="1":     
            lang = input("Press:\n\n 1 for HTML\n\n 2 for CSS\n")
            if lang == "1" :
                select=input("Press:\n\n 1 for HTML Tag\n 2 for Definition of a Tag\n")
                if select=="1":
                    word=input("Enter your Requirement\n")
                    data = json.load(open("search.json"))
                    output = search_word(word)
                    if type(output) == list:
                        for item in output:
                            print(item)
                    else:
                        print(output)
                else:
                    word=input("Enter the Tag Name within Angular Braces (<>)\n")
                    data = json.load(open("html.json"))
                    output = search_word(word)
                    if type(output) == list:
                        for item in output:
                            print(item)
                    else:
                        print(output)
                break      
            elif lang == "2" :
                word=input("Enter the attribute name\n")
                data = json.load(open("css.json"))
                output = search_word(word)
                if type(output) == list:
                    for item in output:
                        print(item)
                else:
                    print(output)
                    break
        elif code=="2":
            lang = input("Press:\n\n 1 for PYTHON\n\n 2 for C\n")
            if lang == "1":
                word=input("Enter the keyword\n")
                data = json.load(open("python.json"))
                output = search_word(word)
                if type(output) == list:
                    for item in output:
                        print(item)
                else:
                    print(output)
                break
            elif lang == "2":
                word=input("Enter the keyword\n")
                data = json.load(open("c.json"))   
                output = search_word(word)
                if type(output) == list:
                    for item in output:
                        print(item)
                else:
                    print(output)
                    break
        else:
            print("Choose from given Options(Markup Language / Coding Language) only")
            break
    loop()

main()