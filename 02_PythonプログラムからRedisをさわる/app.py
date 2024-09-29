import redis

# Redisに接続
client = redis.Redis(host='redis', port=6379, db=0)

# データのセット
client.set('name', 'John')

# データの取得
name = client.get('name')
print(f"Name: {name.decode('utf-8')}")

# リストに値を追加
client.lpush('mylist', 'item1')
client.lpush('mylist', 'item2')

# リストの値を取得
mylist = client.lrange('mylist', 0, -1)
print("List items:")
for item in mylist:
    print(item.decode('utf-8'))
