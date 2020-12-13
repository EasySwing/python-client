from api_wrapper import APIWrapper
from config import Config

api = APIWrapper(Config)
tag_uuid = '2b2f48c2-74e6-4d6b-98c1-111630bfa7ae'
user = api.sign_in(tag_uuid)

print(user.get('first_name'))
print(user.get('last_name'))
for club in user.get('clubs'):
    print(f'{club.get("name")} - {club.get("tee_height")}mm')
