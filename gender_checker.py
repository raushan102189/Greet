import pandas as pd

# read the csv file and store it in a dataframe
data = pd.read_csv("names.csv")
dataframe = pd.DataFrame(data)

# define a function to check the gender of a name
def gender_checker(name):
    gender = "unknown"
    # check the dataframe for the name
    checks = dataframe[dataframe["name"]== name]
    try:
        # get the gender from the dataframe
        check = checks.iloc[0,1]

        if check == "F":
            gender = "female"
        elif check == "M":
            gender = "male"
    except:
        # if the name is not found, use a rule-based approach to determine gender
        if name[-1] in ["a","e","i","o"]:
            gender = "female"
        else:
            gender = "male"
    return gender  

# define a function to update the csv file with the correct gender
def update_file(gender, name):
    # print the detected gender
    print(gender)
    # prompt the user to confirm or correct the gender
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
        update = update_file(gender, name)
    finally:
        print("****************************************************")
        runagain = input("do you want to run again y/n: ")
