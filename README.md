Ansible orchestration csi
=========

* Galaxy: [![Ansible Galaxy](https://img.shields.io/badge/galaxy-tcharl.orchestration_csi-660198.svg?style=flat)](https://galaxy.ansible.com/tcharl/freeipa_server)
* Lint, & requirements: ![Molecule](https://github.com/OsgiliathEnterprise/orchestration_csi/workflows/Molecule/badge.svg)
* Tests: [![Build Status](https://travis-ci.com/OsgiliathEnterprise/orchestration_csi.svg?branch=master)](https://travis-ci.com/OsgiliathEnterprise/orchestration_csi)
* Chat: [![Join the chat at https://gitter.im/OsgiliathEnterprise/platform](https://badges.gitter.im/OsgiliathEnterprise/platform.svg)](https://gitter.im/OsgiliathEnterprise/platform?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Install a container storage interface on top of kubernetes

Requirements
------------

Like any other platform role, executing `tox -e pipdep` and `tox -e dependency` 

Role Variables
--------------

Take a look at the [molecule tests](./molecule/default/converge.yml) tests and the [default variables](./defaults/main.yml)

Dependencies
------------

* [Collections](./requirements-collections.yml)
* [Roles](./requirements-standalone.yml)

License
-------

[Apache-2](https://www.apache.org/licenses/LICENSE-2.0)

Author Information
------------------

* Twitter [@tcharl](https://twitter.com/Tcharl)
* Github [@tcharl](https://github.com/Tcharl)
* LinkedIn [Charlie Mordant](https://www.linkedin.com/in/charlie-mordant-51796a97/)
