from typing import List, Dict, Optional
import httpx
from sqlmodel import SQLModel, Session, create_engine, Field, JSON, Column
import os

        
class Cocktail(SQLModel, table=True):
    # __tablename__ = 'Cocktails'
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    alcoholic: str
    glass: str
    instructions: str
    ingredients: Dict = Field(default={}, sa_column=Column(JSON))

    # @classmethod
    # def from_json(cls,d: Dict):
    #     d = d['drinks'][0]
    #     ing = {d[f'strIngredient{i}']:d[f'strMeasure{i}'] for i in range(1,16) if d[f'strMeasure{i}'] != None}
    #     return cls(id=int(d['idDrink']), name=d['strDrink'], alcoholic=d['strAlcoholic'], 
    #     glass=d['strGlass'], instructions=d['strInstructionsIT'], 
    #     ingredients=ing)
    # def __init__(self,id,name,alc,glass,inst,ings):
    #     self.id = id
    #     self.name = name
    #     self.alcoholic = alc
    #     self.glass = glass
    #     self.instructions = inst
    #     self.ingredients = ings




def create_cock(r):
    d = r['drinks'][0]
    ing = {d[f'strIngredient{i}']:d[f'strMeasure{i}'] for i in range(1,16) if d[f'strMeasure{i}'] != None}
    c = Cocktail(id=int(d['idDrink']), name=d['strDrink'], alcoholic=d['strAlcoholic'], glass=d['strGlass'], instructions=d['strInstructionsIT'], ingredients=ing)
    session = Session(engine)
    # print(c)

    session.add(c)
    session.commit()
    # os.system('dunstify "Aggiunto a database"')

if __name__ == '__main__':


    engine = create_engine("sqlite:///database.db")
    SQLModel.metadata.create_all(engine)



    URL = 'https://www.thecocktaildb.com/api/json/v1/1/random.php'



    r = httpx.get(URL).json()
    c = create_cock(r)





# def get_info(url,df):
#     with httpx.Client() as client:
#        r = [ client.get(url).json() for i in range(100)]
#        for i in r:
#         c = Cocktail.from_json(i)
#         if c.id not in df.id:
#             cock = pd.DataFrame(c.__dict__,index=[int(c.id)])
#             df = pd.concat([df,cock])
#         else:
#             continue
#     return df
            


# if __name__ == '__main__':
#     URL = 'https://www.thecocktaildb.com/api/json/v1/1/random.php'
#     db_name = 'cocktails.pickle'
#     try:
#         df = pd.read_pickle(db_name)
#     except FileNotFoundError:
#         df = pd.DataFrame({})
#     info = get_info(URL,df)
#     info.to_pickle(db_name)
#     print(info)
