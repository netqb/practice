import requests
from bs4 import BeautifulSoup

# Функция для поиска вопросов
def search_questions(keyword, pages=5):
    base_url = "https://stackoverflow.com/questions"
    results = []

    for page in range(1, pages + 1):
        url = f"{base_url}?page={page}&sort=newest&pagesize=15"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Находим все вопросы
        questions = soup.find_all('a', class_='s-link')
        for question in questions:
            title = question.text.strip()
            link = f"https://stackoverflow.com{question['href']}"
            if keyword.lower() in title.lower():
                results.append((title, link))

    return results

# Ввод ключевого слова от пользователя
keyword = input("Введите слово для поиска: ")

# Поиск вопросов
questions = search_questions(keyword, pages=5)

# Вывод результатов
print(f"Результаты поиска по слову: {keyword}")
for i, (title, link) in enumerate(questions, start=1):
    print(f"{i}. {title}\n{link}")
