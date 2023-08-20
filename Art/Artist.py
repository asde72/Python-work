class Artist:
# TODO: Define constructor with parameters to initialize instance attributes
    def __init__(self, name = 'unkown', death_year = -1 ,birth_year = -1,):
        self.name = name
        self.death_year = death_year
        self.birth_year = birth_year

        
# (name, birth_year, death_year)
# TODO: Define print_info() method
    def print_info(self):
        if self.birth_year > 0 and self.death_year > 0:
            print(f'Artist: {self.name} ({self.birth_year} to {self.death_year})')
        elif self.birth_year > 0 and self.death_year < 0:
            print(f'Artist: {self.name} ({self.birth_year} to present)')
        else:
            print(f'Artist: {self.name} (unknown)')