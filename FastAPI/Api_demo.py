from fastapi import FastAPI

# Main application 
app = FastAPI()

# Creating Dataset
houses = {
    
    1: {
        "Number":"58",
        "Sector":"B",
        "Name":"Zulifqar Abid",
        "Size":"14 Marla"
        },
    2: {
        
        "Number":"11",
        "Sector":"A",
        "Name":"Fahad Chattha",
        "Size":"5 Marla"
        },
    3: {
        "Number":"55",
        "Sector":"C",
        "Name":"Adil Chohan",
        "Size":"7 Marla"
        },
    4: {
        
        "Number":"03",
        "Sector":"B",
        "Name":"Burhan Khana",
        "Size":"22 Marla"
        },
    5: {
        
        "Number":"17",
        "Sector":"H",
        "Name":"Rashid Khan",
        "Size":"1 Canal"
        },
    
}

@app.get("/")
def home():
    return{"name":"Dum Dum"}

# To fetch entered single entity from the dataset
@app.get("/get_house/{house_id}")
def get_house(house_id:int):
    return houses[house_id]