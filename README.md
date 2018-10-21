# Kontext

If you work with Kubernetes enough, you will find yourself having to work with several clusters at once, and users
and contexts therein. The aim of this utility is to make it easier to select which context
you wish to set as default so that, for example, `kubectl` runs against the desired cluster context.

## Supported Python Versions

This utility was written and manually tested with python 3.7. No effort was made to test against Python 2 and won't be.

## Installation

```
git clone git@github.com:rdodev/kontext.git
cd kontext
pipenv install .
```

## Usage

```
pipenv run kontext
```

## Warnings And Caveats

1. This utility is only at version 0.0.1 which means:
    * can and will break
    * can wipe your kubeconfig file
    * recommend *NOT* to use when managing production clusters
1. Untested
1. Absolutely no warranty either implicit or explicit

## TODOs

* Testing
* Better error handling