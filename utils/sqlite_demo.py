import sqlite3

conn = sqlite3.connect('provinha.db')

c = conn.cursor()

def connect_database():
    connection = sqlite3.connect('provinha.db')

    return connection.cursor()

def insert_idlike(idlike):
    with conn:
        c.execute("INSERT INTO idlike VALUES (:id, :like)", {'id': idlike.id, 'like': idlike.like})

def update_idlike(idlike):
    with conn:
        c.execute("UPDATE idlike SET like = :like", {'like': idlike.like})

def delete_idlike(id):
    with conn:
        c.execute("DELETE FROM idlike where id = :id", {'id': id})

def get_idlike_by_id(id):
    with conn:
        c.execute("SELECT * FROM idlike where id = :id", {'id': id})
        
    return c.fetchall()

def get_idlike():
    with conn:
        c.execute("SELECT * FROM idlike")

    return c.fetchall()
    
print(get_idlike())

conn.close()

# neighbourhood_group,room_type,price
# ,id,name,host_id,host_name,neighbourhood,latitude,longitude,room_type,price,minimum_nights,number_of_reviews,last_review,reviews_per_month,calculated_host_listings_count,availability_365,neighbourhood_group