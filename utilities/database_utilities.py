import sqlite3 as lite


def create_database(database_path: str):
    # Create the database connection
    conn = lite.connect(database_path)
    # With the connection, we want to do the following
    with conn:
        # Create a cursor
        cur = conn.cursor()
        # We will execute a command to drop the table
        # if the word already exists
        cur.execute("drop table if exists words")
        # Set the ddl to the one we copied from the table
        # Split it up so that we can make it PEP8 compliant
        ddl = "create table words (word text not null constraint words_pk primary key,\
              usage_count int default 1 not null);"
        cur.execute(ddl)
        ddl = "create unique index words_word_uindex on words(word)"
        cur.execute(ddl)


def save_words_to_database(database_path: str, word_list: list):
    conn = lite.connect(database_path)
    with conn:
        cur = conn.cursor()
        for word in word_list:
            # Check to see if the word is in the database
            # We first need to get the count
            sql = "select count(word) from words where word = '" + word + "'"
            cur.execute(sql)
            count = cur.fetchone()[0]
            # If the word exists, we update the count
            if count > 0:
                sql = "update words set usage_count = usage_count + 1 where word = '" + word + "'"
            # If it doesn't exist, we add it to the database
            else:
                sql = "insert into words(word) values('" + word + "')"
            cur.execute(sql)
        print("Database operation is complete!")
