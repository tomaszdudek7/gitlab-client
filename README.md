# Gitlab Client - Search and download git lab repo!

Do you hate clicking through gitlab just to copy the link
to repository so you can clone it? If you are me, you also realize
then you need to make some directories because you try to keep
things organized - after all, you have actually more repositories
to checkout than you would want.

Let this script do this annoying work for you!

Using client is simple. You put the name of the command - `project` if
using provided helper script - then the name of the gitlab
instance you want to connect to (for example `work`):

```
$ project work
```

It will then walk you through configuration and you will
have to generate accesstoken to your gitlab account (you
can generate it at gitlab's account settings. Token is used
to read project list to use with search).

```
Please provide url to gitlab: https://gitlab.example.com
Please provide access token to gitlab: accessToken
Please provide url base for checkout [ssh://git@gitlab.example.com]: 
Please provide directory for project checkout: /home/my-user/my-projects
```

It will then show you searchable list of projects. You can input
you query. In example I've input `foo` and the list of projects
was narrowed down to projects with in path. Do not press an enter
key to search! It will search as you type.


```
foo

my-user/foo          ▮tools/java/foobar▮     client-a/foo
foony/name           foooo/fooo              foo/repo

```

You can navigate result list, select the repository and then press the enter
key to checkout the repository. It will recreate the group structure in
directories, so in our example `tools/java/foobar` will be checked out
as `/home/my-user/my-projects/tools/java/foobar`.

(yup, it has some UI to use in terminal, not just commands)

If you use the helper script added to `.bashrc` or `.zshrc` it will also
`cd` to directory. By default script will also try to start Intellij to
open the project, but this behavior is easy to disable (remove one
obvious line after you paste the script into the `rc` file).

Obviously next time you checkout something from that `work` gitlab it
won't ask for configuration. Config is saved in `~/.gitlab-client.json`
and if you want you can also crete this file manually.

This script can work with multiple instances of gitlab! It wasn't checked
with cloud gitlab though, so if you can confirm it's runnig with it that would
be great!

## Build and install

1. Fire `./build.sh`. It will pack application into executable `gitlab-client.pyz`.
1. Configure client in `~/.gitlab-client.json` (example format in `example.gitlab-client.json`)
1. (optional) Add helper script (below)  

### Helper script

It's possible to add helper script to your shell. Simply add following to your `.bashrc` / `.zshrc`:

```bash
. /path/to/gitlab-client/helper.sh
```

Usage: `project {gitlab instance, eg. unity} {optional search}`

eg: `project unity tools`
