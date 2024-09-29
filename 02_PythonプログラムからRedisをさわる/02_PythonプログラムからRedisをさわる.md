# Redisとは
インメモリデータストア (Key-Value Store)
データがメモリ上に保持されるため読み書き速度が高い
キャッシュやセッション管理
→頻繁にアクセスされるデータ（APIレスポンス、ページ情報）をキャッシュ
リアルタイム分析、キューイングシステム（Pub/Subモデル）などに利用


# 01_コンテナ上でRedisを動作させる
docker-compose up -d

# 以下でRedisに入る
Pythonプログラムで値が入ることを確認できる
docker logs <CONTAINER ID>
Name: John
List items:
item2
item1