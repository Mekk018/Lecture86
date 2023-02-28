
import csv

with open('TestLecture86.csv', mode='w') as Favorite_file:
    Column_writer = csv.writer(Favorite_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    Column_writer.writerow(['NAME', 'MOVIE', 'PET'])
    Column_writer.writerow(['Mekk', 'Dragonball', 'Cat'])
    Column_writer.writerow(['Jj', 'Tom & Jerry', 'Cat'])
    Column_writer.writerow(['Sky', 'ABC', 'Dog'])
    Column_writer.writerow(['Srimork', 'Boots', 'Mouse'])
