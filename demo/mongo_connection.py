# from pymongo import MongoClient
#
# from demo import settings
#
# username = settings.MONGODB_DATABASES['default']['username']
# password = settings.MONGODB_DATABASES['default']['password']
# host = settings.MONGODB_DATABASES['default']['host']
#
# client = MongoClient(
#     host=host,
#     username=username,
#     password=password,
#     tz_aware=settings.MONGODB_DATABASES['default']['tz_aware']
#     )
#
# uri = f"mongodb://{username}:{password}@{host}?authSource=admin&retryWrites=true&w=majority"
# client = MongoClient(uri)
