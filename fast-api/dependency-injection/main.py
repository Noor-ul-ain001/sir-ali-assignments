from fastapi import FastAPI, Depends

app = FastAPI()

# Recipe models
class BiryaniRecipe:
    def get_recipe(self):
        return "Biryani Recipe: Rice, chicken, yogurt, spices, and saffron."

class PastaRecipe:
    def get_recipe(self):
        return "Pasta Recipe: Pasta, tomato sauce, garlic, olive oil, and cheese."

# Chef services
class BiryaniChef:
    def __init__(self, recipe: BiryaniRecipe):
        self.recipe = recipe

    def cook(self):
        return self.recipe.get_recipe()

class PastaChef:
    def __init__(self, recipe: PastaRecipe):
        self.recipe = recipe

    def cook(self):
        return self.recipe.get_recipe()

# Dependency providers
def get_biryani_recipe():
    return BiryaniRecipe()

def get_pasta_recipe():
    return PastaRecipe()

# API routes
@app.get("/biryani")
def biryani(recipe: BiryaniRecipe = Depends(get_biryani_recipe)):
    chef = BiryaniChef(recipe)
    return {"dish": chef.cook()}

@app.get("/pasta")
def pasta(recipe: PastaRecipe = Depends(get_pasta_recipe)):
    chef = PastaChef(recipe)
    return {"dish": chef.cook()}
