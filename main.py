import requests

import tokens


def send(query_body):
    url = 'https://api.github.com/graphql'
    headers = {'Authorization': 'bearer ' + tokens.token}
    body = {'query': query_body}

    result = requests.post(url=url, json=body, headers=headers)
    return result


def main():
    query_body = """
                query {
                    viewer {
                        login
                    }
                }
                """
    result = send(query_body)
    print(result.json)


if __name__ == "__main__":
    main()
