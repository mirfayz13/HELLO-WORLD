#Encapsulation
#it is divided into two parts named private and public
class Telephone:
    def __init__(self,name,company,seria):
        self.name=name
        self.company=company
        self.seria=seria

    def __str__(self) -> str:
        return f"{self.name} {self.company} {self.seria}"

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

#print(samsung)



class User:
    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.__password = password

    def login(self):
        return f"User {self.username} is logging"

    def log_out(self):
        return f"User {self.username} is log out"

    def get_password(self):
        return self.__password

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.username} {self.get_password()}"


class Teacher(User):
    def __init__(self, first_name, last_name, username, password, teacher_id):
        super().__init__(first_name, last_name, username, password)
        self.__teacher_id = teacher_id

    def get_teacher_id(self):
        return self.__teacher_id

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.username} {Teacher.get_password(self)} {Teacher.get_teacher_id(self)}"


class Assistant(Teacher):
    def __init__(self, first_name, last_name, username, password, teacher_id, subject):
        super().__init__(first_name, last_name, username, password, teacher_id)
        self.__subject = subject

    def get_subject(self):
        return self.__subject

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.get_subject()}"


class Mentor(Assistant):
    def __init__(self, first_name, last_name, username, password, teacher_id, subject, teaching_time):
        super().__init__(first_name, last_name, username, password, teacher_id, subject)
        self.teaching_time = teaching_time


mentor = Mentor("Alisher", "Kholov", 12348, "Barca", 8978, "Python", "Morning")
#print(mentor.log_out())






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








