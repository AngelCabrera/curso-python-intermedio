def run():
    users = [
        {
            "id": 1,
            "name": "Angel",
            "delinquent": False,
        },
        {
            "id": 2,
            "name": "Jose",
            "delinquent": True,
        },
        {
            "id": 3,
            "name": "Juan",
            "delinquent": True,
        },
        {
            "id": 5,
            "name": "Juaan",
            "delinquent": False,
        },
        {
            "id": 6,
            "name": "Jorge",
            "delinquent": True,
        }
    ]


    squares = [user for user in users if user["delinquent"]]
    
    print(squares)

if __name__ == '__main__':
    run()