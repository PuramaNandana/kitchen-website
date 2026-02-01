from backend.database import SessionLocal, engine
from backend import models

def seed_data():
    # Create tables if they don't exist
    models.Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    
    # Check if designs already exist
    if db.query(models.Design).count() == 0:
        designs = [
            models.Design(title="Modern Minimalist", image_url="assets/design1.png", description="Clean lines and functional design for the modern home."),
            models.Design(title="Rustic Charm", image_url="assets/design2.png", description="Warm wood tones and traditional elements for a cozy feel."),
            models.Design(title="Industrial Sleek", image_url="https://images.unsplash.com/photo-1556911261-6bd7411630c3?auto=format&fit=crop&w=800&q=80", description="Dark metals and bold textures for a contemporary look."),
            models.Design(title="Classic White", image_url="https://images.unsplash.com/photo-1484154218962-a197022b5858?auto=format&fit=crop&w=800&q=80", description="Timeless white cabinetry that brightens up any space."),
        ]
        db.add_all(designs)
        print("Seeded designs")

    # Check if services already exist
    if db.query(models.Service).count() == 0:
        services = [
            models.Service(title="Modular Kitchen", icon="kitchen", description="Custom modular solutions tailored to your space and style."),
            models.Service(title="Interior Design", icon="design_services", description="Complete interior renovation and design consultation."),
            models.Service(title="Custom Cabinets", icon="cabinet", description="High-quality handcrafted cabinets for maximum storage."),
        ]
        db.add_all(services)
        print("Seeded services")

    db.commit()
    db.close()

if __name__ == "__main__":
    seed_data()
