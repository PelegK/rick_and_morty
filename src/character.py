import requests
import random
import os


class Character:
    def __init__(self, id, name, status, species, gender, location, image):
        self.id = id
        self.name = name
        self.status = status
        self.species = species
        self.gender = gender
        self.location = location
        self.image = image

    def __str__(self):
        return f"Hi! I'm {self.name}, My ID is {self.id}, I'm from {self.location}, my gender is a {self.gender}, my status is {self.status} and i'm a {self.species}"


base_url = "https://rickandmortyapi.com/api/"
def get_episodes():
  response = requests.get(base_url+'episode')
  assert response.status_code == 200
  data = response.json()
  return data['results']

def get_random_episode(episodes):
  filter_episodes = [episode for episode in episodes if len(episode['characters']) >= 30]
  random_episode = random.choice(filter_episodes)
  print(f'Selected episode is "{random_episode["name"]}" which has {len(random_episode["characters"])} characters')
  return random_episode

def get_characters(selected_episode):
  selected_characters = random.sample(selected_episode['characters'], 2)
  return selected_characters

def create_characters():
  file_name = "src/characters_introduction.txt"
  if os.path.exists(file_name):
    os.remove(file_name)
  episodes = get_episodes()
  random_episode = get_random_episode(episodes)
  selected_characters = get_characters(random_episode)
  characters_data = {}
  for character_url in selected_characters:
      response = requests.get(character_url)
      character_data = response.json()
      character = Character(
          id=character_data['id'],
          name=character_data['name'],
          status=character_data['status'],
          species=character_data['species'],
          gender=character_data['gender'],
          location=character_data['location']['name'],
          image = character_data['image']
      )
      characters_data[f"Character{len(characters_data)+1}"] = {"name": character.name, "id": character.id, "location": character.location, "image": character.image}
      with open(file_name, "a") as file:
          file.write(f"{str(character)}\n")
  return characters_data