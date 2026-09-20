from django.core.management.base import BaseCommand
from menu.models import Category, FoodItem


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        categories = [
            ("Burgers", "Juicy burgers made fresh"),
            ("Pizza", "Hot and cheesy pizzas"),
            ("Indian", "Authentic Indian favourites"),
            ("Chinese", "Delicious Asian flavours"),
            ("Drinks", "Refreshing beverages"),
            ("Desserts", "Sweet treats for everyone"),
        ]

        category_objects = {}

        for name, description in categories:
            category, created = Category.objects.get_or_create(
                name=name,
                defaults={"description": description}
            )
            category_objects[name] = category

        foods = [
            ("Classic Cheese Burger", "Burgers",
             "Juicy burger with cheese and fresh vegetables.", 149,
             "burger.jpg", True),

            ("Spicy Chicken Burger", "Burgers",
             "Spicy chicken burger with fresh vegetables.", 179,
             "chicken-burger.jpg", True),

            ("Margherita Pizza", "Pizza",
             "Classic pizza with tomato, cheese and basil.", 249,
             "pizza.jpg", True),

            ("Farmhouse Pizza", "Pizza",
             "Pizza loaded with fresh vegetables and cheese.", 299,
             "farmhouse-pizza.jpg", False),

            ("Chicken Biryani", "Indian",
             "Aromatic basmati rice with delicious chicken.", 229,
             "biryani.jpg", True),

            ("Masala Dosa", "Indian",
             "Crispy dosa served with potato masala.", 119,
             "dosa.jpg", False),

            ("Hakka Noodles", "Chinese",
             "Stir-fried noodles with fresh vegetables.", 159,
             "noodles.jpg", False),

            ("Veg Manchurian", "Chinese",
             "Crispy vegetable balls in spicy sauce.", 169,
             "manchurian.jpg", False),

            ("Cold Coffee", "Drinks",
             "Creamy chilled coffee served cold.", 99,
             "cold-coffee.jpg", True),

            ("Fresh Lime Soda", "Drinks",
             "Refreshing lime drink with a fizzy twist.", 69,
             "lime-soda.jpg", False),

            ("Chocolate Brownie", "Desserts",
             "Warm chocolate brownie with rich chocolate flavour.", 129,
             "brownie.jpg", True),

            ("Chocolate Cake", "Desserts",
             "Soft and delicious chocolate cake.", 149,
             "cake.jpg", False),
        ]

        for name, category, description, price, image, featured in foods:

            FoodItem.objects.update_or_create(
                name=name,
                defaults={
                    "category": category_objects[category],
                    "description": description,
                    "price": price,
                    "image": image,
                    "is_available": True,
                    "is_featured": featured,
                }
            )

        self.stdout.write(
            self.style.SUCCESS(
                "Food Court data added successfully!"
            )
        )