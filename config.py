class BaseConfig(object):
    """���û��� """
    SECRET_KEY='makesure to set very secret key'

class DevelopmentConfig(BaseConfig):
    """������������"""
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='mysql+mysqldb://root@localhost:3306/jobplus4-5?charset=utf8'

class ProductionConfig(BaseConfig):
    """������������"""
    pass

class TestingConfig(BaseConfig):
    """���Ի�������"""
    pass

configs={
        'development':DevelopmentConfig,
        'production':ProductionConfig,
        'testing':TestingConfig
        }
