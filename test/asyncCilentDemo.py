# coding: utf8
from fadeaway.client import ServerProxy
from fadeaway.client import Async

def callback(res, error=None):
    '''error will be set if there is an error while calling'''
    if not error:
        print '[callback]', res
    else:
        print error

def callback_for_mix(num_arg, str_arg, list_arg, dict_arg, error=None):
    if not error:
        print '[mix callback]', num_arg, str_arg, list_arg, dict_arg
    else:
        print error

if __name__ == '__main__':
    ss = ServerProxy(Async, 'localhost', 9151)
    ss.deploy()
    d = ss.Demo()
    d.hello('billy').then(callback, timeout=3)
    d.hello('rowland').then(callback, timeout=7)
    d.hello('lily').then(callback)
    d.hello('qqq').then(callback, timeout=7)
    d.hello('ccc').then(callback, timeout=3)
    d.test_number(222).then(callback, timeout=1)
    d.test_mix(-1, 'greetings', ['a', 'b', 'c'], {"abc": 123}).then(callback)
