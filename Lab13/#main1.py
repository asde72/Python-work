import sys
class FatBurning:
    def __init__(self,):
        self.age = None
       


    def get_age(self,valid):
        if valid == 1:
            print('''Invalid age.
Could not calculate heart rate info.''')
            sys.exit()
    def calculate_fat_burning_rate(self,age):
        self.age = age
        self.difference = 220 - self.age
        fat_rate = self.difference*0.7
        return fat_rate
if __name__ == '__main__':
    Percentage = FatBurning()
    user_age = int(input("What is your age?"))
    if not 18 <= user_age <= 75:
            range = 1
            Percentage.get_age(1)
    else:
            range = 2
            Percentage.get_age(2)
Rate = Percentage.calculate_fat_burning_rate(user_age) 
print(f'''Fat burning rate for a {user_age} year-old: {Rate} bpm ''')
