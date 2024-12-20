Разработать инструмент командной строки для учебного конфигурационного
языка, синтаксис которого приведен далее. Этот инструмент преобразует текст из
входного формата в выходной. Синтаксические ошибки выявляются с выдачей
сообщений.
Входной текст на языке xml принимается из файла, путь к которому задан
ключом командной строки. Выходной текст на учебном конфигурационном
языке попадает в файл, путь к которому задан ключом командной строки.
Многострочные комментарии:
{{!--
Это многострочный
комментарий
--}}
Массивы:
({ значение, значение, значение, ... })
Имена:
[a-zA-Z]+
Значения:
• Числа.
• Строки
• Массивы.
Строки:
@"Это строка"
Объявление константы на этапе трансляции:
var имя = значение
Вычисление константы на этапе трансляции:
![имя]
Результатом вычисления константного выражения является значение.
Все конструкции учебного конфигурационного языка (с учетом их
возможной вложенности) должны быть покрыты тестами. Необходимо показать 3
примера описания конфигураций из разных предметных областей.

Реализация программы

Изначальный файл
![image](https://github.com/user-attachments/assets/a376c28b-3f93-4358-8e57-496a83cdd63d)
Итог
![image](https://github.com/user-attachments/assets/1079c98f-c9ad-4157-84dd-0437a41cfb5f)

Изначальный файл
![image](https://github.com/user-attachments/assets/e7e31db2-ce16-4359-a73d-0d192e1f63f6)
Итог
![image](https://github.com/user-attachments/assets/eec3f8b1-97b6-4af8-8f2f-403e96d7cda3)

Изначальный файл
![image](https://github.com/user-attachments/assets/1f46e981-1127-4e5a-a3e9-edacee2c443b)
Итог
![image](https://github.com/user-attachments/assets/73f73782-fe17-459c-94f1-0a27045937ae)



Тестирование Программы 
![image](https://github.com/user-attachments/assets/207bfb79-3905-476e-b239-6392611ad983)
