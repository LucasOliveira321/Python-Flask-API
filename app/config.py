import os


def gen_connection_string():
    db_name = os.environ.get('DB_NAME')
    db_user = os.environ.get('DB_USER')
    db_password = os.environ.get('DB_PASSWORD')
    if os.getenv('CLOUD_SQL_CONNECTION_NAME'):
        db_conn_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')
        conn_template = 'postgresql://%s:%s@/%s?host=/cloudsql/%s' \
                        % (db_user, db_password, db_name, db_conn_name)
    else:
        if os.uname()[0] == 'Linux' or os.uname()[0] == 'Darwin':
            conn_template = f'postgresql://%s:%s@%s/%s?client_encoding=utf8'
        else:
            raise NotImplemented
        db_addr = os.environ.get('DB_ADDR')
        conn_template = conn_template % (db_user, db_password, db_addr, db_name)
    return conn_template


class Configuration:
    SQLALCHEMY_ENGINE_OPTIONS = {'pool_pre_ping': True}
    SQLALCHEMY_DATABASE_URI = gen_connection_string()
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = 3600
    API_URL_PREFIX = '/api/v0'
