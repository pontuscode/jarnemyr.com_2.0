class Config(object):
	DEBUG = False
	TESTING = False
	
	DB_NAME = "trades"
	

	
class ProductionConfig(Config):
	DEBUG = False
	
class DevelopmentConfig(Config):
	DEBUG = True

class TestingConfig(Config):
	TESTING = True
