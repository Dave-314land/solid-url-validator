"""
Build a basic URL Validator.
Returns a list of responses.
Basic GET and POSTS requests validated.
If GET request contains valid token, return VALID and user name.
If GET request does not contain valid token, return INVALID
If POST request contains valid token and contains valid CSRF token, return VALID and user name.
"""

from urllib.parse import urlparse, parse_qs


def getResponses(valid_auth_tokens, requests):
    responses = []
    for request in requests:

        if request[0] == "GET":
            parsed_result = urlparse(request[1])
            parsed_url_params = parse_qs(parsed_result.query)
            token_value = parsed_url_params['token'][0]
            name_value = parsed_url_params['name'][0]
            
            if token_value in valid_auth_tokens:
                response = [f"VALID, name: {name_value}"]
                responses.append(response)
            else:
                response = ["INVALID"]
                responses.append(response)

        elif request[0] == "POST":
            pass

        else:
            pass

    return responses


if __name__ == "__main__":

    valid_auth_tokens = ["ah37j2ha483u", "safh34ywb0p5"]
    
    requests = [
        ["GET","https://example.com/?token=347sd6yk8iu2&name=alex"],
        ["GET","https://example.com/?token=safh34ywb0p5&name=sam"],
        ["POST","https://example.com/?token=safh34ywb0p5&name=alex"],
        ["POST","https://example.com/?token=safh34ywb0p5&csrf=ak2sh32dy&name=chris"]
    ]
    
    print(getResponses(valid_auth_tokens, requests))
