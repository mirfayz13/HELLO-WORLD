'''
class Phone:
      def __init__(self,lenght,weight,price,colour,brand):
            self.lenght = lenght
            self.weight = weight
            self.price = price
            self.colour = colour
            self.brand = brand

      def __str__(self):
            return f"{lenght} {weight} {price} {colour} {brand}"
      def __le__(self,other):
            if self.weight > other.massa
            else:
            return False

telefon=Telephone(23,275,700,white,Apple)



class Laptop:
      def __init__(self,lenght,weight,price,colour,brand):
            self.weight = weight
            self.price = price
            self.colour = colour
            self.brand = brand 

      def __str__(self):
            return f"{lenght} {weight} {price} {colour} {brand}"
      

notbuk=Laptop()

telefon=Phone(23,34,400,"white,"Applpe)
notbuk=Laptop(34,45,600,"white","Samsung")

if telefon.__le__(notbuk):
    print("Telefon katta")



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

      def __str__(self) -> str:
          return f"{self.name} {self.year} {self.size} {self.level} {self.rating} {self.content} {self.flexibility} {self.functionality} {self.creative_brief} {self.music}"
      
      def degree(self):
          return f"{level} {rating}"
      
      @staticmethod
      def about():
        return "This is about Games class"
      
      @classmethod
      def create object(cls,data: list):
      name = data[0]
      year = data[1]
      size = data[2]
      level = data[3]
      return cls(name,year,size,level)
      

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


      def __str__(self) -> str:
          return f"{author} {written_by} {rythm} {year} {texture} {structure} {expression} {beats} {melody} {harmony}"
      
      @staticmethod
      def about():
        return "This is about Games class"
      
      @classmethod
      def create object(cls,data: list):
      author = data[0]
      written_by = data[1]
      rythm = data[2]
      year = data[3]
      return cls(author,written_by,rythm,year)


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



class Telephone:
      def __init__(self,name,company,seria):
        self.name=name
        self.company=company
        self.seria=seria

      def __str__(self) -> str:
        return f"{self.name} {self.company} {self.seria}"
      @staticmethod
      def about():
        return "This is about Games class"
      
      @classmethod
      def create object(cls,data: list):
      name = data[0]
      company = data[1]
      seria = data[2]
      return cls(name,company,seria)

telefon=Telephone("X","Iphone",345)

class Iphone(Telephone):
      def __init__(self, name, company, seria,number):
         super().__init__(name, company, seria)
         self.__number=number

      def get_number(self):
            return self.__number
      
ayfon=Iphone("XII","Apple",2456,+998937878878)

class Nokia(Iphone):
      def __init__(self, name, company, seria, number,weight):
        super().__init__(name, company, seria, number)
        self.weight=weight

      def __str__(self) -> str:
          return f"{self.name} {self.company} {self.seria} {Iphone.get_number(self)} {self.weight}"


nokia=Nokia("FA","Nokia",4567,+9985987,5)

class Samsung(Nokia):
      def __init__(self, name, company, seria, number, weight,lenght):
        super().__init__(name, company, seria, number, weight)  
        self.lenght=lenght

      def __str__(self) -> str:
          return f"{self.name} {self.company} {self.seria} {Iphone.get_number(self)} {self.weight} {self.lenght}"

samsung=Samsung("S20","SAmsung",787,+99807,3,2)


class Football_player:
      def __init__(self,first_name,last_name,club) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.club = club

      def login(self):
        return f"User called {self.first_name} is logged in"

      def log_out(self):
        return f"User called {self.first_name}  logged out"

      def __str__(self) -> str:
         return f"{self.first_name} {self.last_name} {self.club}"
      
      @staticmethod
      def about():
        return "This is about Games class"
      
      @classmethod
      def create object(cls,data: list):
      first_name = data[0]
      last_name = data[1]
      club = data[2]
      return cls(first_name,last_name,club)


futbolchi=Football_player("Leo","Messi","Barcelona")

print(futbolchi)


class Basketball_player(Football_player):
      def __init__(self, first_name, last_name, club,id) -> None:
            super().__init__(first_name, last_name, club)
            self.__id=id

      def get_id(self):
            return self.__id
      
      def __str__(self):
          return f"{self.first_name} {self.last_name} {self.club} {Basketball_player.get_id(self)}"
      
basketbol=Basketball_player("Anthony","Jordan","Atletico",123)

#print(basketbol)

class VoleyballPlayer(Basketball_player):
      def __init__(self, first_name, last_name, club, id,strong_arm):
        super().__init__(first_name, last_name, club, id)
        self.strong_arm=strong_arm

      def __str__(self):
          return f"{self.first_name} {self.last_name} {self.club} {Basketball_player.get_id(self)} {self.strong_arm}"
      
voleybol=VoleyballPlayer("Mike","Antuan","Bayern",2345,"left")


class BaseBallPayer(VoleyballPlayer):
      def __init__(self, first_name, last_name, club, id, strong_arm,seria):
         super().__init__(first_name, last_name, club, id, strong_arm)
         self.seria=seria

      def get_seria(self):
            return self.__seria
      

      def __str__(self):
          return f"{self.first_name} {self.last_name} {self.club} {Basketball_player.get_id(self)} {self.strong_arm} {BaseBallPayer.get_seria(self)}"
      

beysbol=BaseBallPayer("Anvar","Shokirov","Arsenal",3456,"left","A")
      

class TennisPlayer(BaseBallPayer):
      def __init__(self, first_name, last_name, club, id, strong_arm, seria,number):
         super().__init__(first_name, last_name, club, id, strong_arm, seria)
         self.number=number

      def __str__(self):
          return f"{self.first_name} {self.last_name} {self.club} {Basketball_player.get_id(self)} {self.strong_arm} {BaseBallPayer.get_seria(self)} {self.number}"
      
tennis=TennisPlayer("Luca","Eden","Chelsea",3456)
'''



      
