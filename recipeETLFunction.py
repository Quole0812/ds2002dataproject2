import pandas as pd

recipes_df = pd.read_csv('kaggleRecipes.csv', encoding='latin1')

# test print so that i read the dataset into a df correctly - nice
print("Recipes:")
print(recipes_df.head())

# is there any issue of missing values? - not really we should be fine to continue
print("Missing Values in Recipes:")
print(recipes_df.isnull().sum())

# renaming columns for better clarity - looks nicer now
recipes_df.rename(columns={'recipe_name': 'Recipe', 'cuisine': 'Cuisine', 'ingredients': 'Ingredients', 'cooking_time_minutes': 'Cooking Time (minutes)', 'prep_time_minutes': 'Prep Time (minutes)', 'servings':'Servings','calories_per_serving':'Calories (per serving)', 'dietary_restrictions': 'Dietary Restrictions'}, inplace=True)
print("Updated Recipe Columns:")
print(recipes_df.columns)

# make a total time column based on prep + cook time - im gonna make like a "predicted difficulty" column based on num of ingredients and this total time taken to make the dish
recipes_df['Total Cook Time (minutes)'] = recipes_df['Prep Time (minutes)'] + recipes_df['Cooking Time (minutes)']

# make a num of ingredients column - lambda function; counts every ingredient after splitting on x
recipes_df['Number of Ingredients'] = recipes_df['Ingredients'].apply(
            lambda x: len(x.split(',')) if isinstance(x, str) else 0
        )

# helper function for assigning difficulty levels - lowkey these thresholds are semi-arbitrary but i feel like they make sense
def assign_difficulty(total_time, num_ingredients):
    if total_time >= 60 and num_ingredients >= 12:
        return 'Hard'
    elif total_time >= 30 and num_ingredients >= 5:
        return 'Medium'
    else:
        return 'Easy'

# difficulty column - lambda func (just runs the helper function on each row)
recipes_df['difficulty'] = recipes_df.apply(
            lambda row: assign_difficulty(row['Total Cook Time (minutes)'], row['Number of Ingredients']), axis=1
        )

# double check i can print everything
print(recipes_df.columns)
print(recipes_df.head())

# save to new csv file
recipes_df.to_csv('cleanedRecipes.csv', index=False)

