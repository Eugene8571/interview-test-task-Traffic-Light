
Видеодемонстрация:

https://user-images.githubusercontent.com/40310109/111535046-56aa7d00-8771-11eb-990f-ff70b3bb4bd2.mp4


для запуска локально, из папки репозитария выполнить:
~~~~bash
env\Scripts\activate
cd employee_tree
pip install -r requirements.txt
python manage.py runserver
~~~~

admin usrname: user, password: 0

Наполнение базы данных происходит по команде
~~~~bash
python manage.py generate_emps
~~~~

если понадобится сгенерировать департаменты
~~~~bash
python manage.py generate_departments
~~~~
