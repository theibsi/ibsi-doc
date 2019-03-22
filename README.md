# IBSI Documentation

Readthedocs documentation for the Imaging Biomarker Standardisation Initiative (IBSI).

## Workflow

First, clone the ibsi-doc repository locally (this will create a new folder, 
`ibis-doc`, which contains the repository):

```
$ git clone  https://github.com/theibsi/ibsi-doc.git
```

Next, move into the repository and create a branch (after clone, the `master` 
branch is checked out):

```
$ cd ibsi-doc/
$ git checkout -b <branch_name>
```

Now the repository is switched to the new branch and you can make your changes.

To check your changes, you can build a local version of the site. To do that:

```
$ cd docs/
$ make html
```
Then, go to `docs/_build/html` and open `index.html`

After you're done, we need to stage and commit these changes to the repository:

```
$ git commit -a -m "<Commit Message>"
```

Finally, push the changes to the github. If you have the github open in a browser,
this should also prompt to create a pull request

```
$ git push origin <branch_name>
```
