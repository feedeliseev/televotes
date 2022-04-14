import sqlite3

class voter():
    def __init__(self, chat_id, vote_ivan, vote_farid):
        self.chat_id = chat_id
        self.vote_ivan = vote_ivan
        self.vote_farid = vote_farid
    def add_vote(self):
        conn = sqlite3.connect('votes.db')
        cursor = conn.cursor()
        cursor.execute("insert into votes(id, ivan, farid) values(?, ?, ?)", (self.chat_id, self.vote_ivan, self.vote_farid))
        conn.commit()
        cursor.close()


def spectate_vote():
    conn = sqlite3.connect('votes.db')
    cursor = conn.cursor()
    cursor.execute("select ivan from votes")
    ivan_db = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn = sqlite3.connect('votes.db')
    cursor = conn.cursor()
    cursor.execute("select farid from votes")
    farid_db = cursor.fetchall()
    conn.commit()
    cursor.close()
    far = str(farid_db).replace('[(', '').replace(')]', '').replace(',), (', ' ').replace(',','')
    iva = str(ivan_db).replace('[(','').replace(')]', '').replace(',), (', ' ').replace(',','')
    farid = far.split(' ')
    ivan = iva.split(' ')
    farid_votes = 0
    ivan_votes = 0
    for i in range(len(farid)):
        farid_votes += int(farid[i])
        ivan_votes += int(ivan[i])
    return ivan_votes, farid_votes

