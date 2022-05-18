

**собрать образ докера для бота**

 docker build -f volumes/build/bot/Dockerfile  -t bot . 

**пересобрать бота**

docker-compose up -d --no-deps --build bot


**цель**

только друзья могу подключиться к моей vpn  сети 
для подключения они получают готовый конфиг для wireguard

**нужно сделать**

верефикация пользователей (по телефону, соц сетям, по токену, просто запросить доступ)
права доступа (admin, user)
служба поддержки (на django взять какой-нибудь фреймворк для python, если django  не потянет фронт, то сделать на vue 
и fast api)

**структура каталогов проекта**
- data - данные postgresql
- src  - код бота
  - 
  - 
volumes - конфиги и dockerfile для python, nginx и postgres




