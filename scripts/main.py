import json as js
import os,stat
import shutil
import base64

FLITERED_SUBSCRIPTION_LINKS_PATH = 'stairspeedtest/results/subscribes.txt'

def clean_public():
    '''
    Clean the public folder before the rendering process
    '''
    # shutil.rmtree('./stairspeedtest/logs',True)
    # shutil.rmtree('./stairspeedtest/results',True)
    shutil.rmtree('public',True)
    os.mkdir('public')
    with open('./public/.gitkeep', 'wb') as f:
        f.writelines('')
        f.close()


def read_config(file):
    '''
    Get config from the file
    '''
    with open(file) as json_file:
        config = js.load(json_file)
    return config

def read_file(file):
    f_s = ''
    with open(file) as f:
        f_s = f.read()
    return f_s

def speedtest(sub_links):
    if isinstance(sub_links,str):
        cmd = './stairspeedtest/stairspeedtest /u ' + sub_links
    elif isinstance(sub_links,list):
        cmd = './stairspeedtest/stairspeedtest /u ' + ' | '.join(sub_links)
    else:
        return
    r_v = os.system(cmd)

def getSSTR():
    if os.path.isdir('./stairspeedtest'):
        pass
    else:
        url = 'https://github.com/magicwenli/stairspeedtest-reborn/releases/latest/download/stairspeedtest_reborn_linux64.tar.gz'
        cmd = 'wget '+ url + ' -O temp.tar.gz && mkdir stairspeedtest && tar zxvf temp.tar.gz && rm temp.tar.gz'
        os.system(cmd)
        try:
            os.chmod('stairspeedtest/stairspeedtest',stat.S_IXUSR)
        except Exception as e:
            print(e)

def create_dictionary(path):
    '''
    Create a dictionary from the subscription file
    '''
    os.mkdir(path)


if __name__ == "__main__":
    conf = read_config('config.json')
    global_conf = conf['global']

    # Start getting the data from the subscriptions
    print('[INFO]Getting the data from the subscriptions...')
    subs = conf['subs']
    sub_list = []
    for sub in subs:
        if subs[sub]['type'] == 'sub':
            sub_list.append(subs[sub]['link'])
    # End getting the data from the subscriptions

    print('[INFO]Start testing stair speed, using stairspeedtest-reborn...')
    getSSTR()
    speedtest(sub_list)
    print('[INFO]Speed test done...')

    Combined = read_file(FLITERED_SUBSCRIPTION_LINKS_PATH)

    print('[INFO]Cleanup...')
    clean_public()

    pathlist = global_conf['path'].split('/')
    parent_path = './public'
    for i in pathlist:
        if(i == pathlist[len(pathlist)-1]):
            break
        create_dictionary(parent_path+'/'+i)
        parent_path = parent_path+'/'+i
    # Creation completed
    print('[INFO]Created!')

    # Start encoding the string to formal vmess subscription format
    print('[INFO]Encoding the string to formal vmess subscription format...')
    Encoded = base64.b64encode(Combined.encode())
    print('[INFO]Encoded!')
    # End encoding the string to formal vmess subscription format

    # Start writing the data to the file
    print('[INFO]Writing the data to the file...')
    with open('./public/' + conf['global']['path'], 'wb+') as f:
        f.write(Encoded)
        f.close()
    print('[INFO]Writing completed!')
    # End writing the data to the file
    os.remove('stairspeedtest/results/subscribes.txt')

    print('Done!')
