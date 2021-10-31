import requests
import os
import json
import mysql.connector

from dotenv import load_dotenv

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
load_dotenv()
bearer_token = os.environ.get("TWITTER_BEARER_TOKEN")

db_host = os.environ.get("DB_HOST")
db_database = os.environ.get("DB_DATABASE")
db_user = os.environ.get("DB_USERNAME")
db_pass = os.environ.get("DB_PASSWORD")

db_connection = mysql.connector.connect(host=db_host, user=db_user, password=db_pass, database=db_database)

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2FilteredStreamPython"
    return r


def get_rules():
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream/rules", auth=bearer_oauth
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot get rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))
    return response.json()


def delete_all_rules(rules):
    if rules is None or "data" not in rules:
        return None

    ids = list(map(lambda rule: rule["id"], rules["data"]))
    payload = {"delete": {"ids": ids}}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        auth=bearer_oauth,
        json=payload
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot delete rules (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    print(json.dumps(response.json()))


def set_rules(delete):
    # You can adjust the rules if needed
    rules = [
        {"value": "#resbakuna (-is:retweet) (lang:en OR lang:tl)"},
        {"value": "#bidabakunation (-is:retweet) (lang:en OR lang:tl)"},
        {"value": "#pfizer (-is:retweet) (lang:en OR lang:tl)"},
        {"value": "#pfizerbiontech (-is:retweet) (lang:en OR lang:tl)"},
        {"value": "#sinovac (-is:retweet) (lang:en OR lang:tl)"},
        {"value": "#astrazeneca (-is:retweet) (lang:en OR lang:tl)"},
        {"value": "#moderna (-is:retweet) (lang:en OR lang:tl)"},
        {"value": "#sinopharm (-is:retweet) (lang:en OR lang:tl)"},
        {"value": "#sputnikv (-is:retweet) (lang:en OR lang:tl)"},
        {"value": "#janssen (-is:retweet) (lang:en OR lang:tl)"}
    ]
    payload = {"add": rules}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        auth=bearer_oauth,
        json=payload,
    )
    if response.status_code != 201:
        raise Exception(
            "Cannot add rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))


def get_stream(set):
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream", auth=bearer_oauth, stream=True,
    )
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Cannot get stream (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    for response_line in response.iter_lines():
        if response_line:
            json_response = json.loads(response_line)

            tweet_id = response_line["data"]["id"]
            tweet_text = response_line["data"]["text"]

            db_cursor = db_connection.cursor()

            sql = "INSERT INTO tweets (tweet_id, text) VALUES ($d, $s)"
            value = (tweet_id, tweet_text)

            db_cursor.execute()
            db_connection()

            print(json.dumps(json_response, indent=4, sort_keys=True))


def main():
    rules = get_rules()
    delete = delete_all_rules(rules)
    set = set_rules(delete)
    get_stream(set)


if __name__ == "__main__":
    main()