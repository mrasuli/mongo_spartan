from flask import Flask, request

from pymongo import MongoClient
#because we are going to migerate to the cloud, we need provide the full url for our db server
#so we have to make our ip address dynamic as it will change everytime
#we keep the ip address as a variable so its called on everytime needed inside the "database.config"
#the db.config will have the database url, you can pass it as a file to the docker container

# with open("database.config") as config_file:
#     database_url = config_file.read().strip()


#do this as best practice when tryig to connect to a resources > this will make the app work with the dns
while True: #this stops the servers from overloading
    try: #connect to the mongo server
        client = MongoClient("mongodb://db.mrasuli.devops106:27017")
        break #if not available break
    except Exception as e:
        print("trying to create a connection to the datatbase")
        time.sleep(2) #if not available, sleep for 2 secs and try again untill connected


db = client.spartan_m


flask_app = Flask(__name__) #this is telling py that i want to create a new server
@flask_app.route('/')
def home_page():
    return "This is the home page for flask and MongoDB..."


@flask_app.route('/add', methods=['POST']) #allows the user to add the spartan data by passing a json file
def add_spartan ():
    spartan = request.get_json()
    record = db.clients_data.insert_one(spartan)
    print(record)
    return f"the spartan that will be added is {spartan}"


@flask_app.route('/<spartan_id>', methods=["GET"])
def get_spartan(spartan_id):
    spartan_id = int(spartan_id)

    found_spartan = {}
    for item in db.clients_data.find({ "spartan_id": spartan_id }):
        print(item)
        found_spartan = item

    return f"{found_spartan}"


@flask_app.route('/spartans/<spartan_id>', methods=['DELETE'])
def delete_spartan(spartan_id):
    db.clients_data.delete_spartan(spartan_id)
    return f"You are removing a Spartan ID: {spartan_id}"


@flask_app.route('/spartans/list', methods=['GET'])
def spartan_list():
    db.clients_data.get_all_spartans()
    return f"You are looking for the list of spartans {all_spartans}"


if __name__ =="__main__":
    flask_app.run(debug=True, port = 8080, host= '0.0.0.0')
