# Question 3: Shopping Cart Management

def manage_cart(cart, add_product, remove_product):
    cart.append(add_product)
    print("Added product:", add_product)

    if remove_product in cart:
        cart.remove(remove_product)
        print("Removed product:", remove_product)
    else:
        print("Product not found:", remove_product)

    print("Final cart:", cart)
    print("Total number of products:", len(cart))

manage_cart(["Mouse", "Keyboard", "Headphones"], "Webcam", "Keyboard")
