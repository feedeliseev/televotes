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
3