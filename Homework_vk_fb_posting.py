#Домашнее задание по курсу «Программист Python (уровень) #1», модуль 4
#Выполнил Богаевский Ростислав

#Для работы требуются модули vk_api и facebook
#Для отправления постов в Facebook, нужен ключ доступа (access token)

import vk_api, facebook

login = '' #добавить действительный логин VK
password = '' #добавить пароль VK
fb_token = '' #добавить access token для Facebook

message = input("What would you like to post? \n")
if len(message) > 140:
    print("Sorry, your post is too long")
else:
    try:
        vk_session = vk_api.VkApi(login, password)
        vk_session.auth()
        vk = vk_session.get_api()
        vk.wall.post(message=message)
        print("VK post made succesfully")
    except vk_api.exceptions.BadPassword:
        print("Sorry, something is wrong with VK login or password")
    except Exception:
        print("Sorry, something went wrong with VK")
    try:
        graph = facebook.GraphAPI(access_token = fb_token)
        graph.put_object('me', 'feed', message = message)
        print("Facebook post made successfully")
    except facebook.GraphAPIError:
        print("Sorry, error with app permission on Facebook")
    except Exception:
        print("Sorry, something went wrong with Facebook")
input("Press Enter to leave")
