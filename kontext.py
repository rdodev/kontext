# Ruben Orduz (c) 2018
from kubernetes import config
import click, pick, json, sys, yaml

__error_prefix__ = click.style("[Error] ", 'red')
__info_prefix__  = click.style("[Info] ", 'blue')

__DEFAULT_LOC__ = ''


def kontext():
    '''
    Very simple utility to visually select Kubernetes config contexts. It reads all the available contexts
    from KUBECONFIG (or whereever the kubernetes client is set).
    '''
    # load kubeconfig and get context
    config.load_kube_config()
    __DEFAULT_LOC__ = config.kube_config.KUBE_CONFIG_DEFAULT_LOCATION
    kubectx = get_context_from_user()
    info("Selected kubeconfig context: " + kubectx)
    # First, read and parse the yaml file
    info('Opening: ' + __DEFAULT_LOC__)
    with open(__DEFAULT_LOC__, 'r') as f:
        f.seek(0)
        y = yaml.load(f.read())
    # Set context to chosen by user
    y['current-context'] = kubectx
    # Let's write to the file
    info('Writing context to kubeconfig')
    with open(__DEFAULT_LOC__, 'w') as f:
        f.seek(0)
        f.write(yaml.dump(y))
    info('Success. kubectl commands should be running against ' + kubectx + ' cluster.')



def get_context_from_user():
    contexts, active_context = config.list_kube_config_contexts()
    if not contexts:
        error("Cannot find any context in kubeconfig file.")
    contexts = [context['name'] for context in contexts]
    active_index = contexts.index(active_context['name'])
    option, _ = pick.pick(contexts, title="Please select the context you wish to set as default",
                     default_index=active_index)
    return option

def error(msg):
    click.echo(__error_prefix__ + msg)
    sys.exit(1)

def info(msg):
    click.echo(__info_prefix__ + msg)


if __name__ == '__main__':
   kontext()