# Задание №1 - Ближайший ноль

> Выполнено 10.12.2022 г.

## Описание задачи

Тимофей ищет место, чтобы построить себе дом. Улица, на которой он хочет жить, имеет длину n, то есть состоит из n одинаковых идущих подряд участков. Каждый участок либо пустой, либо на нём уже построен дом. 
Общительный Тимофей не хочет жить далеко от других людей на этой улице. Поэтому ему важно для каждого участка знать расстояние до ближайшего пустого участка. Если участок пустой, эта величина будет равна нулю — расстояние до самого себя.
Помогите Тимофею посчитать искомые расстояния. Для этого у вас есть карта улицы. Дома в городе Тимофея нумеровались в том порядке, в котором строились, поэтому их номера на карте никак не упорядочены. Пустые участки обозначены нулями.

## Описание решения

Решение основывается на двух последовательных частях, оформленных в функции __*nearest_zero(list)*__. 

Во время первой части мы находим через метод __*List.index(0)*__ позицию первого нуля, а затем запускаем проход по данному массиву. В результате прохода мы находим расстояние от фиксированного нуля (который меняется при каждом нахождении нового нуля) до чисел, заключенных между данным нулем и следующим. Однако у нас не будет учтено наименьшее расстояние от числа до следующего нуля.

Для этого, во второй части алгоритма, мы запускаем второй проход по массиву, но уже не прямой, а обратный, который работает по аналогии с первым проходом: мы находим индекс нуля (с прошлой части у нас уже есть индекс последнего нуля), фиксируем его, находим расстояния в промежутке между текущем нулем и следующим, однако мы заменяем не значение не просто на расстояние, а на минимум из нового расстояния и расстояния, полученного при прошлом обходе.

Тем самым мы получаем требуемый результат.

------

# Задание №2 - Ближайший ноль

> Выполнено 10.12.2022 г.

## Описание задачи

Игра «Тренажёр для скоростной печати» представляет собой поле из клавиш 4x4. В нём на каждом раунде появляется конфигурация цифр и точек. На клавише написана либо точка, либо цифра от 1 до 9. 
В момент времени $t$ игрок должен одновременно нажать на все клавиши, на которых написана цифра $t$. Гоша и Тимофей могут нажать в один момент времени на k клавиш каждый. Если в момент времени $t$ нажаты все нужные клавиши, то игроки получают 1 балл. Найдите число баллов, которое смогут заработать Гоша и Тимофей, если будут нажимать на клавиши вдвоём.

## Описание решения

Поскольку значения нашего поля - цифры от нуля до девяти (нет чисел, состоящих их двух цифр), для упрощения решения объединим входные строки в единую.

Пскольку каждый из ребят может нажать $k$ клавиш, то вместе они нажмут $2k$ клавиш. Отсюда получаем, что, чтобы получить очки, нужно, чтобы выполнялось соотношение при фиксированном $t$: $0 < m ≤ 2k$, где $m$ - количество кнопок c $t$. 

Благодаря циклу и методу __*list.count()*__ вычисляем количество баллов.

-------

![cat](https://d31iynjnzaofi5.cloudfront.net/blog/uploads/2018/11/giphy-12.gif)