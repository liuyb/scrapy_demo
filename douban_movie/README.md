## [豆瓣电影top250](http://movie.douban.com/top250)

### 实现功能

* 抓取电影的排行，标题，打分等信息保存到MySQL数据库
* 保存电影封面图片到本地

### 使用

下载代码并安装依赖

```bash
$ git clone https://github.com/crazygit/scrapy_demo.git
$ cd scrapy_demo/douban_movie/
$ pip install -r requirements.txt
```

创建本地数据库

```sql
mysql> create database douban;
mysql> use douban
mysql> source db/movies_schema.sql
mysql> show tables;
+------------------+
| Tables_in_douban |
+------------------+
| top250           |
+------------------+
1 row in set (0.00 sec)

mysql> desc top250;
+------------+--------------+------+-----+---------+----------------+
| Field      | Type         | Null | Key | Default | Extra          |
+------------+--------------+------+-----+---------+----------------+
| id         | int(11)      | NO   | PRI | NULL    | auto_increment |
| rank       | int(11)      | NO   |     | NULL    |                |
| picture    | varchar(250) | NO   |     | NULL    |                |
| title      | varchar(250) | NO   |     | NULL    |                |
| info       | varchar(250) | NO   |     | NULL    |                |
| star       | decimal(4,1) | YES  |     | NULL    |                |
| quote      | varchar(250) | NO   |     | NULL    |                |
| crawl_time | datetime     | NO   |     | NULL    |                |
| people     | int(11)      | NO   |     | NULL    |                |
+------------+--------------+------+-----+---------+----------------+
9 rows in set (0.14 sec)
```

编辑项目配置信息, 修改`douban_movie/douban_movie/settings.py`里的数据库信息`DB_ARGS`和图片保存路径`IMAGES_STORE`

```python
DB_ARGS = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': 'linliang',
    'db': 'movies',
    'charset': 'utf8',
    'use_unicode': True,
}

IMAGES_STORE = '/tmp/douban/images'
```

### 运行

```bash
$ cd scrapy_demo/douban_movie
$ python main.py
```


### 结果展示

```sql
mysql> select * from top250 order by rank limit 10;
+----+------+----------------------------------------------------------------------------+-----------------------+-------------------------------------------------------------------------------------------------+------+---------------------------------------------------------------------------+---------------------+--------+
| id | rank | picture                                                                    | title                 | info                                                                                            | star | quote                                                                     | crawl_time          | people |
+----+------+----------------------------------------------------------------------------+-----------------------+-------------------------------------------------------------------------------------------------+------+---------------------------------------------------------------------------+---------------------+--------+
|  3 |    1 | http://img3.douban.com/view/movie_poster_cover/ipst/public/p480747492.jpg  | 肖申克的救赎          | 导演: 弗兰克·德拉邦特 Frank Darabont   主演: 蒂姆·罗宾斯 Tim Robbins /...                       |  9.6 | 希望让人自由。                                                            | 2015-10-29 11:59:01 | 647786 |
|  2 |    2 | http://img3.douban.com/view/movie_poster_cover/ipst/public/p511118051.jpg  | 这个杀手不太冷        | 导演: 吕克·贝松 Luc Besson   主演: 让·雷诺 Jean Reno / 娜塔丽·波特曼 ...                        |  9.4 | 怪蜀黍和小萝莉不得不说的故事。                                            | 2015-10-29 11:59:01 | 616931 |
|  1 |    3 | http://img4.douban.com/view/movie_poster_cover/ipst/public/p510876377.jpg  | 阿甘正传              | 导演: Robert Zemeckis   主演: Tom Hanks / Robin Wright Penn / Gary Sinise                       |  9.4 | 一部美国近现代史。                                                        | 2015-10-29 11:59:01 | 544114 |
|  4 |    4 | http://img3.douban.com/view/movie_poster_cover/ipst/public/p1910813120.jpg | 霸王别姬              | 导演: 陈凯歌 Kaige Chen   主演: 张国荣 Leslie Cheung / 张丰毅 Fengyi Zha...                     |  9.4 | 风华绝代。                                                                | 2015-10-29 11:59:01 | 445125 |
|  5 |    5 | http://img3.douban.com/view/movie_poster_cover/ipst/public/p510861873.jpg  | 美丽人生              | 导演: 罗伯托·贝尼尼 Roberto Benigni   主演: 罗伯托·贝尼尼 Roberto Beni...                       |  9.5 | 最美的谎言。                                                              | 2015-10-29 11:59:01 | 301136 |
|  6 |    6 | http://img4.douban.com/view/movie_poster_cover/ipst/public/p511146957.jpg  | 海上钢琴师            | 导演: 朱塞佩·托纳多雷 Giuseppe Tornatore   主演: 蒂姆·罗斯 Tim Roth / ...                       |  9.2 | 每个人都要走一条自己坚定了的路，就算是粉身碎骨。                          | 2015-10-29 11:59:01 | 474256 |
|  7 |    7 | http://img3.douban.com/view/movie_poster_cover/ipst/public/p492406163.jpg  | 辛德勒的名单          | 导演: 史蒂文·斯皮尔伯格 Steven Spielberg   主演: 连姆·尼森 Liam Neeson...                       |  9.4 | 拯救一个人，就是拯救整个世界。                                            | 2015-10-29 11:59:01 | 286737 |
|  8 |    8 | http://img4.douban.com/view/movie_poster_cover/ipst/public/p1910830216.jpg | 千与千寻              | 导演: 宫崎骏 Hayao Miyazaki   主演: 柊瑠美 Rumi Hîragi / 入野自由 Miy...                        |  9.2 | 最好的宫崎骏，最好的久石让。                                              | 2015-10-29 11:59:01 | 491132 |
|  9 |    9 | http://img3.douban.com/view/movie_poster_cover/ipst/public/p449665982.jpg  | 机器人总动员          | 导演: 安德鲁·斯坦顿 Andrew Stanton   主演: 本·贝尔特 Ben Burtt / 艾丽...                        |  9.3 | 小瓦力，大人生。                                                          | 2015-10-29 11:59:01 | 396790 |
| 10 |   10 | http://img3.douban.com/view/movie_poster_cover/ipst/public/p457760035.jpg  | 泰坦尼克号            | 导演: James Cameron   主演: Leonardo DiCaprio / Kate Winslet / Billy Zane                       |  9.1 | 失去的才是永恒的。                                                        | 2015-10-29 11:59:01 | 503397 |
+----+------+----------------------------------------------------------------------------+-----------------------+-------------------------------------------------------------------------------------------------+------+---------------------------------------------------------------------------+---------------------+--------+
```

```bash
$ ls /tmp/douban/images/full/
00eebe95ff0798ca7b5e7ba5d505f08b0ada20cc.jpg
01d49f7b8232c299f86222de888227e677cc9831.jpg
02d8ebaa2a27717c50bfeec08dd422422867d5a7.jpg
031695131e938ff06c6682aff0e1188c3df15a01.jpg
040a4f83b9ac60912be7b3d91fc0b2b05ae257ee.jpg
05155dc1dddf30ad26225807d14a02f564e2c497.jpg
0526e4bb015fb64e2335790195abd699f1ebb165.jpg
0542781ed51202db0195e73980b0c7173d4926ff.jpg
07520d2afcca25a48bb3ec6a78617f692c17df55.jpg
08627907d82ab5a379bd8e8d5ee0f49f35ad3285.jpg
09560a68e86d6b020d86647ac7d435fada91a28a.jpg
0b0507fda7fe375c533233b3a6379ac0d287951f.jpg
0c2dbbd2b0612fcc9a41fc8680e662ccd94e6a3a.jpg
0c4d8a558ff17f3c6767c172f580f09541683a58.jpg
0ddcbae4a9aa587ea0e748449287bf9cc3b944cc.jpg
0e10abd518187aa3f797fc79d147a1bdaccec459.jpg
0ff47dadaddfafb6c9fcaf1ab387bcc056dc5178.jpg
11619f1bb00c7effe5c9cae4f1e383696da5636d.jpg
118f241e9935902c56cf2d09521d878f1270f1f8.jpg
12fff3bc872917530c7fb42a79b1491f0bd8a186.jpg
131bb684e32b2ff18119f2275794501b2f7edfcc.jpg
14003808b106d90e895dca2b3cc086f44086d650.jpg
15165cd8b541f198cc74a6158ebde392f0d44e63.jpg
161ea64387db426fdd82c750ecb3cae1f00821dc.jpg
166396e41c1d2790d435f0855b6ec17c11ea5230.jpg
17f6d746fed0892b0cdff23af7da1d854e308f13.jpg
```

### 封面效果图

![效果图](http://7xkp7e.com1.z0.glb.clouddn.com/crazygit/douban_movies.png "效果图")

