def calculate_inventory_value(products):
    total_inventory_value = 0
    
    # El bucle 'for' recorre las filas, '.items()' te da los datos de adentro
    for product_name, details in products.items():
        product_total = details["price"] * details["amount"]
        
        print(f"the total price of the products: {product_name}: {product_total}")
        
        # 1. Sumamos el total de este producto a nuestra "alcancía" general
        total_inventory_value += product_total
        
    # 2. Devolvemos el valor total final (fuera del bucle)
    return total_inventory_value

# --- Para probar que funciona ---
inventory = {
    "Apples": {"price": 1500, "amount": 10},
    "Pears": {"price": 2000, "amount": 5},
    "Oranges": {"price": 1200, "amount": 8}
}

resultado = calculate_inventory_value(inventory)
print(f"\nEl valor total del inventario es: {resultado}")