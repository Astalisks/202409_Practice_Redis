# Redisとは
インメモリデータストア (Key-Value Store)
データがメモリ上に保持されるため読み書き速度が高い
キャッシュやセッション管理
→頻繁にアクセスされるデータ（APIレスポンス、ページ情報）をキャッシュ
リアルタイム分析、キューイングシステム（Pub/Subモデル）などに利用


# 01_コンテナ上でRedisを動作させる
docker-compose up -d

# 以下でRedisに入る
docker exec -it redis_container redis-cli
127.0.0.1:6379> PING
PONG

# データを入れる
127.0.0.1:6379> SET name "John"
OK
127.0.0.1:6379> SET name "Mike"
OK
127.0.0.1:6379> SET name "Taro"
OK

keyに対応する値は上書きされる
127.0.0.1:6379> GET name
"Taro"

# リストにデータを入れる
127.0.0.1:6379> LPUSH mylist "item1"
USH mylist "item2"
(integer) 1
127.0.0.1:6379> LRANGE mylist 0 -1
1) "item1"
127.0.0.1:6379> LPUSH mylist "item2"
(integer) 2
リストは先頭に追加される
127.0.0.1:6379> LRANGE mylist 0 -1
1) "item2"
2) "item1"

# ハッシュにデータを入れる
127.0.0.1:6379> HSET myhash field1 "value1"
(integer) 1
127.0.0.1:6379> HGET myhash field1
"value1"