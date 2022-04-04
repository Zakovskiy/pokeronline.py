from pokeronline import pokeronline

Poker = durakonline.Client("access_token")

@Poker.event(command="user_msg")
def event(data):
    try:
        user_id = data["from"]
    except:
        user_id = Poker.uid
    to = data["from"] if data["to"] == Poker.uid else data["to"]
    user_name = data["name"]
    Poker.friend.send_message(f">>{user_name}, hello!", to)
