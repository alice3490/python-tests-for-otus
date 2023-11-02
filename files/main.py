import json
import csv


def get_books_from_csv_file(file_csv: str):
    books_keys = ["Title", "Author", "Pages", "Genre"]
    with open(file_csv, "r") as file_books:
        books = csv.DictReader(file_books)
        books_list = []
        for book in books:
            result = {key: value for key, value in book.items() if key in books_keys}
            books_list.append(result)
    return books_list


def get_users_from_json_file(file_name: str):
    users_keys = ["name", "gender", "age", "address"]
    with open(file_name, "r") as json_file:
        users = json.load(json_file)
        users_list = []
    for user in users:
        data = {key: value for key, value in user.items() if key in users_keys}
        data = {key: data.pop(key) for key in users_keys}
        users_list.append(data)
    return users_list


def give_books_to_users(books_list, users_list):
    result_list = []
    books_per_user = len(books_list) // len(users_list)
    remaining_books = len(books_list) % len(users_list)

    for i, user in enumerate(users_list):
        user_books = books_list[i * books_per_user: (i + 1) * books_per_user]

        if i < remaining_books:
            user_books.append(books_list[len(users_list) * books_per_user + i])

        user["books"] = user_books
        result_list.append(user)

    return result_list


def json_to_file(result_list):
    with open("result.json", "w") as file:
        json.dump(result_list, file, indent=4)
        file.write("\n")


def main():
    json_file_name = "users.json"
    csv_file_name = "books.csv"

    books_processed = get_books_from_csv_file(csv_file_name)
    users_processed = get_users_from_json_file(json_file_name)

    result = give_books_to_users(books_processed, users_processed)
    json_to_file(result)


if __name__ == "__main__":
    main()
