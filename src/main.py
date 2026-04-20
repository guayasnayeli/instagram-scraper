from session.session_manager import create_session

def main():
    session = create_session()

    print("Sesión creada correctamente")
    print("Headers:", session.headers)

if __name__ == "__main__":
    main()