from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from secret_key import openapi_key

import os
os.environ['OPENAI_API_KEY'] = openapi_key

llm = OpenAI(temperature=0.5)

def generate_restaurant_name_and_items(cuisine):
    # Chain 1: Restaurant Name
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    # Chain 2: Menu Items
    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="""Suggest 10 menu items for {restaurant_name}. Return it as a comma separated string"""
    )

    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', "menu_items"]
    )

    response = chain({'cuisine': cuisine})

    return response
def generate_recipe(menu_item):
    # Chain 3: Generate Recipe
    prompt_template_recipe = PromptTemplate(
        input_variables=['menu_item'],
        template="Generate the recipe for {menu_item}."
    )

    recipe_chain = LLMChain(llm=llm, prompt=prompt_template_recipe, output_key="recipe")

    chain = SequentialChain(
        chains=[recipe_chain],
        input_variables=['menu_item'],
        output_variables=['recipe']
    )

    recipe_generated = chain({'menu_item': menu_item})

    return recipe_generated['recipe']
