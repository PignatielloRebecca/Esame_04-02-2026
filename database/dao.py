from database.DB_connect import DBConnect
from model.authorship import Authorship
from model.artist import Artist
from model.artista import Artista

class DAO:

    @staticmethod
    def get_authorship():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ select distinct role
                    FROM authorship"""
        cursor.execute(query)

        for row in cursor:
            result.append(row["role"])

        cursor.close()
        conn.close()
        return result

    @staticmethod

    def get_all_artista(ruolo):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """  select  a.artist_id as artist_id , a.name as name, count(*) as peso 
                    from authorship au, artists a , objects o 
                    where a.artist_id =au.artist_id and au.role=%s and au.object_id=o.object_id and curator_approved=1 
                    group by a.artist_id, a.name"""
        cursor.execute(query, (ruolo,))

        for row in cursor:
            result.append(Artista(row['artist_id'], row['name'], row['peso']))

        cursor.close()
        conn.close()
        return result


    @staticmethod

    def get_all_connessioni(ruolo):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ select distinct p1.artist_id as a1, p2.artist_id as a2, (p2.produttività-p1.produttività) as peso
 from (select  a.artist_id, a.name, count(*) as produttività 
 		from authorship au, artists a , objects o 
 		where a.artist_id =au.artist_id and au.role= %s and au.object_id=o.object_id and curator_approved=1 
 		group by a.artist_id, a.name ) p1, 
 		(select  a.artist_id, a.name, count(*) as produttività 
 		from authorship au, artists a , objects o 
 		where a.artist_id =au.artist_id and au.role= %s and au.object_id=o.object_id and curator_approved=1 
 		group by a.artist_id, a.name ) p2
where p1.artist_id<> p2.artist_id and p1.produttività< p2.produttività
group by p1.artist_id, p2.artist_id  
 		 """
        cursor.execute(query, (ruolo, ruolo))

        for row in cursor:
            result.append((row['a1'], row['a2'], row['peso']))

        cursor.close()
        conn.close()
        return result








