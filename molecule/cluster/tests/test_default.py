import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_redis_file(host):
    u = host.user('redis')

    assert u.name == 'redis'
    assert 'redis' in u.groups


def test_redis_conf_file(host):
    f = host.file('/etc/redis/6379.conf')

    assert f.exists
    assert f.user == 'redis'


def test_redis_nodes_file(host):
    f = host.file('/etc/redis/nodes.conf')

    assert f.exists


def test_redis_init_file(host):
    f = host.file('/etc/init.d/redis-6379')

    assert f.exists


def test_redis_pid_file(host):
    f = host.file('/var/run/redis/6379.pid')

    assert f.exists


def test_redis_service(host):
    s = host.service('redis-6379')

    assert s.is_enabled
    assert s.is_running
