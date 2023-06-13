import sqlite3

def setup_db():
    conn = sqlite3.connect('server_activity.db')
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS text_activity (
            id INTEGER PRIMARY KEY,
            user_id TEXT NOT NULL,
            text_channel_id TEXT NOT NULL,
            message_id TEXT NOT NULL,
            timestamp TEXT NOT NULL
        );
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS voice_activity (
            id INTEGER PRIMARY KEY,
            user_id TEXT NOT NULL,
            voice_channel_id TEXT NOT NULL,
            timestamp TEXT NOT NULL
        );
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    setup_db()
