# EXTERNAL-SOURCE-LOAD

## Description

The aim of this project is to create a **load** in an ELT that will have a rest api, then deposit the data in a datalake and finally send a notification to the transfom that a document has been added.

## Getting Started

### Prerequisites

List all dependencies and their version needed by the project as :

* IDE used pycharm 2024.3 or later [download](https://www.jetbrains.com/pycharm/download/?section=windows)
* Python 3.13 or later [official doc](https://www.python.org/downloads/)
* Git version 2.47.1 ou ultérieure [official doc](https://git-scm.com/)

### Configuration

Install requiremenets 
````shell
pip install -r requirements.txt
````

Copy and modify the .env
````shell
cp .env.example .env
````

## Development environment


## Collaborate

* Workflow
    * [Gitflow](https://www.atlassian.com/fr/git/tutorials/comparing-workflows/gitflow-workflow#:~:text=Gitflow%20est%20l'un%20des,les%20hotfix%20vers%20la%20production.)
    * [How to commit](https://www.conventionalcommits.org/en/v1.0.0/)
    * [How to use your workflow](https://nvie.com/posts/a-successful-git-branching-model/)

    * Propose a new feature in [Github issues](https://github.com/CPNV-ES-BI1-SBB/EXTERNAL-SOURCE-LOAD-DATALAKE/issues)
    * Pull requests are open to merge in the develop branch.
    * Release on the main branch we use GitFlow and not with GitHub release.
    * Issues are added to the [github issues page](https://github.com/CPNV-ES-BI1-SBB/EXTERNAL-SOURCE-LOAD-DATALAKE/issues)

### Commits
* [How to commit](https://www.conventionalcommits.org/en/v1.0.0/)
```bash
<type>(<scope>): <subject>
```

* **build** : changements qui affectent le système de build ou des dépendances externes (npm, make…)
* **ci** : changements concernant les fichiers et scripts d’intégration ou de configuration (Travis, Ansible, BrowserStack…)
* **feat** : ajout d’une nouvelle fonctionnalité
* **fix** : correction d’un bug
* **perf** : amélioration des performances
* **refactor** : modification qui n’apporte ni nouvelle fonctionalité ni d’amélioration de performances
* **style** : changement qui n’apporte aucune alteration fonctionnelle ou sémantique (indentation, mise en forme, ajout d’espace, renommante d’une variable…)
* **docs** : rédaction ou mise à jour de documentation
* **test** : ajout ou modification de tests

examples :
```bash
feat(MyClass): add a button in the ...
````
```bash
feat(example.js): change name into username
````

## License
MIT

## Contact

* If needed you can create an issue on GitHub we will try to respond as quickly as possible.
