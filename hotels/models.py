from django.db import models

locations = [
    ("Ariana", "Ariana"),
    ("Beja", "Beja"),
    ("Ben Arous", "Ben Arous"),
    ("Bizerte", "Bizerte"),
    ("Gabes", "Gabes"),
    ("Gafsa", "Gafsa"),
    ("Jendouba", "Jendouba"),
    ("Kairouan", "Kairouan"),
    ("Kasserine", "Kasserine"),
    ("Kebili", "Kebili"),
    ("Kef", "Kef"),
    ("Mahdia", "Mahdia"),
    ("Manouba", "Manouba"),
    ("Medenine", "Medenine"),
    ("Monastir", "Monastir"),
    ("Nabeul", "Nabeul"),
    ("Sfax", "Sfax"),
    ("Sidi Bouzid", "Sidi Bouzid"),
    ("Siliana", "Siliana"),
    ("Sousse", "Sousse"),
    ("Tataouine", "Tataouine"),
    ("Tozeur", "Tozeur"),
    ("Tunis", "Tunis"),
    ("Zaghouan", "Zaghouan")
]
room_types = [
    ("Single Room", "Single Room"),
    ("Double Room", "Double Room"),
    ("Suite", "Suite"),
    ("Family Room", "Family Room")
]

class Hotel(models.Model):
    name = models.CharField(max_length=500)
    location = models.CharField(max_length=800, choices=locations)
    email = models.EmailField(max_length=600)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name
class Room(models.Model):
    Hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    type = models.CharField(max_length=500, choices=room_types)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.room_type} - {self.hotel.name}"
class Season(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    def __str__(self):
        return self.name
class Price(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.room.room_type} - {self.season.name} - {self.price}"
