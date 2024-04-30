import requests

def get_user_info(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        user_info = response.json()
        print(f"Nome: {user_info.get('name')}")
        print(f"Localização: {user_info.get('location')}")
        print(f"Bio: {user_info.get('bio')}")
        print(f"Seguidores: {user_info.get('followers')}")
    else:
        print(f"Erro: Não foi possível obter informações para o usuário {username}")

def get_user_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        repos = response.json()
        for repo in repos:
            print(f"Repositório: {repo['name']} - Estrelas: {repo['stargazers_count']}")
    else:
        print(f"Erro: Não foi possível obter repositórios para o usuário {username}")

def get_users_info(usernames):
    for username in usernames:
        print(f"\nInformações para o usuário {username}:")
        url = f"https://api.github.com/users/{username}/repos"
        response = requests.get(url)
        if response.status_code == 200:
            repos = response.json()
            print(f"Quantidade de repositórios: {len(repos)}")
            if repos:
                latest_repo = max(repos, key=lambda x: x['pushed_at'])
                print(f"Repositório mais recente: {latest_repo['name']}")
        else:
            print(f"Erro: Não foi possível obter informações para o usuário {username}")

username = input("Digite o nome de usuário do GitHub: ")
get_user_info(username)
get_user_repos(username)

usernames = input("Digite uma lista de nomes de usuários do GitHub separados por vírgula: ").split(', ')
get_users_info(usernames)
