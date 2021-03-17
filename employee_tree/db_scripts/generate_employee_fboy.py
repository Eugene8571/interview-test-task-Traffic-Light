from factory.faker import faker
import factory

import os
import django

import sys

sys.path.insert(0,'..')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employee_tree.settings')
django.setup()

from list_of_employees.models import Employees
from datetime import datetime
from datetime import timedelta

import random

adjectives = ('Attractive', 'Bald', 'Beautiful', 'Chubby', 'Clean', 'Dazzling', 'Drab', 'Elegant', 'Fancy', 'Fit', 'Flabby', 'Glamorous', 'Gorgeous', 'Handsome', 'Long', 'Magnificent', 'Muscular', 'Plain', 'Plump', 'Quaint', 'Scruffy', 'Shapely', 'Short', 'Skinny', 'Stocky', 'Ugly', 'Unkempt', 'Unsightly', 'Ashy', 'Black', 'Blue', 'Gray', 'Green', 'Icy', 'Lemon', 'Mango', 'Orange', 'Purple', 'Red', 'Salmon', 'White', 'Yellow', 'Alive', 'Better', 'Careful', 'Clever', 'Dead', 'Easy', 'Famous', 'Gifted', 'Hallowed', 'Helpful', 'Important', 'Inexpensive', 'Mealy', 'Mushy', 'Odd', 'Poor', 'Powerful', 'Rich', 'Shy', 'Tender', 'Unimportant', 'Uninterested', 'Vast', 'Wrong', 'Aggressive', 'Agreeable', 'Ambitious', 'Brave', 'Calm', 'Delightful', 'Eager', 'Faithful', 'Gentle', 'Happy', 'Jolly', 'Kind', 'Lively', 'Nice', 'Obedient', 'Polite', 'Proud', 'Silly', 'Thankful', 'Victorious', 'Witty', 'Wonderful', 'Zealous', 'Angry', 'Bewildered', 'Clumsy', 'Defeated', 'Embarrassed', 'Fierce', 'Grumpy', 'Helpless', 'Itchy', 'Jealous', 'Lazy', 'Mysterious', 'Nervous', 'Obnoxious', 'Panicky', 'Pitiful', 'Repulsive', 'Scary', 'Thoughtless', 'Uptight', 'Worried', 'Broad', 'Chubby', 'Crooked', 'Curved', 'Deep', 'Flat', 'High', 'Hollow', 'Low', 'Narrow', 'Refined', 'Round', 'Shallow', 'Skinny', 'Square', 'Steep', 'Straight', 'Wide', 'Big', 'Colossal', 'Fat', 'Gigantic', 'Great', 'Huge', 'Immense', 'Large', 'Little', 'Mammoth', 'Massive', 'Microscopic', 'Miniature', 'Petite', 'Puny', 'Scrawny', 'Short', 'Small', 'Tall', 'Teeny', 'Tiny', 'Crashing', 'Deafening', 'Echoing', 'Faint', 'Harsh', 'Hissing', 'Howling', 'Loud', 'Melodic', 'Noisy', 'Purring', 'Quiet', 'Rapping', 'Raspy', 'Rhythmic', 'Screeching', 'Shrilling', 'Squeaking', 'Thundering', 'Tinkling', 'Wailing', 'Whining', 'Whispering', 'Ancient', 'Brief', 'Early', 'Fast', 'Future', 'Late', 'Long', 'Modern', 'Old', 'Prehistoric', 'Quick', 'Rapid', 'Short', 'Slow', 'Swift', 'Young', 'Acidic', 'Bitter', 'Cool', 'Creamy', 'Delicious', 'Disgusting', 'Fresh', 'Greasy', 'Juicy', 'Hot', 'Moldy', 'Nutritious', 'Nutty', 'Putrid', 'Rancid', 'Ripe', 'Rotten', 'Salty', 'Savory', 'Sour', 'Spicy', 'Spoiled', 'Stale', 'Sweet', 'Tangy', 'Tart', 'Tasteless', 'Tasty', 'Yummy', 'Breezy', 'Bumpy', 'Chilly', 'Cold', 'Cool', 'Cuddly', 'Damaged', 'Damp', 'Dirty', 'Dry', 'Flaky', 'Fluffy', 'Freezing', 'Greasy', 'Hot', 'Icy', 'Loose', 'Melted', 'Prickly', 'Rough', 'Shaggy', 'Sharp', 'Slimy', 'Sticky', 'Strong', 'Tight', 'Uneven', 'Warm', 'Weak', 'Wet', 'Wooden', 'Abundant', 'Billions', 'Enough', 'Few', 'Full', 'Hundreds', 'Incalculable', 'Limited', 'Little', 'Many', 'Most', 'Millions', 'Numerous', 'Scarce', 'Some', 'Sparse', 'Substantial', 'Thousands')

list_of_departments = 'abcdefghijklmnopqrstuvwxyz'

ranks = ['I', 'II', 'III', 'IV', 'V']

list_of_positions = [
'Team Leader',
'Manager',
'Assistant Manager',
'Director',
'Administrator'
]



class RandomEmployeeFactory(factory.Factory):
    class Meta:
        model = Employees

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    middle_name = random.choice(adjectives)
    date_of_employment = datetime.today() - timedelta(days=random.randint(1,1000))
    salary = random.randint(25, 100)
    department = random.choice(list_of_departments).upper()
    position = random.choice(list_of_positions).upper()
    rank = random.choice(adjectives)


# emp = RandomEmployeeFactory()
# print(f"{emp.first_name=}")
# print(f"{emp.middle_name=}")
# print(f"{emp.first_name=}")
# print(f"{emp.date_of_employment=}")
# print(f"{emp.salary=}")
# print(f"{emp.department=}")
# print(f"{emp.position=}")










