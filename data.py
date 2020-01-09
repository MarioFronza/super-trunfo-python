from app.models.card import Card

cars = [
    Card("Peteinossauro", 0.3, 0.6, 0.1, 210.0),
    Card("Oftamossauro", 1.3, 5.0, 3000.0, 165.0),
    Card("Alossauro", 5.2, 14.5, 3600.0, 151.0),
    Card("Globidens", 1.1, 6.0, 400.0, 150.0),
    Card("Barionix", 8.0, 12.0, 2000.0, 125.5),
    Card("Triceratopo", 6.0, 9.0, 6000.0, 64.0),
    Card("Ultrassauro", 22.0, 38.0, 9000.0, 154.0),
    Card("Tiranossauro (T)", 5.6, 14.0, 7000.0, 68.0),
    Card("Patagossauro", 8.7, 18.0, 16000.0, 169.0),
    Card("Brachiossauro", 15.0, 28.0, 5000.0, 156.0),
    Card("Pterodactilo", 0.1, 1.9, 1.1, 140.0),
    Card("Velociraptor", 1.0, 2.0, 80.0, 80.0),
    Card("Estegossauro", 4.0, 9.0, 4000.0, 159.0),
    Card("Dilofossauro", 2.5, 8.0, 450.0, 206.0),
    Card("Diplodoco", 5.0, 27.0, 2500.0, 157.0),
    Card("Melanorossauro", 12.0, 15.0, 8000.0, 220.0),
    Card("Compsognato", 0.9, 1.3, 2.5, 170.0),
    Card("Baptornis", 0.8, 1.0, 7.0, 83.0),
    Card("Psitacossauro", 0.7, 2.0, 25.0, 125.0),
    Card("Procompsognato", 0.4, 1.2, 1.0, 222.0),
]


def get_all_cards():
    return cars

