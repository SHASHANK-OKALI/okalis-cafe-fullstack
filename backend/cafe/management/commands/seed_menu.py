from django.core.management.base import BaseCommand
from cafe.models import MenuItem

MENU = [
 ("Cappuccino","Coffee","Rich espresso blended with silky steamed milk and a soft layer of foam.",160,4.9,"https://images.unsplash.com/photo-1572442388796-11668a67e53d?auto=format&fit=crop&w=700&q=85",True),
 ("Caramel Latte","Coffee","Smooth espresso, creamy steamed milk and a delicate caramel sweetness.",180,4.8,"https://images.unsplash.com/photo-1561882468-9110e03e0f78?auto=format&fit=crop&w=700&q=85",False),
 ("Cold Coffee","Beverages","A chilled, creamy coffee blend topped with a smooth layer of froth.",170,4.7,"https://images.unsplash.com/photo-1461023058943-07fcbe16d735?auto=format&fit=crop&w=700&q=85",False),
 ("Cafe Mocha","Coffee","Bold espresso meets rich chocolate and steamed milk for a decadent cup.",190,4.9,"https://images.unsplash.com/photo-1578314675249-a6910f80cc4e?auto=format&fit=crop&w=700&q=85",True),
 ("Classic Burger","Fast Food","Juicy vegetable patty layered with fresh greens, cheese and our signature sauce.",220,4.8,"https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=700&q=85",True),
 ("Loaded Sandwich","Fast Food","Freshly toasted bread filled with vegetables, cheese and creamy house dressing.",190,4.7,"https://images.unsplash.com/photo-1528735602780-2552fd46c7af?auto=format&fit=crop&w=700&q=85",False),
 ("Chocolate Cake","Desserts","Moist chocolate sponge layered with silky chocolate cream and ganache.",210,4.9,"https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=700&q=85",True),
 ("Blueberry Cheesecake","Desserts","Creamy cheesecake topped with a bright blueberry compote and fresh berries.",230,4.8,"https://images.unsplash.com/photo-1533134242443-d4fd215305ad?auto=format&fit=crop&w=700&q=85",False),
 ("French Fries","Fast Food","Golden crispy fries seasoned with our special cafe seasoning.",130,4.6,"https://images.unsplash.com/photo-1573080496219-bb080dd4f877?auto=format&fit=crop&w=700&q=85",False),
 ("Masala Chai","Beverages","Traditional Indian tea brewed with aromatic spices and creamy milk.",100,4.8,"https://images.unsplash.com/photo-1594631252845-29fc4cc8cde9?auto=format&fit=crop&w=700&q=85",False),
 ("Pasta Alfredo","Special Dishes","Creamy Alfredo pasta tossed with herbs, vegetables and parmesan.",260,4.9,"https://images.unsplash.com/photo-1645112411341-6c4fd023714a?auto=format&fit=crop&w=700&q=85",True),
 ("Brownie Sundae","Desserts","Warm chocolate brownie served with vanilla ice cream and chocolate drizzle.",220,4.9,"https://images.unsplash.com/photo-1564355808539-22fda35bed7e?auto=format&fit=crop&w=700&q=85",True),
]
class Command(BaseCommand):
    help = "Seed or refresh the starter OKALI'S CAFE menu. Existing items are updated by name."
    def handle(self, *args, **options):
        for name, category, description, price, rating, image, popular in MENU:
            MenuItem.objects.update_or_create(name=name, defaults={"category":category,"description":description,"price":price,"rating":rating,"image":image,"popular":popular,"is_available":True})
        self.stdout.write(self.style.SUCCESS(f"Seeded {len(MENU)} cafe menu items."))
