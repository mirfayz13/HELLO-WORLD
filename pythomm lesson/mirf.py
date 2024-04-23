#1
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

talaba=Student("Mirfayz","Zaripov",2004,"second","finance")

#2
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
#3
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

#4
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

#5
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

#6
class Basketball_player:
      def __init__(self,name,surname,strong_hand,club,nationality,number: int,favorite_team,height: int,weight: int,year:int):
            self.name=name
            self.surname=surname
            self.strong_hand=strong_hand
            self.club=club
            self.nationality=nationality
            self.number=number
            self.favorite_team=favorite_team
            self.height=height
            self.weight=weight
            self.year=year
basketbol=Basketball_player("Shahruz","Shomurodov","left","Barcelona","uzbek")
#7
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

#8
class Universities:
      def __init__(self,name,country,city,location,established_year:int,number_of_faculties:int,number_of_students:int,contract_fee:int,number_of_buildings:int,number_of_teachers:int):
            self.name=name
            self.country=country
            self.city=city
            self.location=location
            self.established_year=established_year
            self.number_of_faculties=number_of_faculties
            self.number_of_students=number_of_students
            self.contract_fee=contract_fee
            self.number_of_buildings=number_of_buildings
            self.number_of_teachers=number_of_teachers

universitetlar=Universities("Wiut","Uzbekistan","Tashkent","Istiqlol street",2002)

#9
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

#10
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

#11
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

#12
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

#13
class Voleyball_player:
      def __init__(self,name,surname,strong_hand,club,nationality,number: int,favorite_team,height: int,weight: int,year:int):
            self.name=name
            self.surname=surname
            self.strong_hand=strong_hand
            self.club=club
            self.nationality=nationality
            self.number=number
            self.favorite_team=favorite_team
            self.height=height
            self.weight=weight
            self.year=year

voleybol=Voleyball_player("Alisher","Rakhmatov","right","Real Madrid","uzbek")

#14
class Pupil:
      def __init__(self,name,surname,id_number:int,sinf:int,year:int,location,country,city,nationality,height):
            self.name=name
            self.surname=surname
            self.id_number=id_number
            self.sinf=sinf
            self.year=year
            self.location=location
            self.country=country
            self.city=city
            self.nationality=nationality
            self.height=height

oquvchi=Pupil("Mirfayz","Zaripov",000,10,2004)

#15
class Musical_instruments:
      def __init__(self,type,name,sort,colour,year:int,speed,string,brass,keyboard,percussion):
            self.type=type
            self.name=name
            self.sort=sort
            self.colour=colour
            self.year=year
            self.speed=speed
            self.brass=brass
            self.keyboard=keyboard
            self.percussion=percussion

musiqaa=Musical_instruments("classic","piano","trombone","black",2004)
            
#16
class Baseball_player:
      def __init__(self,name,surname,strong_hand,club,nationality,number: int,favorite_team,height: int,weight: int,year:int):
            self.name=name
            self.surname=surname
            self.strong_hand=strong_hand
            self.club=club
            self.nationality=nationality
            self.number=number
            self.favorite_team=favorite_team
            self.height=height
            self.weight=weight
            self.year=year

beysbol=Baseball_player_player("Shohruh","Alisherov","right","Totenham","uzbek")

#17
class Teacher:
      def __init__(self,name,surname,father_name,id:int,year:int,experience_year:int,university,country,city,location):
            self.name=name
            self.surname=surname
            self.father_name=father_name
            self.id=id
            self.year=year
            self.experience_year=experience_year
            self.university=university
            self.country=country
            self.city=city
            self.location=location

ustoz=Teacher("Nozim","Ibrohimov","ikromovich",2323,1998)

#18
class School:
      def __init__(self,name,country,city,location,established_year:int,number_of_faculties:int,number_of_students:int,contract_fee:int,number_of_buildings:int,number_of_teachers:int):
            self.name=name
            self.country=country
            self.city=city
            self.location=location
            self.established_year=established_year
            self.number_of_faculties=number_of_faculties
            self.number_of_students=number_of_students
            self.contract_fee=contract_fee
            self.number_of_buildings=number_of_buildings
            self.number_of_teachers=number_of_teachers

maktablar=School("Hamza","Uzbekistan","Bukhara","Beruniy street",1992)

#19
class Iphone:
      def __init__(self,name,brand,year:int,colour,camera,battery,battery_health:int,size,power):
            self.name=name
            self.brand=brand
            self.year=year
            self.colour=colour
            self.camera=camera
            self.battery=battery
            self.battery_health=battery_health
            self.size=size
            self.power=power

ayfon=Iphone("XV","Iphone",2021,"Gold","hz")

#20
class Shop:
      def __init__(self,country,city,street,type,name,size:int,lenght:int,year:int,payment,services):
            self.country=country
            self.city=city
            self.street=street
            self.type=type
            self.name=name
            self.size=size
            self.lenght=lenght
            self.year=year
            self.payment=payment
            self.services=services

magazin=Shop("Germany","Munich","Ludwig","clothes","Zara")






 #birinchisi object va =dan keyin class
#20 ta class har birini ichida 10 tadan argument va ichida 5 tadan method