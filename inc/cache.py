import os
from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options

cache = CacheManager(**parse_cache_config_options({
	'cache.type': 'file',
	'cache.data_dir': os.path.join(os.getcwd(), 'cache', 'data'),
	'cache.lock_dir': os.path.join(os.getcwd(), 'cache', 'lock'),
	'expire': '86400',
}))