import praw
import config
import time
import database


def bot_login():
    print("Производится вход в аккаунт...")
    r = praw.Reddit(username=config.username, password=config.password,
                    client_id=config.client_id, client_secret=config.client_secret,
                    user_agent="MosPolytech")
    print("Вход в аккаунт произведён")
    return r


def run_bot(r):
    cur = database.con.cursor()
    print("Происходит проверка 50 комментариев")
    for comment in r.subreddit('rusAskReddit').comments(limit=50):
        if (("университет" in comment.body.lower() or "уник" in comment.body.lower() or "вуз" in comment.body.lower())
                and comment.author != r.user.me() and len(cur.execute(
                f"SELECT comment_id FROM Comments WHERE comment_id = '{comment.id}'").fetchall()) == 0):
            print(f"Найден новый комментарий {comment.id}!")
            comment_reply = ("Дружище, не совершай ошибок, поступай в Московский Политехнический Университет!")
            comment.reply(comment_reply)
            print(f"Ответили на комментарий {comment.id}")
            cur.execute(
                f"INSERT INTO Comments (comment_id, body, author) VALUES (?, ?, ?)", (comment.id, comment.body, comment.author.name))
            database.con.commit()
            time.sleep(10)


if __name__ == '__main__':
    r = bot_login()
    while True:
        run_bot(r)
