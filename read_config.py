 
import telegram 
import telegram.ext
import configparser 
import redis

config=configparser.ConfigParser()
config.read('7940_lab3/config.ini')
redis1 = redis.Redis(host=(config['REDIS']['HOST']),
                         password=(config['REDIS']['PASSWORD']),
                         port=(config['REDIS']['REDISPORT']),
                         decode_responses=(config['REDIS']['DECODE_RESPONSE']),
                         username=(config['REDIS']['USER_NAME']))
print(config['REDIS']['PASSWORD'])
print(config['REDIS']['REDISPORT'])
print(config['REDIS']['USER_NAME'])
print(config['REDIS']['DECODE_RESPONSE'])
print(redis1.ping())