from random import randint

 	
answers = ['Бесспорно.', 'Мне кажется - да.', 'Пока неясно.', 'Попробуй снова.', 
           'Даже не думай !', 'Предрешено.', 'Вероятнее всего.', 'Спроси позже.', 
           'Мой ответ - нет.', 'Никаких сомнений.', 'Хорошие перспективы.', 
           'Лучше не рассказывать.', 'По моим данным - нет.', 'Определённо да.',
           'Знаки говорят - да.', 'Сейчас нельзя предсказать.', 'Перспективы не очень хорошие.', 
           'Можешь быть уверен в этом', 'Да.', 'Сконцентрируйся и спроси опять.', 
           'Весьма сомнительно.']
        
def magic_ball():
    s = input('Твой вопрос: ')
    print(answers[randint(0, 19)])


print('Привет Мир, я магический шар, и я знаю ответ на любой вопрос.')		
name = input('Как тебя зовут?: ')	
print('Привет,', name)
while True:
    magic_ball()
    yes_no = input('Ты хочешь задать вопрос еще раз? ["+" - да, "-" - нет]: ')
    if yes_no == '+':
        continue
    elif yes_no == '-':
        print('Возвращайся если возникнут вопросы!')
        break
    


