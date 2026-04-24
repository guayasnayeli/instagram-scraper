from session.session_manager import create_session
from config.settings import TARGET_USER, LIMIT
from scraper.user_scraper import extract_user_data
from scraper.relationships_scraper import extract_users
from export.exporter import export_to_csv
from scraper.post_scraper import extract_posts
from scraper.comments_scraper import extract_comments
from analysis.post_analysis import analyze
from analysis.report import generate_report
import os

def get_user_input(default_user, default_limit):
    user = input(f"Usuario (Enter={default_user}): ").strip() or default_user

    option = input("1=followers, 2=following, 3=ambos: ").strip()

    limit_input = input(f"Cantidad (Enter={default_limit} o 'all'): ").strip()
    
    deep_input = input("Modo avanzado (y/n): ").strip().lower()
    deep = deep_input == "y"
    limit = int(input("Cantidad usuarios: ") or default_limit)
    post_limit = int(input("Cantidad de posts: ") or 5)
    comment_limit = int(input("Comentarios por post: ") or 3)
    
    if not limit_input:
        limit = default_limit
    elif limit_input.lower() == "all":
        limit = None
    else:
        try:
            limit = int(limit_input)
        except:
            print("Valor inválido, usando default.")
            limit = default_limit

    

    return user, option, limit, deep, post_limit, comment_limit


def main():
    session = create_session()

    # 🔥 INPUT DINÁMICO
    user, option, limit, deep, post_limit, comment_limit = get_user_input(TARGET_USER, LIMIT)

    # 🔹 Obtener info del usuario
    url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={user}"
    response = session.get(url)

    if response.status_code != 200:
        print(f"Error al obtener usuario: {response.status_code}")
        return

    data = response.json()
    user_data = extract_user_data(data)

    print("\n=== USER DATA ===")
    for key, value in user_data.items():
        print(f"{key}: {value}")

    # 🔹 Obtener user_id
    user_id = user_data.get("id")

    if not user_id:
        print("No se pudo obtener el user_id")
        return
    
    posts = extract_posts(session, user_id, limit=post_limit)

    all_comments = []
    for p in posts:
        all_comments.extend(
        extract_comments(session, p["post_id"], limit=comment_limit)
    )
    #ANÁLISIS
    followers_count = user_data.get("followers", 0)

    metrics = analyze(posts, followers_count)

    report = generate_report(metrics, followers_count)

    print(report)
    #GUARDAR
    os.makedirs("outputs", exist_ok=True)

    with open("outputs/analysis.txt", "w", encoding="utf-8") as f:
        f.write(report)
    # 🔥 LÓGICA SEGÚN OPCIÓN

    if option == "1":
        print("\n=== FOLLOWERS ===")
        users = extract_users(session, user_id, mode="followers", limit=limit, deep=deep)

        for u in users:
            print(u)

        export_to_csv(users,"followers")

    elif option == "2":
        print("\n=== FOLLOWING ===")
        users = extract_users(session, user_id, mode="following", limit=limit, deep=deep)

        for u in users:
            print(u)
        
        export_to_csv(users,"following")

    elif option == "3":
        print("\n=== FOLLOWERS ===")
        followers = extract_users(session, user_id, mode="followers", limit=limit, deep=deep)

        for f in followers:
            print(f)

        export_to_csv(followers,"followers")

        print("\n=== FOLLOWING ===")
        following = extract_users(session, user_id, mode="following", limit=limit, deep=deep)

        for f in following:
            print(f)

        export_to_csv(following,"following")

    else:
        print("Opción inválida")

if __name__ == "__main__":
    main()
  