import splinter
import pickle

# cities to loop over its neighbors: Tel Aviv district
# features: prices, social indices, education, density of buying and selling (from the map).
# rate according to features (after clustering)

# scraping flow: all country > districts > tel aviv district > cities > neighborhoods : prices table >
# social indices table

# data samples are neighborhoods, features are: city, prices (do manual feature selection),
# socials (do manual feature selection). 