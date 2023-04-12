# CryptocurrencyAnalys
### Предисловие
В какой то момент я решил обзавестись пассивным доходом. Поискав информацию в интернете пришел к выводу что сейчас очень популярна тема криптовалют. Верить в чужие статьи я не хотел и по этому решил провести небольшой анализ. Нашел датасет с нужной мне информацией, а именно ценой и объемом торгов по четырем самым популярным криптовалютам, а именно BTC, ETH, USDT, BNB. Так как задача изначально заключалась именно в пасивном доходе, нужно было проверить способ добычи этих валют. Тогда я решил проанализировать целесообразность майнинга в наши дни.
### Начнем с Датасета 
Что ж, датасет найден, приступаем к его обработке. Для этого я использую Python и его различные библиотеки. 
С помощью библиотеки Pandas выведу первые 10 строк в датасете для демонстации его структуры. Так же с помошью настроек Pandas уберем ограничение на количество отображаемых столбцов и установим ширину отображения в 150 символов, что бы все красиво поместилось на экран.

<img src="https://github.com/smashok/CryptocurrencyAnalys/blob/main/Images/DataSet.png" style="width:450px;height:300px;">

### Общее представление 
Для начала выведем на общем графике цены на наши монеты. Сделаем это с помощью того же Pandas и Matplotlib. 

<img src="https://github.com/smashok/CryptocurrencyAnalys/blob/main/Images/4currencyPlot(code).png" style="width:350px;height:150px;">
В ходе работы выяснилось что столбец "дата" имел тип данных "строка". В шестой строчке исправляем это меняя тип данных на "datetime". 

В результате получаем график :

<img src="https://github.com/smashok/CryptocurrencyAnalys/blob/main/Images/4currencyPlot.png" style="width:500px;height:350px;">

Из графика можно увидеть, что в сентябре - октябре 2020 года произошел резкий скачок цен на криптовалюты. (Кроме USDT, поскольку этот токен перманентно равен доллару.)
На этом этапе мне стало интересно, как изменился спрос в связи с этим скачком цен. Я решил создать такой же график и для volume:

<img src="https://github.com/smashok/CryptocurrencyAnalys/blob/main/Images/VolumesPlot.png" style="width:500px;height:350px;"> <img src="https://github.com/smashok/CryptocurrencyAnalys/blob/main/Images/VolumesPlot(Code).png" style="width:350px;height:200px;">

На графике мы можем увидеть, что рост цены на криптовалюты потянул за собой рост спроса на USDT. Так как он привязан к доллару и является стейблкоином, я предполагаю что игроки на рынке переводят свои прибыли именно в USDT, для избежания потерь в случае если остальные активы упадут в цене.
Что ж, информация занятная, но перейдем к практической части.

### То, ради чего все это затевалось
И так, майнинг. Для начала нужно очертить определенные требования к тому, что действительно нам нужно. Я решил, что неплохо было бы, если ферма окупит себя как можно быстрее. Для этого нужно начать майнить в тот промежуток времени когда цена на добываемый актив будет расти. Пришло время поискать интересные закономерности в ценах.

Для каждой валюты я буду выводить графики за определенный год, кусочек кода будет один (ибо меняются только входные данные), а графиков будет несколько.

Начнем с BTC:

С помощью Pandas и Matplotlib построим отдельные графики за каждый год. Для этого отфильруем датафрейм по определенному году :

<img src="https://github.com/smashok/CryptocurrencyAnalys/blob/main/Images/BTC2018(Code).png" style="width:500px;height:350px;">

Что ж, в итоге получаем графики за 2018-2022 года:

<img src="https://github.com/smashok/CryptocurrencyAnalys/blob/main/Images/BTC2018(Price).png" style="width:300px;height:200px;"> <img src="https://github.com/smashok/CryptocurrencyAnalys/blob/main/Images/BTC2019(Price).png" style="width:300px;height:200px;">
<img src="https://github.com/smashok/CryptocurrencyAnalys/blob/main/Images/BTC2020(Price).png" style="width:300px;height:200px;"> <img src="https://github.com/smashok/CryptocurrencyAnalys/blob/main/Images/BTC2021(Price).png" style="width:300px;height:200px;">
<img src="https://github.com/smashok/CryptocurrencyAnalys/blob/main/Images/BTC2022(Price).png" style="width:300px;height:200px;">
 
По графикам видно, что все года, за исключением 2019, в летний период цена либо перестает расти, либо проседает. Из этого можно сделать инсайт что летом интерес к рынку падает и следовательно падает цена. 

Проверим наше предположение, создав графики спроса :

<img src="https://github.com/smashok/CryptocurrencyAnalys/blob/main/Images/BTC2018(Volume).png" style="width:300px;height:200px;"> <img src="https://github.com/smashok/CryptocurrencyAnalys/blob/main/Images/BTC2019(Volume).png" style="width:300px;height:200px;">
<img src="https://github.com/smashok/CryptocurrencyAnalys/blob/main/Images/BTC2020(Volume).png" style="width:300px;height:200px;"> <img src="https://github.com/smashok/CryptocurrencyAnalys/blob/main/Images/BTC2021(Volume).png" style="width:300px;height:200px;">
<img src="https://github.com/smashok/CryptocurrencyAnalys/blob/main/Images/BTC2022(Volume).png" style="width:300px;height:200px;">

Что ж, графики спроса подтверждают просадку метрики "Volume". Но что же произошло в 2019 году ? Судя по графику цен, в июне 2019 биткоин пробил отметку в 10000$, что могло послужить неким психологическим триггером для того что бы люди заинтерисовались криптовалютой. После поисков в интернете мне так же удалось найти заявления различных крупных игроков на рынке о том что биткоин легко преодолеет отметку в 100к $. Возможно это и подогрело интерес аудитории. Затем в августе 2019 года крупнейшая биржа Binance объявила о том, что она будет запрещать доступ к своей платформе для пользователей из США. На графике четко видно последствия этих заявлений (просадка в цене).
Мы выяснили что 2019 год - аномальный и скорее является искючением из общей закономерности. По этому полагаться на него не будем.

### Другие валюты
Биткоин я проанализировал для наглядности, теперь я хочу найти ту валюту, доход с которой будет самым высоким. USDT сразу отбрасываем, так как это стейблкоин. BNB так же не подходит ибо согласно информации с сайта Binance, их монеты можно получить только в ходе операций на бирже, майнингу они не подлежат. Остался ETH, его то мы и сравним с BTC.

Для начала нужно узнать что происходило с ETH за этот же промежуток времени (не думаю что будут существенные отличия, но все же вдруг обнаружатся какие то интересные аномалии).

Графики цены :

<img src="https://github.com/smashok/CryptocurrencyAnalys/blob/main/Images/ETH2018(Price).png" style="width:300px;height:200px;"> <img src="https://github.com/smashok/CryptocurrencyAnalys/blob/main/Images/ETH2019(Price).png" style="width:300px;height:200px;">
<img src="https://github.com/smashok/CryptocurrencyAnalys/blob/main/Images/ETH2020(Price).png" style="width:300px;height:200px;"> <img src="https://github.com/smashok/CryptocurrencyAnalys/blob/main/Images/ETH2021(Price).png" style="width:300px;height:200px;">
<img src="https://github.com/smashok/CryptocurrencyAnalys/blob/main/Images/ETH2022(Price).png" style="width:300px;height:200px;">

Графики Volume :

<img src="https://github.com/smashok/CryptocurrencyAnalys/blob/main/Images/ETH2018(Volume).png" style="width:300px;height:200px;"> <img src="https://github.com/smashok/CryptocurrencyAnalys/blob/main/Images/ETH2019(Volume).png" style="width:300px;height:200px;">
<img src="https://github.com/smashok/CryptocurrencyAnalys/blob/main/Images/ETH2020(Volume).png" style="width:300px;height:200px;"> <img src="https://github.com/smashok/CryptocurrencyAnalys/blob/main/Images/ETH2021(Volume).png" style="width:300px;height:200px;">
<img src="https://github.com/smashok/CryptocurrencyAnalys/blob/main/Images/ETH2022(Volume).png" style="width:300px;height:200px;">

Как я и предполагал, отличий не много. Это наталкивает на мысль что монеты зависят друг от друга. Нужно это проверить.

### Корреляция 
Построим тепловую карту корреляций. Для этого нам понадобятся такие библиотеки как Pandas, Matplotlib и Seaborn.

<img src="https://github.com/smashok/CryptocurrencyAnalys/blob/main/Images/Corr(code).png" style="width:300px;height:300px;"> <img src="https://github.com/smashok/CryptocurrencyAnalys/blob/main/Images/Corr.png" style="width:500px;height:500px;">

Из карты корреляций видно что коэффициент кореляции цены биткоина и эфира - 0.92. Это достаточно много. Это подтверждает нашу гипотезу о том что эти две валюты зависят друг от друга(если цена на одну из валют растет, то вторая так же растет в цене).

Так же на этой карте можно увидеть что метрики USDT имеют отрицательную корреляцию со всеми остальными метриками. Это обусловленно тем что его цена привязанна к доллару и если допустить что цена USDT будет идти вниз, то следовательно цена других валют, пусть и не сильно(коэффициенты не сильно низкие), но будет возрастать. Это достаточно полезная информация, но она больше понадобится при торгах на бирже для прогнозирования цен, нас же интересует майнинг.

### Майнинг ферма
Так как я не разбираюсь в майнинге, создание фермы я решил доверить новому интсрументу, а именно нейросети GPT. Мой бюджет составляет 5000$ и для начала попросим GPT построить ферму для добычи биткоина:

<img src="https://github.com/smashok/CryptocurrencyAnalys/blob/main/Images/Farm(BTC).png" style="width:150px;height:300px;">

Теперь нужно посчитать доход с этой фермы. Для этого использую онлайн калькулятор "nicehash".

<img src="https://github.com/smashok/CryptocurrencyAnalys/blob/main/Images/Profit(BTC).png" style="width:400px;height:600px;">

Вносим в калькулятор 7 предложенных нейросетью видеокарт (именно столько получиться приобрести поместившись в 5000 долларов) и цену электроенергии за 1 кВт/ч в Киеве. Итого видим что чистая прибыль в день составляет 2.65$, а в месяц 92.86$. При таком раскладе для окупаемости фермы нужно 53 месяца. Результат печален. Но это было не последнее разочарование. Покопавшись в интернете я нашел информацию о том что ETH больше не добывается. Следовательно можно сделать выводы.

### Выводы 
В итоге в ходе исследований мы пришли к выводу что майнинг в 2023 году существенно потерял популярнось и заниматься им нецелесообразно. Но инстайты,  которые удалось найти в ходе анализа цен и спроса на различные валюты, могут пригодиться в трейдинге и в целом просто занимательные. 

#### Послесловие 
Целью данного проекта была демонстация работы с Python и его библиотеками для анализа данных, а так же демонстрация моего хода мысли. Надеюсь это было интересно читать :) Все выводы и советы в этом проекте - не являються финансовой рекомендацией, руководством к действию и не претендуют на истину в последней инстанции. Спасибо за внимание!)



