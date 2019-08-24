#Connect to datastore




def create_post(name, content):
    #Insert data into datastore
    from google.cloud import datastore
    import datetime
    client = datastore.Client()
    key = client.key('posts', name + datetime.datetime.now())
    entity = datastore.Entity(key=key)
    entity.update({
        'userName': name,
        'userPost': content
    })
    client.put(entity)

    posts = [name, content]
    return posts

def get_posts():
    #Retrieve data from datastore
    posts = ['bob', 'Hello World!']
    return posts

