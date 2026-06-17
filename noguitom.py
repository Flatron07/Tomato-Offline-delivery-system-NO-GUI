import mysql.connector
import random

# =========================
# Database (MySQL) helpers
# =========================
def connect_db():
    """Make a connection to MySQL and return it."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="tomato_app",
        connection_timeout=3
    )

def register_user(username, password):
    """Create a new user account."""
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users(username, password) VALUES(%s, %s)",
            (username, password)
        )
        conn.commit()
        return True, "Registered successfully!"
    except mysql.connector.IntegrityError:
        return False, "Username already exists."
    except Exception as e:
        return False, f"Database Error: {e}"
    finally:
        try:
            cur.close()
            conn.close()
        except:
            pass

def check_login(username, password):
    """Return True if username and password are valid, else False."""
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute(
            "SELECT 1 FROM users WHERE username=%s AND password=%s",
            (username, password)
        )
        return bool(cur.fetchone())
    except Exception as e:
        print("Database Error:", e)
        return False
    finally:
        try:
            cur.close()
            conn.close()
        except:
            pass

# =========================
# Coupons
# =========================
COUPONS = {
    "FOOD10":   {"percent": 0.10, "flat": 0.0,  "cap": None},
    "SAVE50":   {"percent": 0.0,  "flat": 50.0, "cap": None},
    "DINNER30": {"percent": 0.30, "flat": 0.0,  "cap": 100.0},
}

def apply_coupon(subtotal, code):
    """Return (final_amount, discount_amount) after applying coupon code."""
    if not code:
        return subtotal, 0.0

    coupon = COUPONS.get(code.strip().upper())
    if not coupon:
        return subtotal, 0.0

    percent_discount = subtotal * coupon["percent"]
    if coupon["cap"] is not None:
        percent_discount = min(percent_discount, coupon["cap"])

    total_discount = min(percent_discount + coupon["flat"], subtotal)
    final_amount = subtotal - total_discount
    return final_amount, total_discount

# =========================
# Restaurants and Menus (unchanged)
# =========================
RESTAURANTS = [
    {"name": "Red Pepper Diner", "cuisine": "Indian",
     "menu": [{"name": "Butter Chicken", "price": 220},
              {"name": "Paneer Tikka", "price": 180},
              {"name": "Dal Makhani", "price": 160},
              {"name": "Garlic Naan", "price": 40},
              {"name": "Veg Biryani", "price": 190}]},
    {"name": "Sizzle Street", "cuisine": "Chinese",
     "menu": [{"name": "Noodles", "price": 150},
              {"name": "Spring Rolls", "price": 90},
              {"name": "Manchurian", "price": 170},
              {"name": "Fried Rice", "price": 140},
              {"name": "Chilli Paneer", "price": 190}]},
    {"name": "La Pizzeria", "cuisine": "Italian",
     "menu": [{"name": "Margherita Pizza", "price": 299},
              {"name": "Farmhouse Pizza", "price": 399},
              {"name": "Pesto Pasta", "price": 329},
              {"name": "Arrabbiata Pasta", "price": 299},
              {"name": "Garlic Bread", "price": 129}]},
    {"name": "Taco Loco", "cuisine": "Mexican",
     "menu": [{"name": "Veg Tacos", "price": 199},
              {"name": "Bean Burrito", "price": 219},
              {"name": "Quesadilla", "price": 239},
              {"name": "Nachos", "price": 149},
              {"name": "Churros", "price": 129}]},
    {"name": "Sushi Zen", "cuisine": "Japanese",
     "menu": [{"name": "Veg Sushi Roll", "price": 249},
              {"name": "Miso Soup", "price": 129},
              {"name": "Tempura Veg", "price": 269},
              {"name": "Ramen", "price": 289},
              {"name": "Edamame", "price": 149}]},
    {"name": "Burger Barn", "cuisine": "American",
     "menu": [{"name": "Classic Veg Burger", "price": 159},
              {"name": "Cheese Burger", "price": 179},
              {"name": "Fries", "price": 89},
              {"name": "Onion Rings", "price": 99},
              {"name": "Milkshake", "price": 149}]},
    {"name": "Spice Route", "cuisine": "Thai",
     "menu": [{"name": "Green Curry", "price": 259},
              {"name": "Red Curry", "price": 259},
              {"name": "Pad Thai", "price": 239},
              {"name": "Tom Yum Soup", "price": 169},
              {"name": "Sticky Rice", "price": 119}]},
    {"name": "Kebab House", "cuisine": "Middle Eastern",
     "menu": [{"name": "Falafel Wrap", "price": 169},
              {"name": "Hummus & Pita", "price": 139},
              {"name": "Paneer Kebab", "price": 219},
              {"name": "Shawarma", "price": 209},
              {"name": "Baklava", "price": 149}]},
    {"name": "Curry Leaf", "cuisine": "South Indian",
     "menu": [{"name": "Masala Dosa", "price": 129},
              {"name": "Idli Sambar", "price": 99},
              {"name": "Medu Vada", "price": 99},
              {"name": "Pongal", "price": 109},
              {"name": "Filter Coffee", "price": 69}]},
    {"name": "Bengal Bite", "cuisine": "Bengali",
     "menu": [{"name": "Veg Chop", "price": 79},
              {"name": "Luchi & Cholar Dal", "price": 129},
              {"name": "Aloo Posto", "price": 149},
              {"name": "Misti Doi", "price": 89},
              {"name": "Roshogolla", "price": 99}]},
]

# =========================
# Ratings (random for demo)
# =========================
ratings_cache = {}  # Keeps same ratings during one program run

def get_ratings(restaurant_index):
    """Return a dict like {1: votes, 2: votes, ..., 5: votes}."""
    if restaurant_index not in ratings_cache:
        # Create 5 random vote counts for 1 to 5 stars
        votes = [random.randint(1, 9) for _ in range(5)]
        ratings_cache[restaurant_index] = {stars: votes[stars - 1] for stars in range(1, 6)}
    return ratings_cache[restaurant_index]

# =========================
# Helper display functions
# =========================
def print_main_menu(username):
    print("\n========================")
    print(f"Welcome, {username}!")
    print("1. View Restaurants")
    print("2. View Cart")
    print("3. Checkout")
    print("4. Logout")
    print("========================")

def print_restaurants():
    for i, r in enumerate(RESTAURANTS, start=1):
        print(f"{i}. {r['name']} ({r['cuisine']})")

def show_cart_total(cart):
    """Print cart items and return subtotal."""
    subtotal = 0
    print("\n--- YOUR CART ---")
    for item in cart:
        print(f"{item['name']} - ₹{item['price']} x {item['qty']}")
        subtotal += item["price"] * item["qty"]
    print(f"Total: ₹{subtotal}")
    return subtotal

# =========================
# Main App (after login)
# =========================
def run_app(username):
    cart = []

    while True:
        print_main_menu(username)
        user_choice = input("Choose option: ").strip()

        if user_choice == "1":
            # Show restaurants and pick one
            print_restaurants()
            try:
                idx = int(input("Select restaurant number: ")) - 1
            except:
                print("Please enter a number.")
                continue

            if idx < 0 or idx >= len(RESTAURANTS):
                print("Invalid restaurant number.")
                continue

            restaurant = RESTAURANTS[idx]
            print(f"\n--- Menu: {restaurant['name']} ---")
            for i, menu_item in enumerate(restaurant["menu"], start=1):
                print(f"{i}. {menu_item['name']} - ₹{menu_item['price']}")
            print("6. View Ratings")
            print("0. Back")

            option = input("Choose: ").strip()

            if option == "6":
                rt = get_ratings(idx)
                print("\nRatings (1-5 stars):")
                for stars, votes in rt.items():
                    print(f"{stars}⭐ : {votes} votes")
                continue

            if option == "0":
                continue

            # Add selected item to cart
            try:
                item = restaurant["menu"][int(option) - 1]
            except:
                print("Invalid option.")
                continue

            # If already in cart, increase quantity
            for c in cart:
                if c["name"] == item["name"]:
                    c["qty"] += 1
                    break
            else:
                cart.append({"name": item["name"], "price": item["price"], "qty": 1})

            print("Added to cart!")

        elif user_choice == "2":
            if not cart:
                print("Cart empty.")
                continue

            show_cart_total(cart)
            print("1. Remove item")
            print("0. Back")
            action = input("Choose: ").strip()

            if action == "1":
                name = input("Enter item name to remove: ").strip()
                cart = [c for c in cart if c["name"] != name]

        elif user_choice == "3":
            if not cart:
                print("Cart empty.")
                continue

            subtotal = sum(c["price"] * c["qty"] for c in cart)
            print("\n--- CHECKOUT ---")
            print(f"Subtotal = ₹{subtotal}")

            coupon = input("Enter coupon code (optional): ").strip()
            final_amount, discount = apply_coupon(subtotal, coupon)
            print(f"Discount: ₹{discount:.2f}")
            print(f"Final Amount: ₹{final_amount:.2f}")

            address = input("Enter delivery address: ")
            eta_minutes = random.randint(10, 45)

            print("\nOrder Placed!")
            print(f"ETA: {eta_minutes} minutes\n")
            cart.clear()

        elif user_choice == "4":
            print("Logged out.\n")
            break

        else:
            print("Invalid option. Please choose 1-4.")

# =========================
# Login / Register Menu
# =========================
def main():
    while True:
        print("\n==== Tomato App ====")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            username = input("Username: ").strip()
            password = input("Password: ").strip()
            if check_login(username, password):
                print("Login successful!")
                run_app(username)
            else:
                print("Invalid login.")

        elif choice == "2":
            username = input("New username: ").strip()
            password = input("New password: ").strip()
            ok, msg = register_user(username, password)
            print(msg)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please choose 1-3.")

if __name__ == "__main__":
    main()
