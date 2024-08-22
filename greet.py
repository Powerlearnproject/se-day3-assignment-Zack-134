import random

def greet_user():
  """Prompts the user for their name and prints a random motivational message."""

  name = input("What is your name? ")
  print(f"Hello, {name}!")

  messages = [
    "You've got this!",
    "Believe in yourself.",
    "Never give up.",
    "Keep pushing forward.",
    "Small steps, big results.",
    "You are capable of amazing things.",
    "Today is a new beginning.",
    "Embrace the challenge."
  ]

  random_message = random.choice(messages)
  print(random_message)

greet_user()