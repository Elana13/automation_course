from werkzeug.security import safe_str_cmp
from models.user import UserModel


def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user
     # return None

def identity(payload):
    '''
    Functios that gets called when user has already authenticated, and Flask-JWT verified
    :param payload: A dictionary with "identity" key - user id
    :return: A UserModel object
    '''

    user_id = payload['identity']
    return UserModel.find_by_id(user_id)


