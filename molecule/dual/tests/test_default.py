import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_redis_user(host):
    u = host.user('redis')

    assert u.name == 'redis'
    assert 'redis' in u.groups


def test_redis_conf_6378_file(host):
    f = host.file('/etc/redis/6378.conf')

    assert f.exists
    assert f.user == 'redis'

    s = list(filter(lambda x: len(x) > 0, f.content_string.split('\n')))

    assert 'bind 127.0.0.1' in s
    assert 'port 6378' in s


def test_redis_conf_6379_file(host):
    f = host.file('/etc/redis/6379.conf')

    assert f.exists
    assert f.user == 'redis'

    s = list(filter(lambda x: len(x) > 0, f.content_string.split('\n')))

    assert 'bind 127.0.0.1' in s
    assert 'port 6379' in s


def test_redis_init_file(host):
    f1 = host.file('/etc/init.d/redis-6378')
    f2 = host.file('/etc/init.d/redis-6379')

    assert f1.exists
    assert f2.exists


def test_redis_pid_file(host):
    f1 = host.file('/var/run/redis/6378.pid')
    f2 = host.file('/var/run/redis/6379.pid')

    assert f1.exists
    assert f2.exists


def test_redis_service(host):
    s1 = host.service('redis-6378')
    s2 = host.service('redis-6379')

    assert s1.is_enabled
    assert s1.is_running
    assert s2.is_enabled
    assert s2.is_running
