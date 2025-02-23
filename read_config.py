 
import telegram 
import telegram.ext
import configparser 
import redis

config=configparser.ConfigParser()
config.read('config.ini')
print(config['REDIS']['HOST'])
print(config['REDIS']['PASSWORD'])
print(config['REDIS']['REDISPORT'])
print(config['REDIS']['USER_NAME'])
print(config['REDIS']['DECODE_RESPONSE'])

print(type(config['REDIS']['REDISPORT']))
print(repr(config['REDIS']['HOST']))
print("redis-17507.c322.us-east-1-2.ec2.redns.redis-cloud.com")

# assert(config['REDIS']['HOST'] == "redis-17507.c322.us-east-1-2.ec2.redns.redis-cloud.com")
# assert(config['REDIS']['PASSWORD'] == "BFIzvcGNrI1l3XPhHCs7DwIsXqcl0vR0")
# assert(config['REDIS']['REDISPORT'] == 17507)
# assert(config['REDIS']['USER_NAME'] == "default")
# assert(config['REDIS']['DECODE_RESPONSE'] == True)

redis1 = redis.Redis(host=(config['REDIS']['HOST']),
                         password=(config['REDIS']['PASSWORD']),
                         port=(config['REDIS']['REDISPORT']),
                         decode_responses=(config['REDIS']['DECODE_RESPONSE']),
                         username=("default"))
success = redis1.set('foo', 'bar')
# True
result = redis1.get('foo')
print(result)

print(redis1.ping())