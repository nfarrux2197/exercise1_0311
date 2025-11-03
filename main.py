class ObHavo:
    def __init__(self, shahar, harorat, holat):
        self.shahar = shahar
        self.harorat = harorat
        self.holat = holat

    def malumot(self):
        return f"Shahar: {self.shahar}, Harorat: {self.harorat}°C, Holat: {self.holat}"

    def harorat_yangila(self, yangi_harorat):
        self.harorat = yangi_harorat
        print(f"{self.shahar} shahrida harorat yangilandi: {self.harorat}°C")


toshkent = ObHavo("Toshkent", 25, "Quyoshli")
print(toshkent.malumot())

toshkent.harorat_yangila(28)
print(toshkent.malumot())
