def show_ingredients(*ingredients):
    print("Those are the ingredients you want on your sandwich:")
    for ing in ingredients:
        print(ing)
show_ingredients('chicken')
show_ingredients('tuna','mayo')
show_ingredients('ham','tomato','lettuce')
