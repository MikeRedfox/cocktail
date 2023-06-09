const getCocktail = async () => {
    const URL = 'http://127.0.0.1:5000/random'
    const response = await fetch(URL);
    const r = await response.json();
    return r;
}

const getImage = async (id) => {
    const URL = `https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i=${id}`
    const response = await fetch(URL);
    const r = await response.json();
    let i = r['drinks'][0]['strDrinkThumb']
    return i;
    
    
}

const randomCocktail = async () => {
    const j = await getCocktail();
    let info = (j['py/state']['__dict__']);
    let name = info['name'];
    let al = info['alcoholic'];
    let glass = info['glass'];
    let instructions = info['instructions'];
    let ing = info['ingredients'];
    let id = info['id']
    

    
    let txt = "";
    for (let x in ing) {
    txt += x + " " + ing[x] + "<br>";
    };

    document.querySelector('#nome').innerHTML = name;
    document.querySelector('#ins').innerHTML = instructions;
    document.querySelector('#ing').innerHTML = txt;
    document.querySelector('#alc_glass').innerHTML = `${al} 🍸: ${glass}`;
    
    const image = await getImage(id);
    const img = document.querySelector('img');
    img.src = image;
};

