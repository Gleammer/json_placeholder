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
	c_temp['clip_description'] = "Desciption_cont."
	c_temp['clip_categories'] = []
	for x in range(randrange(3) + 1):
		c_temp['clip_categories'].append(get_lesson_categories(x))
	c_temp['clip_video_url'] = "https://youtu.be/dQw4w9WgXcQ"
	return c_temp

def create_item(index):
	temp = {}
	temp['id'] = index
	temp['thumbnail'] = "https://picsum.photos/id/" + str(index) + "/300/200"
	temp['description'] = "Desciption_cont."
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
		for x in range(randrange(3) + 1):
			temp['categories'].append(get_lesson_categories(x))
		temp['extern'] = "Extern_cont."			
		temp['clips'] = []
		for x in range(randrange(4)):
			temp['clips'].append(get_lesson_clip(x))
	return temp

''' Setting up the data object '''
data = {}
data['items'] = []

for x in range(20):
	data['items'].append(create_item(x))

''' Useful for testing the outcome of db_cretor.py '''
'''
with open('testing_db.json', 'w') as outfile:
	json.dump(data, outfile, sort_keys=True, indent=4)
'''

with open('db.json', 'w') as outfile:
	json.dump(data, outfile, separators=(',',':'))