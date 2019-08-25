#Connect to datastore




def create_post(name, content):
    #Insert data into datastore
    from google.cloud import datastore
    import datetime
    client = datastore.Client()
    currentTime = datetime.datetime.now()
    key = client.key('posts', str(currentTime))
    entity = datastore.Entity(key=key)
    entity.update({
        'userName': name,
        'userPost': content
    })
    client.put(entity)

    

def get_posts():
    #Retrieve data from datastore
    from google.cloud import datastore
    client = datastore.Client()

    query = client.query(kind='posts')
    results = list(query.fetch())

    return results

