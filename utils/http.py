from fastmcp import Context


def get_bearer_token(ctx: Context):
    request = ctx.get_http_request()
    headers = request.headers

    # Check if 'Authorization' header is present
    authorization_header = headers.get("X_User_Token")

    if authorization_header:
        # Split the header into 'Bearer <token>'
        parts = authorization_header.split()

        if len(parts) == 2 and parts[0] == "Bearer":
            return parts[1]
        else:
            raise ValueError("Invalid Authorization header format")
    else:
        raise ValueError("Authorization header missing")
