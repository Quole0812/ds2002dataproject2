
<img width="298" alt="Screenshot 2025-05-09 at 12 43 50 AM" src="https://github.com/user-attachments/assets/a2d0628e-f0c4-4c3c-81bf-007a326e51c4" />

endpoint link: http://35.193.163.40:5000/chat

TUTORIAL: PLEASE WATCH
https://youtu.be/q1wtwunGXg8?si=Dr7vW3F1kKlntfqA 

download the repo, then do the following command

python main.py

#then it's going to give you a prompt, you can choose food recipe, drink recipe, or gemini

#choose one then follow the prompt


ALTERNATIVELY, you can do 

curl -X POST http://35.193.163.40:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"token": "food recipe"}'                                       

after the bot is prompted the specific token, you then do 

curl -X POST http://35.193.163.40:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"token": "food recipe", "question": "Spicy Kimchi Fried Rice"}'

Same thing for the drink 

Drink recipe covered: 
https://www.thecocktaildb.com/ 

### Recipes Covered

Here's the dataset https://www.kaggle.com/datasets/prajwaldongre/collection-of-recipes-around-the-world 

- Spicy Kimchi Fried Rice
- Classic Margherita Pizza
- Coconut Chickpea Curry
- Pad See Ew with Tofu
- Beef Bourguignon
- Chicken Enchiladas with Green Sauce
- Greek Lemon Herb Chicken and Potatoes
- Swedish Meatballs with Cream Sauce
- Injera with Misir Wot
- Jollof Rice with Chicken
- Peruvian Lomo Saltado
- Argentinian Empanadas with Beef
- Australian Lamb Chops with Rosemary and Garlic
- Hawaiian Poi with Kalua Pig
- Japanese Chicken Teriyaki with Steamed Broccoli
- Vietnamese Pho Bo (Beef Noodle Soup)
- Spanish Paella with Seafood
- Moroccan Tagine with Lamb and Apricots
- Brazilian Feijoada (Black Bean Stew)
- American Clam Chowder (New England Style)
- Jamaican Jerk Chicken with Rice and Peas
- Lebanese Fattoush Salad
- Irish Shepherd's Pie
- Argentine Chimichurri Steak with Roasted Vegetables
- Thai Green Curry with Shrimp
- Korean Bibimbap (Mixed Rice with Meat and Vegetables)
- Italian Risotto with Saffron and Parmesan
- Mexican Fish Tacos with Cabbage Slaw
- French Onion Soup with Gruyere Croutons
- Greek Spanakopita (Spinach and Feta Pie)
- Swedish Gravlax with Dill Sauce
- Ethiopian Doro Wat (Chicken Stew) with Hard-Boiled Eggs
- Nigerian Egusi Soup with Pounded Yam
- Peruvian Ceviche with Sweet Potato and Corn
- Argentinian Asado (Grilled Meats)
- Australian Barbecue Prawns with Garlic Butter
- Hawaiian Laulau (Pork Wrapped in Taro Leaves)
- Japanese Ramen with Pork Belly and Soft Egg
- Vietnamese Goi Cuon (Fresh Spring Rolls) with Peanut Sauce
- Spanish Gazpacho (Cold Tomato Soup)
- Moroccan Chicken Tagine with Olives and Preserved Lemons
- Brazilian Moqueca (Seafood Stew with Coconut Milk)
- American Jambalaya with Chicken and Sausage
- Jamaican Ackee and Saltfish
- Lebanese Kibbeh (Baked Meat and Burghul Dish)
- Irish Colcannon (Mashed Potatoes with Kale or Cabbage)
- Argentine Milanesa with Mashed Potatoes
- Thai Massaman Curry with Chicken and Potatoes
- Korean Bulgogi (Marinated Grilled Beef)
- Mexican Pozole Rojo with Pork and Hominy
- French Ratatouille (Vegetable Stew)
- Greek Moussaka (Eggplant and Meat Casserole)
- Swedish Kanelbullar (Cinnamon Buns)
- Ethiopian Injera with Shiro Wot
- Nigerian Suya (Grilled Spicy Skewered Meat)
- Peruvian Aji de Gallina (Spicy Chicken Stew)
- Argentinian Locro (Hearty Stew with Corn and Beans)
- Australian Lamingtons (Sponge Cake with Chocolate and Coconut)
- Hawaiian Poke Bowl with Tuna and Avocado
- Japanese Okonomiyaki (Savory Pancake)
- Vietnamese Banh Mi (Sandwich)
- Spanish Tortilla Española (Spanish Omelette)
- Moroccan Harira Soup (Lentil and Tomato Soup)
- Brazilian Pão de Queijo (Cheese Bread)
- American Chili con Carne
- Jamaican Brown Stew Fish
- Lebanese Tabbouleh Salad
- Irish Boxty (Potato Pancakes)
- Argentine Carbonada Criolla (Beef and Vegetable Stew)
- Thai Panang Curry with Chicken
- Korean Japchae (Glass Noodles with Vegetables and Beef)
- Italian Carbonara (Pasta with Eggs, Cheese, Bacon)
- Mexican Tamales with Chicken and Salsa Verde
- French Crêpes Suzette (Pancakes with Orange Butter Sauce)
- Greek Pastitsio (Baked Pasta with Meat Sauce and Bechamel)
- Swedish Semlor (Cardamom Buns with Almond Paste and Cream)
- Ethiopian Tibs (Sautéed Meat with Vegetables)
- Nigerian Moi Moi (Steamed Bean Pudding)
- Peruvian Anticuchos de Corazón (Grilled Beef Heart Skewers)
- Argentinian Alfajores (Shortbread Cookies with Dulce de Leche)
- Australian Pavlova (Meringue Dessert with Fruit)
- Hawaiian Kalua Pig (Slow-Cooked Shredded Pork)
- Japanese Miso Soup with Tofu and Seaweed
- Vietnamese Bun Cha (Grilled Pork with Noodles and Herbs)
- Spanish Churros with Chocolate Sauce
- Moroccan Tanjia (Slow-Cooked Meat in a Clay Pot)
- Brazilian Brigadeiros (Chocolate Fudge Balls)
- American Gumbo with Chicken, Sausage, and Shrimp
- Jamaican Curry Goat with Rice and Peas
- Lebanese Manakeesh (Flatbread with Za'atar or Cheese)
- Irish Soda Bread
- Argentine Flan with Dulce de Leche
- Thai Tom Yum Soup with Shrimp
- Korean Tteokbokki (Spicy Rice Cakes)
- Italian Tiramisu (Coffee-Flavored Dessert)
- Mexican Chiles Rellenos (Stuffed Poblano Peppers)
- French Soupe à l'Oignon Gratinée (French Onion Soup with Cheese Croutons)
- Greek Baklava (Sweet Pastry with Nuts and Syrup)
- Swedish Fika (Coffee Break with Pastries)
- Ethiopian Kitfo (Minced Raw Beef with Spices and Butter)
- Nigerian Puff Puff (Deep-Fried Dough Balls)
- Peruvian Arroz con Pollo (Rice with Chicken)
- Argentinian Choripan (Chorizo Sandwich)
- Australian Tim Tam Slam (Chocolate Biscuits with Hot Drink)
- Hawaiian Haupia (Coconut Milk Pudding)
- Japanese Sushi Rolls (Various Types)
- Vietnamese Summer Rolls with Peanut Sauce
- Spanish Seafood Paella
- Moroccan Mint Tea
- Brazilian Coxinha (Chicken Croquettes)
- American Apple Pie
- Jamaican Bammy (Cassava Flatbread)
- Lebanese Hummus with Pita Bread
- Irish Stew with Lamb and Vegetables
- Argentine Dulce de Leche (Caramel Spread)
- Thai Red Curry with Beef
- Korean Kimchi Jjigae (Kimchi Stew)
- Italian Pesto Genovese with Trofie Pasta
- Mexican Chicken Fajitas with Bell Peppers and Onions
- French Quiche Lorraine (Bacon and Cheese Tart)
- Greek Dolmades (Stuffed Grape Leaves with Rice and Herbs)
- Swedish Pea Soup with Pork and Pancakes
- Ethiopian Gomen (Collard Greens with Spices)
- Nigerian Jollof Rice with Beef
- Peruvian Papa a la Huancaína (Potatoes with Cheese Sauce)
- Argentinian Provoleta (Grilled Provolone Cheese)
- Australian Meat Pies
- Hawaiian Chicken Long Rice
- Japanese Tempura (Deep-Fried Seafood and Vegetables)
- Vietnamese Banh Xeo (Crispy Savory Crepes)
- Spanish Gambas al Ajillo (Garlic Shrimp)
- French Shallots Sauté
- Peruvian SweetPotato Bowl
- Swedish Lingonberries Wrap
- Italian Mozzarella Rolls
- Australian Lamb Delight
- Japanese Tofu Feast
- Swedish Salmon Wrap
- Swedish Potatoes Delight
- Brazilian Beef Curry
- Australian Egg Stew
- Mexican ChiliPowder Medley
- Ethiopian SpicedButter Medley
- Nigerian Okra Stew
- Polynesian Breadfruit Medley
- Japanese Miso Medley
- Ethiopian SpicedButter Wrap
- Korean Scallions Wrap
- Spanish Rice Stew
- Argentinian Chimichurri Wrap
- Japanese Miso Wrap
- Peruvian AjiAmarillo Feast
- Swedish Lingonberries Medley
- Thai Galangal Medley
- Chinese Five-Spice Delight
- Nigerian PalmOil Curry
- Thai Lime Grill
- Korean Scallions Delight
- Nigerian Cassava Feast
- American Corn Curry
- Brazilian BlackBeans Curry
