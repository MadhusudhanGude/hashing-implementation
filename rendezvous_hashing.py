def custom_hash(key):
    x = 0
    for i in range(len(key)):
        ascii_code = ord(key[i])
        x = x + ascii_code
    return x

def compute_score(username, server):
    username_hash, server_hash = custom_hash(username), custom_hash(server)
    return (username_hash * 13 + server_hash * 8) % 67


def pick_server_simple_hashing(username, available_servers):
    hash = custom_hash(username)
    return available_servers[hash % len(available_servers)]


def pick_server_rendezvous_hashing(username, available_servers):
    max_score = 0
    max_server = None
    for each_server in available_servers:
        score = compute_score(username, each_server)
        if score > max_score:
            max_server = each_server
            max_score = score
    return max_server
  
server_set_one = [
    'server0',
    'server1',
    'server2',
    'server3',
    'server4',
    'server5'
]

server_set_two = [
    'server0',
    'server1',
    'server2',
    'server3',
    'server4'
]

usernames = [
    'username0',
    'username1',
    'username2',
    'username3',
    'username4',
    'username5',
    'username6',
    'username7',
    'username8'
]


# Simple Hashing Strategy
for username in usernames:
    server_one = pick_server_simple_hashing(username, server_set_one)
    server_two = pick_server_simple_hashing(username, server_set_two)
    print('Username {}: server one {} server two {} | equals  {}'.format(username, server_one, server_two, server_one==server_two))
    
    
# Rendezvous Hashing Strategy
for username in usernames:
    server_one = pick_server_rendezvous_hashing(username, server_set_one)
    server_two = pick_server_rendezvous_hashing(username, server_set_two)
    print('Username {}: server one {} server two {} | equals  {}'.format(username, server_one, server_two, server_one==server_two))
