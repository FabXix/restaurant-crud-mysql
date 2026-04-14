GET_COOK_FROM_DISH = """
  SELECT 
    c.cook_id,
    c.name AS cook_name,
    d.dish_id,
    d.name AS dish_name
  FROM Dish d 
  JOIN Cook c ON c.cook_id = d.cook_id
  WHERE d.name = %s
"""

GET_COOKS_WITH_DISHES = """
  SELECT 
    c.name AS cook_name,
    d.name AS dish_name
  FROM Cook c
  LEFT JOIN Dish d ON d.cook_id = c.cook_id
  ORDER BY c.name, d.name
"""

GET_INGREDIENTS_THAT_A_COOK_USE = """
  SELECT 
    c.name AS cook_name,
    d.name AS dish_name,
    COUNT(DISTINCT i.ingredient_id) AS num_ingredients
  FROM Cook c
  LEFT JOIN Dish d ON d.cook_id = c.cook_id
  LEFT JOIN Dish_Ingredient di ON di.dish_id = d.dish_id
  LEFT JOIN Ingredient i ON di.ingredient_id = i.ingredient_id
  GROUP BY cook_name, dish_name
  ORDER BY num_ingredients DESC
"""

GET_AMOUNT_OF_COOKS_THAT_USE_INGREDIENTS = """
  SELECT  
    i.ingredient_id,
    i.name AS ingredient_name,
    COUNT(DISTINCT c.cook_id) AS cooks
  FROM Ingredient i
  JOIN Dish_Ingredient di ON di.ingredient_id = i.ingredient_id
  JOIN Dish d ON di.dish_id = d.dish_id
  JOIN Cook c ON c.cook_id = d.cook_id
  GROUP BY i.ingredient_id, i.name
  HAVING COUNT(DISTINCT c.cook_id) > 1
  ORDER BY cooks DESC
"""

GET_A_COOK_DISH = """
  SELECT 
    c.name AS cook_name,
    d.name AS dish_name
  FROM Cook c
  LEFT JOIN Dish d ON d.cook_id = c.cook_id
  WHERE c.name = %s
"""
