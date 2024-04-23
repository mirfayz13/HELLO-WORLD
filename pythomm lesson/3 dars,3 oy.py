class Base:
      def __init__(self, id , name , rating , status , comment , mentor ):
            self.id=id
            self.name=name
            self.rating=rating
            self.status=status
            self.comment=comment
            self.mentor=mentor

def __str__(self):
      return f"{id} {name} {surname}"

asos=Base(123,Mirf,Zara)

class Subject(Base):
      def __init__(self,id,name,reyting,status,comment,mentor,active_students):
            super().__init__(id,name,reyting,status,comment,mentor)
            self.active_students=active_students

            def __str__(self):
                  return f"{self.id} {self.name}"
            



class Lesson(Base):
      def __init__(self,id,name,reyting,status,comment,mentor,homework,date):
            Base.__init__(self,id,name,reyting,status,comment,mentor)
            self.homework=homework
            self.date=date
            
class Student:
      def __init__(self,name,surname,year,course,field,interests,height,weight,number,location):
            self.name=name
            self.surname=surname
            self.year=year
            self.course=course
            self.field=field
            self.interests=interests
            self.height=height
            self.weight=weight
            self.number=number
            self.location=location


def __str__(self):
      return f"{name} {surname}"

talaba=Student("Mirfayz","Zaripov",2004,"second","finance")

class UniversityStudent(Student):
    def __init__(self, name, surname, year, course, field, interests, height, weight, number, location, university):
       
        super().__init__(name, surname, year, course, field, interests, height, weight, number, location)
        self.university = university

university_student = UniversityStudent("Mirfayz", "Zaripov", 2004, "second", "finance", "Programming", 175, 68, "123456789", "City University", "Finance Department")

class Student:
    

    def display_info(self):
        print(f"Student: {self.name} {self.surname}, Year: {self.year}, Course: {self.course}")

class UniversityStudent(Student):


   
    def display_info(self):
        print(f"University Student: {self.name} {self.surname}, Year: {self.year}, Course: {self.course}, University: {self.university}")


student = Student("John", "Doe", 2023, "first", "engineering", "Physics", 180, 70, "987654321", "Town University")
university_student = UniversityStudent("Mirfayz", "Zaripov", 2004, "second", "finance", "Programming", 175, 68, "123456789", "City University", "Finance Department")

student.display_info()
university_student.display_info()


class Football_player:
      def __init__(self,name,surname,strong_foot,club,nationality,number: int,favorite_team,height: int,weight: int,year:int):
            self.name=name
            self.surname=surname
            self.strong_foot=strong_foot
            self.club=club
            self.nationality=nationality
            self.number=number
            self.favorite_team=favorite_team
            self.height=height
            self.weight=weight
            self.year=year
futbolchi=Football_player("Mirfayz","Zaripov","right","FC Bukhara","Uzbek")

class Goalkeeper(Football_player):
    def __init__(self, name, surname, strong_foot, club, nationality, number, favorite_team, height, weight, year, gloves_brand):
        
        super().__init__(name, surname, strong_foot, club, nationality, number, favorite_team, height, weight, year)
        self.gloves_brand = gloves_brand

    def display_info(self):
       
        print(f"Goalkeeper: {self.name} {self.surname}, Club: {self.club}, Gloves Brand: {self.gloves_brand}")


football_player = Football_player("Mirfayz", "Zaripov", "right", "FC Bukhara", "Uzbek", 10, "Real Madrid", 180, 75, 1995)


goalkeeper = Goalkeeper("Iker", "Casillas", "left", "FC Porto", "Spanish", 1, "Real Madrid", 185, 82, 1981, "Nike")


football_player.display_info()
goalkeeper.display_info()

class Telephone:
      def __init__(self,name,brand,model,year:int,colour,battery,camera,storage: int,battery_health:int,size:int):
            self.name=name
            self.brand=brand
            self.model=model
            self.year=year
            self.colour=colour
            self.battery=battery
            self.camera=camera
            self.storage=storage
            self.battery_health=battery_health
            self.size=size

telefon=Telephone("Iphone","Apple","XII",2024,"black")

class Smartphone(Telephone):
    def __init__(self, name, brand, model, year, colour, battery, camera, storage, battery_health, size, operating_system):
        
        super().__init__(name, brand, model, year, colour, battery, camera, storage, battery_health, size)
        self.operating_system = operating_system

    def display_info(self):
       
        print(f"Smartphone: {self.name} {self.model}, Brand: {self.brand}, OS: {self.operating_system}")


telephone = Telephone("Generic Phone", "Unknown", "Basic Model", 2022, "Silver", "3000 mAh", "Basic Camera", 16, 100, 5)

smartphone = Smartphone("iPhone", "Apple", "XII", 2024, "Black", "4000 mAh", "Advanced Camera", 128, 95, 6.1, "iOS")


telephone.display_info()
smartphone.display_info()

class Computer:
      def __init__(self,type,brand,model,year:int,colour,battery,camera,storage: int,battery_health:int,size:int):
            self.type=type
            self.brand=brand
            self.model=model
            self.year=year
            self.colour=colour
            self.battery=battery
            self.camera=camera
            self.storage=storage
            self.battery_health=battery_health
            self.size=size

kompyuter=Computer("Laptop","Apple","M1",2024,"Black")

class Computer:
    def __init__(self, type, brand, model, year, colour, battery, camera, storage, battery_health, size):
        self.type = type
        self.brand = brand
        self.model = model
        self.year = year
        self.colour = colour
        self.battery = battery
        self.camera = camera
        self.storage = storage
        self.battery_health = battery_health
        self.size = size

kompyuter = Computer("Laptop", "Apple", "M1", 2024, "Black")

class DesktopComputer(Computer):
    def __init__(self, type, brand, model, year, colour, battery, camera, storage, battery_health, size, monitor_size):
        super().__init__(type, brand, model, year, colour, battery, camera, storage, battery_health, size)
        self.monitor_size = monitor_size

    def display_info(self):
        print(f"Desktop Computer: {self.brand} {self.model}, Monitor Size: {self.monitor_size}")

computer = Computer("Generic", "Unknown", "Basic Model", 2022, "Silver", "No Battery", "No Camera", 512, 100, 15)
desktop_computer = DesktopComputer("Desktop", "Dell", "Inspiron", 2024, "Black", "No Battery", "No Camera", 1024, 95, 21.5, "27 inches")

computer.display_info()
desktop_computer.display_info()


class Car:
      def __init__(self,model,brand,weight: int,year: int,colour: str,speed: int,type: str,seats: int,country: str,watt: str):
            self.model=model
            self.brand=brand
            self.weight=weight
            self.year=year
            self.colour=colour
            self.speed=speed
            self.type=type
            self.seats=seats
            self.country=country
            self.watt=watt

      def __str__(self):
            return f"{self.country}"
Mashina=Car("bmw","m7",1 ,2022,"black",220,"hybrid",5,"Germany","bmw")

print(Mashina)

class ElectricCar(Car):
    def __init__(self, model, brand, weight, year, colour, speed, type, seats, country, watt, battery_capacity):
        super().__init__(model, brand, weight, year, colour, speed, type, seats, country, watt)
        self.battery_capacity = battery_capacity

    def __str__(self):
        return f"Electric Car: {self.brand} {self.model}, Country: {self.country}, Battery Capacity: {self.battery_capacity} kWh"



car = Car("bmw", "m7", 1, 2022, "black", 220, "hybrid", 5, "Germany", "bmw")

electric_car = ElectricCar("Tesla", "Model S", 2, 2023, "blue", 250, "electric", 5, "USA", "tesla", 100)


print(car)
print(electric_car)

class Laptop:
      def __init__(self,model,brand,type_of_screen,year:int,colour,battery,camera,storage: int,battery_health:int,size:int):
            self.model=model
            self.brand=brand
            self.type_of_screen=type_of_screen
            self.year=year
            self.colour=colour
            self.battery=battery
            self.camera=camera
            self.storage=storage
            self.battery_health=battery_health
            self.size=size
notbuk=Laptop("M2","Apple","LCD",2023,"White")

class Tablet(Laptop):
    def __init__(self, model, brand, type_of_screen, year, colour, battery, camera, storage, battery_health, size, touch_pen):
        super().__init__(model, brand, type_of_screen, year, colour, battery, camera, storage, battery_health, size)
        self.touch_pen = touch_pen

    def display_info(self):
        print(f"Tablet: {self.brand} {self.model}, Screen Type: {self.type_of_screen}, Touch Pen: {self.touch_pen}")


laptop = Laptop("M2", "Apple", "LCD", 2023, "White")
tablet = Tablet("iPad", "Apple", "Retina", 2024, "Silver", "Li-ion", "8 MP", 128, 90, 10.2, True)

laptop.display_info()
tablet.display_info()

class Games:
      def __init__(self,name,year:int,size:int,level:int,rating: int,content,flexibility,functionality,creative_brief,music):
            self.name=name
            self.year=year
            self.size=size
            self.level=level
            self.rating=rating
            self.content=content
            self.flexibility=flexibility
            self.functionality=functionality
            self.creative_brief=creative_brief
            self.music=music

oyinlar=Games("Pubg",2018,2,5,5)

class MobileGame(Games):
    def __init__(self, name, year, size, level, rating, content, flexibility, functionality, creative_brief, music, mobile_platform):
        super().__init__(name, year, size, level, rating, content, flexibility, functionality, creative_brief, music)
        self.mobile_platform = mobile_platform

    def display_info(self):
        print(f"Mobile Game: {self.name}, Year: {self.year}, Rating: {self.rating}, Platform: {self.mobile_platform}")

class PCGame(Games):
    def __init__(self, name, year, size, level, rating, content, flexibility, functionality, creative_brief, music, pc_requirements):
        super().__init__(name, year, size, level, rating, content, flexibility, functionality, creative_brief, music)
        self.pc_requirements = pc_requirements

    def display_info(self):
        print(f"PC Game: {self.name}, Year: {self.year}, Rating: {self.rating}, Requirements: {self.pc_requirements}")

game = Games("Pubg", 2018, 2, 5, 5)
mobile_game = MobileGame("Angry Birds", 2010, 0.5, 3, 4, "Casual", "High", "Good", "Simple", "Catchy", "Mobile")
pc_game = PCGame("The Witcher 3", 2015, 50, 8, 9, "Open World", "Medium", "Excellent", "Complex", "Epic", "High-End PC")

game.display_info()
mobile_game.display_info()
pc_game.display_info()

class Music:
      def __init__(self,author,written_by,rythm,year:int,texture,structure,expression,beats,melody,harmony):
            self.author=author
            self.written_by=written_by
            self.rythm.rythm
            self.year=year
            self.texture=texture
            self.structure=structure
            self.expression=expression
            self.beats=beats
            self.melody=melody
            self.harmony.harmony

musiqa=Music("Luis","Fonsi","intensive",2012,"very fast")

class PopMusic(Music):
    def __init__(self, author, written_by, rythm, year, texture, structure, expression, beats, melody, harmony, danceability):
        super().__init__(author, written_by, rythm, year, texture, structure, expression, beats, melody, harmony)
        self.danceability = danceability

    def display_info(self):
        print(f"Pop Music: {self.author}, Year: {self.year}, Danceability: {self.danceability}")

class ClassicalMusic(Music):
    def __init__(self, author, written_by, rythm, year, texture, structure, expression, beats, melody, harmony, orchestration):
        super().__init__(author, written_by, rythm, year, texture, structure, expression, beats, melody, harmony)
        self.orchestration = orchestration

    def display_info(self):
        print(f"Classical Music: {self.author}, Year: {self.year}, Orchestration: {self.orchestration}")


music = Music("Luis", "Fonsi", "intensive", 2012, "very fast")

pop_music = PopMusic("Ed Sheeran", "Ed Sheeran", "upbeat", 2017, "simple", "verse-chorus-verse", "emotional", "moderate", "catchy", "harmonic", "High")
classical_music = ClassicalMusic("Beethoven", "Beethoven", "steady", 1804, "complex", "sonata-allegro", "expressive", "moderate", "melodic", "contrapuntal", "Orchestra")

music.display_info()
pop_music.display_info()
classical_music.display_info()

class Tv:
      def __init__(self,screen,size:int,brand,type,contrast:int,panel,digital,services,media_player,interface):
            self.screen=screen
            self.size=size
            self.brand=brand
            self.type=type
            self.contrast=contrast
            self.panel=panel
            self.digital=digital
            self.services=services
            self.media_player=media_player
            self.interface=interface

televizor=Tv("Led",64,"Apple","Plasma",70)

class SmartTV(Tv):
    def __init__(self, screen, size, brand, type, contrast, panel, digital, services, media_player, interface, smart_features):
        super().__init__(screen, size, brand, type, contrast, panel, digital, services, media_player, interface)
        self.smart_features = smart_features

    def display_info(self):
        print(f"Smart TV: {self.brand}, Size: {self.size}, Smart Features: {self.smart_features}")

class OLED_TV(Tv):
    def __init__(self, screen, size, brand, type, contrast, panel, digital, services, media_player, interface, thickness):
        super().__init__(screen, size, brand, type, contrast, panel, digital, services, media_player, interface)
        self.thickness = thickness

    def display_info(self):
        print(f"OLED TV: {self.brand}, Size: {self.size}, Thickness: {self.thickness}mm")


tv = Tv("Led", 64, "Apple", "Plasma", 70)
smart_tv = SmartTV("OLED", 55, "Samsung", "OLED", 100, "AMOLED", "Yes", "Netflix, Hulu", "Built-in", "SmartHub", "Voice Control")
oled_tv = OLED_TV("OLED", 65, "LG", "OLED", 120, "OLED", "Yes", "Amazon Prime, Disney+", "Built-in", "WebOS", 5)
tv.display_info()
smart_tv.display_info()
oled_tv.display_info()

class Home:
      def __init__(self,location,type_of_accomadation,rooms,country,city,size:int,floor,phone_number,address,ownership_status):
            self.location=location
            self.type_of_accomadation=type_of_accomadation
            self.rooms=rooms
            self.country=country
            self.city=city
            self.size=size
            self.floor=floor
            self.phone_number=phone_number
            self.address=address
            self.ownership_status=ownership_status

uy=Home("Bukhara","cottage",4,"country","Bukhara")

class Apartment(Home):
    def __init__(self, location, type_of_accommodation, rooms, country, city, size, floor, phone_number, address, ownership_status, amenities):
        super().__init__(location, type_of_accommodation, rooms, country, city, size, floor, phone_number, address, ownership_status)
        self.amenities = amenities

    def display_info(self):
        print(f"Apartment: {self.type_of_accomadation}, Location: {self.location}, Rooms: {self.rooms}, Amenities: {self.amenities}")

class Villa(Home):
    def __init__(self, location, type_of_accommodation, rooms, country, city, size, floor, phone_number, address, ownership_status, garden_size):
        super().__init__(location, type_of_accommodation, rooms, country, city, size, floor, phone_number, address, ownership_status)
        self.garden_size = garden_size

    def display_info(self):
        print(f"Villa: {self.type_of_accomadation}, Location: {self.location}, Rooms: {self.rooms}, Garden Size: {self.garden_size}")

home = Home("Bukhara", "cottage", 4, "country", "Bukhara")
apartment = Apartment("Tashkent", "apartment", 2, "Uzbekistan", "Tashkent", 80, 5, "123-456-7890", "123 Main St", "owned", "Balcony, Gym")
villa = Villa("Samarkand", "villa", 6, "Uzbekistan", "Samarkand", 300, 2, "987-654-3210", "456 Oak St", "rented", "Large")
home.display_info()
apartment.display_info()
villa.display_info()

#Polymorf.Methodni nomi bir xil boladi lekin ichi har xil