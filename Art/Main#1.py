import Artist
import Artwork

if __name__ == "__main__":
 user_artist_name = input()
 user_birth_year = int(input())
 user_death_year = int(input())
 user_title = input()
 user_year_created = int(input())
 user_artist = Artist.Artist(user_artist_name, user_birth_year, user_death_year)
 new_artwork = Artwork.Artwork(user_title, user_year_created, user_artist)
 
 user_artist.print_info()
 new_artwork.print_info()