import io
import os
import json
import pathlib
import datetime
import distutils.dir_util


def get_absolute_path_of_project_directory():
    abs_path = ''
    current_path = pathlib.Path().absolute()

    for path_name in str(current_path).split('/'):
        abs_path += path_name + '/'

        if path_name == 'melon-playlist-continuation':
            break

    return abs_path


def write_json(data, fname, is_submit=False):
    def _conv(o):
        if isinstance(o, (np.int64, np.int32)):
            return int(o)
        raise TypeError

    if type(data) != list:
        raise Exception('result 형태는 list of dictionary 타입으로 만드시오.')
    else:
        if type(data[0]) != dict:
            raise Exception('result 형태는 list of dictionary 타입으로 만드시오.')
        else:
            if set(data[0].keys()) != set(['id', 'songs', 'tags']):
                raise Exception('dictionary의 key는 id, songs, tags만 됩니다.')

    base_path = get_absolute_path_of_project_directory()
    base_path += 'submit_val/' if is_submit else 'local_val/'
    now = datetime.datetime.now().strftime('%m%d_%H%M%S')

    if '.json' in fname:
        prefix = fname.split('.')[0]
        fname = prefix + '_' + now + '.json'
    else:
        fname += '_' + now + '.json'

    parent = os.path.dirname(base_path + fname)
    distutils.dir_util.mkpath(parent)
    with io.open(base_path + fname, 'w', encoding='utf-8') as f:
        json_str = json.dumps(data, ensure_ascii=False, default=_conv)
        f.write(json_str)