# ReactPy requires a multiprocessing-safe and thread-safe cache.
REACTPY_CACHE = "default"

# ReactPy requires a multiprocessing-safe and thread-safe database.
REACTPY_DATABASE = "default"

# Maximum seconds between reconnection attempts before giving up.
# Use `0` to prevent component reconnection.
REACTPY_RECONNECT_MAX = 259200

# The URL for ReactPy to serve the component rendering websocket
REACTPY_WEBSOCKET_URL = "reactpy/"

# Dotted path to the default `reactpy_django.hooks.use_query` postprocessor function, or `None`
REACTPY_DEFAULT_QUERY_POSTPROCESSOR = "reactpy_django.utils.django_query_postprocessor"

# Dotted path to the Django authentication backend to use for ReactPy components
# This is only needed if:
#   1. You are using `AuthMiddlewareStack` and...
#   2. You are using Django's `AUTHENTICATION_BACKENDS` settings and...
#   3. Your Django user model does not define a `backend` attribute
REACTPY_AUTH_BACKEND = None