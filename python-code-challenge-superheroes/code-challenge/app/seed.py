from app import app
from models import Hero, Power, HeroPower,db

# Create and add sample data
def seed_database():
    # Sample Heroes
    hero1 = Hero(name="Kamala Khan", super_name="Ms. Marvel")
    hero2 = Hero(name="Doreen Green", super_name="Squirrel Girl")
    hero3 = Hero(name="Gwen Stacy", super_name="Spider-Gwen")

    # Sample Powers
    power1 = Power(name="super strength", description="gives the wielder super-human strengths")
    power2 = Power(name="flight", description="gives the wielder the ability to fly through the skies at supersonic speed")

    # Sample HeroPowers
    hero_power1 = HeroPower(strength="Average", hero=hero1, power=power1)
    hero_power2 = HeroPower(strength="Above Average", hero=hero1, power=power2)
    hero_power3 = HeroPower(strength="Strong", hero=hero2, power=power1)

    # Add data to the session
    db.session.add(hero1)
    db.session.add(hero2)
    db.session.add(hero3)
    db.session.add(power1)
    db.session.add(power2)
    db.session.add(hero_power1)
    db.session.add(hero_power2)
    db.session.add(hero_power3)

    # Commit the changes to the database
    db.session.commit()

if __name__ == '__main__':
    # Initialize the Flask app and database
   
    with app.app_context():
        db.create_all()
        seed_database()
