import requests as req
import timeit
import time
import pandas as pd
from IPython.display import Image, HTML
import random
from tqdm import tqdm
from ratelimit import limits, sleep_and_retry
from multiprocessing import Pool, Manager, cpu_count
from functools import partial
 
 
API_POKEMON = 'https://pokeapi.co/api/v2/pokemon/{pokemon}'
 
#  To see how it ran
# def infoDebugger(title):
#     print(title)
#     print('module name:', __name__)
#     if hasattr(os, 'getppid'):
#         print('parent process:', os.getppid())
#     print('process id:', os.getpid())
 
 
@sleep_and_retry
@limits(calls=100, period=60)
def call_api (url) :
    response = req.get(url)
    
    if response.status_code == 404 :
        return 'Not Found'
    if response.status_code != 200 :
        raise Exception( 'API response: {}' .format(response.status_code))
    return response
 
 
# https://docs.python.org/2/library/multiprocessing.html
 
def get_number_pokemon () :
    res = req.get(API_POKEMON.format(pokemon= '' ))
    number_pokemon = res.json()[ 'count' ]
    res_url = call_api(API_POKEMON.format(pokemon= '?offset=0&limit={limit}' .format(limit=str(number_pokemon))))
    pokemon_links_values = [link[ 'url' ] for link in res_url.json()[ 'results' ]]
    return pokemon_links_values
 
def get_pokemon_multiprocess (listManager=None, links_pokemon=None, process= 0 ) :
#     print('Called Pokemon', process)
    link = links_pokemon[process]
    info = None
    resolved = False
#     print(link)
    
    try :
        while not resolved:
 
              
            res = None
            tooManyCalls = False
            
            try :
                res = call_api(link)
                if res == 'Not Found' :
                    resolved = True
                    break
            except Exception as e:
                print(e)
                if e == 'too many calls' :
                    tooManyCalls = True
                    
            if tooManyCalls:
                time.sleep( 60 )
                
            elif res.status_code < 300 :
 
                pokemon_info = res.json()
 
                info = {
                    'Image' : pokemon_info[ 'sprites' ][ 'front_default' ],
                    'id' :  pokemon_info[ 'id' ],
                    'name' : pokemon_info[ 'name' ],
                    'height' : pokemon_info[ 'height' ],
                    'base_experience' : pokemon_info[ 'base_experience' ],
                    'weight' : pokemon_info[ 'weight' ],
                    'species' : pokemon_info[ 'species' ][ 'name' ]
 
                }
 
                resolved = True
                
            elif res.status_code == 429 :
                print(res.status_code)
                time.sleep( 60 )
 
            else :
                print(res.status_code)
                sleep_val = random.randint( 1 , 10 )
                time.sleep(sleep_val)
                
    except Exception as e:
        print(e)
    finally :
        if info != None :
            listManager.append(info)
            time.sleep( 0.5 )
            return
 
 
def image_formatter (im) :
    return f'<img src=" {im} ">'
 
 
def main_pokemon_run_multiprocessing () :
    ## cannot be 0, so max(NUMBER,1) solves this
    workers = max(cpu_count() -1 , 1 )
 
    ## create the pool
    manager = Manager()
    
    ## Need a manager to help get the values async, the values will be updated after join
    listManager = manager.list()
    pool = Pool(workers)
    try :
 
        links_pokemon = get_number_pokemon()
        part_get_clean_pokemon = partial(get_pokemon_multiprocess, listManager, links_pokemon)
 
#         could do this the below is visualize the rate success /etc
#         pool.imap(part_get_clean_pokemon, list(range(0, len(links_pokemon))))
#         using tqdm to see progress imap works
        for _ in tqdm(pool.imap(part_get_clean_pokemon, list(range( 0 , len(links_pokemon)))), total=len(links_pokemon)):
            pass
        pool.close()
        pool.join()
    finally :
        pool.close()
        pool.join()
        
    pokemonList = list(listManager)
    
    df_pokemon = pd.DataFrame(pokemonList)
    df_pokemon.sort_values([ 'id' ],inplace= True )
    return df_pokemon, HTML(df_pokemon.iloc[ 0 : 4 ].to_html(formatters={ 'Image' : image_formatter}, escape= False ))
    