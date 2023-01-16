import pandas as pd
data = pd.read_csv("names.csv")
dataframe = pd.DataFrame(data)

def gender_checker(name):
    gender = "unknown"
    checks = dataframe[dataframe["name"]== name]
    try:
        check = checks.iloc[0,1]

        if check == "F":
            gender = "female"
        elif check == "M":
            gender = "male"
    except:
        if name[-1] in ["a","e","i","o"]:
            gender = "female"
        else:
            gender = "male"
    return gender  

def update_file(gender):
    print(gender)
    rule = """**************************************************** \ny >>> yes \nn >>> no\n****************************************************"""
    sorry = """ sorry try again file has been updated"""
    user1 = ""
    user2 = ""
    if gender == "male":
        print(rule)
        user1 =input(f"""{gender},"is it right sir """)
    elif gender == "female":
        print(rule)
        user2 = input(f"""{gender},"is it right mam """)
    if user1 == "y":
        print("thank you")
    elif user1 == "n":
        print(sorry)
        data = pd.read_csv("names.csv")
        dataframe = pd.DataFrame(data)
        update = pd.dataframe({"name":[name],"gender":["M"]})
        pd.concat([dataframe,update]).to_csv("names.csv",index=False)
        print("file has been updated")
    elif user2 == "y":
        print("thank you")
    elif user2 == "n":
        print(sorry)
        data = pd.read_csv("names.csv")
        dataframe = pd.DataFrame(data)
        update = pd.dataframe({"name":[name],"gender":["F"]})
        pd.concat([dataframe,update]).to_csv("names.csv",index=False)
        print("file has been updated")
runagain ="y"
while runagain == "y":
    name =  input("Enter your name: ").capitalize()
    try:
        checkint = int(name)
        print("please enter a valid name (⌐■_■)")
    except:
        gender = gender_checker(name)
        update = update_file(gender)
    finally:
        print("****************************************************")
        runagain = input("do you want to run again y/n: ")
       