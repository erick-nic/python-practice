import json

def json_parser():
    with open("data.json", "r") as file:
        data = json.load(file)
        data['name'] = input("Insert name: ")
        data['ocupation'] = input("Insert ocupations: ")
        
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)
        print(data)

if __name__ == "__main__":
    json_parser()
