cart = ["apple", "milk", "bread", "apple", "eggs", "milk"]
unique_items = list(set(cart))
unique_items.append("cheese")
unique_items.remove("bread")
print("Unique items in the cart:", unique_items)
unique_items.sort()
print("Cart sorted alphabetically:", unique_items)
print("final number of different items in cart", len(unique_items))
