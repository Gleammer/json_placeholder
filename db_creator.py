import json
from random import randrange

''' Set-up authors constant '''
authors = [
	{
		'author_id': 1,
		'author_name': 'Autor 1',
		'author_avatar': 'https://picsum.photos/50',
		'lyceum_id': 1,
		'lyceum_name': 'Liceul 1',
		'date': "2020-01-08T18:52:50.637635"
	},
	{
		'author_id': 2,
		'author_name': 'Autor 2',
		'author_avatar': 'https://picsum.photos/50',
		'lyceum_id': 1,
		'lyceum_name': 'Liceul 1',
		'date': "2020-01-08T18:52:50.637635"
	},
	{
		'author_id': 3,
		'author_name': 'Autor 3',
		'author_avatar': 'https://picsum.photos/50',
		'lyceum_id': 2,
		'lyceum_name': 'Liceul 2',
		'date': "2020-01-08T18:52:50.637635"
	},
	{
		'author_id': 4,
		'author_name': 'Autor 4',
		'author_avatar': 'https://picsum.photos/50',
		'lyceum_id': 2,
		'lyceum_name': 'Liceul 2',
		'date': "2020-01-08T18:52:50.637635"
	}
]

categories = [
	{
		'categories_id': 1,
		'categories_title': 'Categoria 1'
	},
	{
		'categories_id': 2,
		'categories_title': 'Categoria 2'
	},
	{
		'categories_id': 3,
		'categories_title': 'Categoria 3'
	},
	{
		'categories_id': 4,
		'categories_title': 'Categoria 4'
	}
]

def get_post_meta():
	return authors[randrange(len(authors))]

def get_lesson_categories(index):
	return categories[index]

def get_lesson_clip(index):
	c_temp = {}
	c_temp['clip_id'] = index
	c_temp['clip_title'] = "Clip " + str(index)
	c_temp['clip_thumbnail'] = "https://picsum.photos/id/" + str(index) + "/300/200"
	c_temp['clip_description'] = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur."
	c_temp['clip_categories'] = []
	for x in range(randrange(4) + 1):
		c_temp['clip_categories'].append(get_lesson_categories(x))
	c_temp['clip_video_url'] = "https://youtu.be/dQw4w9WgXcQ"
	return c_temp

def create_item(index):
	temp = {}
	temp['id'] = index
	temp['thumbnail'] = "https://picsum.photos/id/" + str(index) + "/300/200"
	temp['description'] = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur."
	if(randrange(2)):
		temp['type'] = "post"
		temp['metadata'] = get_post_meta()
		if(randrange(2)):
			temp['is_video'] = True
			temp['video_url'] = "https://youtu.be/dQw4w9WgXcQ"
		else:
			temp['is_video'] = False
	else:
		temp['type'] = "lesson"
		temp['video_url'] = "https://youtu.be/dQw4w9WgXcQ"
		temp['categories'] = []
		for x in range(randrange(4) + 1):
			temp['categories'].append(get_lesson_categories(x))
		temp['extern'] = "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."			
		temp['clips'] = []
		for x in range(randrange(4)):
			temp['clips'].append(get_lesson_clip(x))
	return temp

''' Setting up the data object '''
data = {}
data['items'] = []

for x in range(40):
	data['items'].append(create_item(x))

''' Useful for testing the outcome of db_cretor.py '''
'''
with open('testing_db.json', 'w') as outfile:
	json.dump(data, outfile)
'''

with open('db.json', 'w') as outfile:
	json.dump(data, outfile)