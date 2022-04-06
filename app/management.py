from spartan import Spartans
import json
import pymongo

while True: #this stops the servers from overloading
    try: #connect to the mongo server
        client = MongoClient("mongodb://db.mrasuli.devops106:27017")
        break #if not available break
    except Exception as e:
        print("trying to create a connection to the datatbase")
        time.sleep(2)

# client = MongoClient(database_url)
db = client.spartan_m
# adding spartans to this dict by giving the id as the key
all_spartans_dict = {}

def get_all_spartans():
    list = {}
    with open("data/spartan_data.json", "r") as json_file:
        list = json.load(json_file)
    return list


def create(create_spartan):
    create_spartan = Spartans(create_spartan["spartan_id"], create_spartan["first_name"], create_spartan["last_name"],
                              create_spartan["birth_year"], create_spartan["birth_month"], create_spartan["birth_day"],
                              create_spartan["sp_course"], create_spartan["sp_stream"])

    if len(create_spartan.get_first_name()) < 2:
        return "Error: first name needs to have at least 2 characters"
    if len(create_spartan.get_last_name()) < 2:
        return "Error: last name needs to have at least 2 characters"
    if len(create_spartan.get_sp_course()) < 2:
        return "Error: spartan course needs to have at least 2 characters"
    if len(create_spartan.get_sp_stream()) < 2:
        return "Error: spartan stream needs to have at least 2 characters"

    # if int(create_spartan.get_birth_month() not in range (1, 32):
    #     return "ERROR: Day of birth should be a number between 1 and 31."

    # if int(create_spartan["birth_month"]) not in range(1, 12):
    #     return "ERROR: Month of birth should be a number between 1 and 12."
    # if int(create_spartan["birth_year"]) not in range(1900, 2005):
    #     return "ERROR: Year of birth should be a number between 1900 and 2005."

    load_jsonfile()
    all_spartans_dict[create_spartan.get_spartan_id()] = create_spartan
    save_to_jsonfile()
    return "Spartan has been saved"


def get_spartan(spartan_id):
    load_jsonfile()
    spartan = all_spartans_dict[int(spartan_id)]
    return spartan


def remove_spartan(spartan_id):
    load_jsonfile()
    del all_spartans_dict[int(spartan_id)]
    save_to_jsonfile()


def save_to_jsonfile():
    global all_spartans_dict
    temp_spartans = {}
    # The vars() function returns the __dic__ attribute of an object
    for spartan_id in all_spartans_dict:
        spartan = all_spartans_dict[spartan_id]
        spartan_dict = vars(spartan)
        temp_spartans[spartan_id] = spartan_dict
    # the file we want to write to
    # the vars allows for the file not be read as an object but instead its serialised
    with open("data/spartan_data.json", "w") as json_file:
        json.dump(temp_spartans, json_file)

    print("Data is stored in data.json")

def load_jsonfile():
    global all_spartans_dict

    temp_dict = {}
    all_spartans_dict = {}
    with open("data/spartan_data.json", "r") as json_file:
        temp_dict = json.load(json_file)

    for key_id in temp_dict:
        spartan = temp_dict[key_id]

        temp_spartan = Spartans(spartan["spartan_id"], spartan["first_name"],
                                spartan["last_name"], spartan["birth_year"],
                                spartan["birth_month"], spartan["birth_day"],
                                spartan["sp_course"], spartan["sp_stream"])

        all_spartans_dict[temp_spartan.get_spartan_id()] = temp_spartan
