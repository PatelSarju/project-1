product_name=input("Enter the Product name:")
product_price=int(input("Enter the Product price:"))

GST_PERCENTAGE=18

gst_value=(product_price*GST_PERCENTAGE)/100
total_price=product_price+gst_value

print(f"Your purchased product {product_name}'s final price with gst is {total_price}!")