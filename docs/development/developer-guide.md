# Developer Guide

This developer guide includes complete instructions for setting up a developer
environment.

## Setup

To work on this operator you should:

 - Have a recent version of Go installed (1.18.1)
 - Have minikube installed

**Important** For minikube, make sure to enable [DNS plugins](https://minikube.sigs.k8s.io/docs/handbook/addons/ingress-dns/).

```bash
$ minikube addons enable ingress
$ minikube addons enable ingress-dns
```

Note that for production clusters (e.g., [GKE](https://cloud.google.com/kubernetes-engine/docs/concepts/ingress)) I believe this
addon is enabled by default. The basic Flux networking (pods seeing one another) won't work if your cluster does not support DNS.
You also won't be able to expose the service with minikube service if you don't do the above (but port-forward would technically work)
You'll then also want to clone the repository.

```bash
# Clone the source code
$ git clone https://github.com/flux-framework/flux-operator
$ cd flux-operator
```

### Local Development

After cloning, you need to create your MiniKube cluster before doing anything else!

#### 1. Quick Start

Here is a quick start for doing that, making the namespace, and installing the operator.

```console
# Start a minikube cluster
$ minikube start

# Make a flux operator namespace
$ kubectl create namespace flux-operator
namespace/flux-operator created
```

Here is how to build and install the operator:

```
# Build the operator
$ make

# How to make your manifests
$ make manifests

# And install. This places an executable "bin/kustomize"
$ make install
```

#### 2. Configs

##### Default Config

Our "default" job config, or custom resource definition "CRD" can be found in [config/samples](https://github.com/flux-framework/flux-operator/tree/main/config/samples).
We will walk through how to deploy this one, and then any of the ones in our examples gallery.
When you've built and installed the operator, here is how to "launch"
the Mini Cluster (or if providing a command, an ephemeral job):

```bash
$ kubectl apply -f config/samples/flux-framework.org_v1alpha1_minicluster.yaml
```

there is a courtesy function to clean, and apply the samples:

```bash
$ make clean  # remove old flux-operator namespaced items
$ make apply  # apply the setup and job config
$ make run    # make the cluster
```

or run all three for easy development!

```bash
$ make redo  # clean, apply, and run
```

To see logs for the job, you'd do:

```bash
$ kubectl logs -n flux-operator job.batch/flux-sample
```

And this is also:

```bash
$ make log
```

But the above gives you a (somewhat random?) pod. If you want to see a specific one do:

```bash
./script/log.sh flux-sample-0-b5rw6
```

E.g., rank 0 is the "main" one. List running pods (each pod is part of a batch job)

```bash
$ make list
```

And shell into one with the helper script:

```bash
./script/shell.sh flux-sample-0-b5rw6
```

Note that if you are running more than one container, you need a custom command for shell:

```bash
$ kubectl exec --stdin --tty -n flux-operator flux-sample-0-vsnvz -c flux-sample-1 -- /bin/bash
```

Where the first is the name of the pod, and `-c` references the container.

##### Example Configs

We provide an extended gallery of configs for:

 - [Flux Restful Examples](https://github.com/flux-framework/flux-operator/tree/main/examples/flux-restful) that deploy a web interface to submit jobs to.
 - [Headless Test Examples](https://github.com/flux-framework/flux-operator/tree/main/examples/tests) that run commands directly, ideal for testing.

Generally these sets of configs are the same (e.g., same container bases and other options) and only vary in providing a command entrypoint (for the headless)
or not (for the Flux Restful). To make it easy to clean up your cluster and apply a named config, you have two options:

###### Flux Restful

We call this the main set of "examples." To clean up Minikube, apply a named config, and run the example via a Mini Cluster, first match the name of the yaml
file to a variable name. E.g., for the following files, the names would be:

```console
$ tree examples/flux-restful/
├── minicluster-conveyorlc.yaml       (- name=conveyorlc
├── minicluster-lammps.yaml           (- name=lammps
└── minicluster-osu-benchmarks.yaml   (- name=osu-benchmarks
```

This, to run the full example for conveyorlc:

```bash
$ make name=conveyorlc redo_example
```

Be careful running this on a production cluster, as it will delete all Kubernetes objects in the namespace.
If you just want to just apply the new job and run the cluster, do:

```bash
$ make name=conveyorlc example
$ make run
```

###### Headless Tests

Our headless tests are modified examples intended to be run without the web interface.
The naming convention is the same as above, except we are concerned with files
in the examples test folder:

```console
$ tree examples/tests/
examples/tests/
├── hello-world           (- name=hello-world
│   └── minicluster.yaml
└── lammps                (- name=lammps
    └── minicluster.yaml
```

Thus, to run the full example for hello-world you can do:

```bash
$ bash script/test.sh hello-world
```
or (for a less scripted run):

```bash
$ make name=hello-world redo_test
```

If you just want to just apply the new job without a cleanup, do:

```bash
$ make name=hello-world applytest
$ make run
```

Note that there is a default sleep of ~20 seconds for all jobs (so the worker nodes start after the broker)
so they will not run instantly. You can list pods to get an id, and then view logs:

```bash
$ make list
$ bash script/log.sh <pod>
```

Also note that these headless tests have `test: true` in the config,
meaning you will only see output with the command above from what you actually ran.
We do this because we test them in CI, and we don't want the other verbose output
to get in the way! If you want to disable this quiet mode, just comment out
this parameter in the configuration.


### Interacting with Services

Currently, the most reliable thing to do is port forward:

#### port-forward

If we run as a ClusterIP, we can accomplish the same with a one off `kubectl port-forward`:

```console
kubectl port-forward -n flux-operator flux-sample-0-zdhkp 5000:5000
Forwarding from 127.0.0.1:5000 -> 5000
```

This means you can open [http://localhost:5000](http://localhost:5000) to see the restful API (and interact with it there).

If you want to use a minikube service, this seems to work, but is spotty - I think because
minikube is expecting the service to be available from any pod (it is only running from index 0).
If you want to try this:

```console
$ minikube service -n flux-operator flux-restful-service --url=true
```

But for now I'm developing with port forward.


## Build Images

If you want to build the "production" images - here is how to do that!
This happens in our Docker CI, however you can build (and deploy if you are an owner) them too!

```bash
$ make docker-build
$ make docker-push
```
```bash
# operator lifecycle manager
$ operator-sdk olm install
$ make bundle
$ make bundle-build
$ make bundle-push
```

And for the catalog:

```bash
$ make catalog-build
$ make catalog-push
```

Note that these are done in CI so you shouldn't need to do anything from the command line.

## Other Developer Commands

### Build Operator Yaml

To generate the CRD to install to a cluster, we've added a `make build-config` command:

```bash
$ make build-config
```

That will generate a yaml to install the operator (with default container image) to a
cluster in `examples/dist`. This file being updated is tested in the PR, so you
should do it before opening.

## Build API

We use openapi to generate our Python SDK! You can update it as follows:

```bash
$ make api
```

## Pre-push

We likely want to build the config _and_ API generation in one swoop.
We have a courtesy command for that:

```bash
$ make pre-push
```

## Container Requirements

If you are looking to build a container to use with the Flux Operator, we have a set of
example containers [here](https://github.com/rse-ops/flux-hpc) and general guidelines are below.
Generally we recommend using the flux-sched base image
so that install locations and users are consistent. This assumes that:

 - we are currently starting focus on supporting debian bases
 - if you created the flux user, it has uid 1000 (unless you customize `fluxUser.Uid`)
 - sudo is available in the container (apt-get install -y sudo)
 - `/etc/flux` is used for configuration and general setup
 - `/usr/libexec/flux` has executables like flux-imp, flux-shell
 - flux-core / flux-sched with flux-security should be installed and ready to go.
 - If you haven't created a flux user, one will be created for you (with a common user id 1000 or `fluxuser.Uid`)
 - Any executables that the flux user needs for your job should be on the path (if launching command directly)
 - Do not have any requirements (data or executables in root's home)
 - The container (for now) should start with user root, and we run commands on behalf of flux.
 - You don't need to install the flux-restful-api (it will be installed by the operator)
 - munge should be install, and a key generated at `/etc/munge/munge.key`

For the last point, since all Flux running containers should have the same munge key
in that location, we simply use it. The pipeline will fail if the key is missing from any
Flux runner container.  For the curve.cert that we need to secure the cluster, we will
be running your flux runner container before the indexed job is launched, generating
the certificate, and then mapping it into the job pods via another config map.
Note that we considered generating this natively in Gom, however the underlying library to do this
generation that is [available in Go](https://pkg.go.dev/github.com/zeromq/goczmq#section-readme)
requires system libraries, and thus would be annoying to add as a dependency.

These criteria are taken from the [flux-sched](https://github.com/flux-framework/flux-sched/blob/master/src/test/docker/focal/Dockerfile)
base image [available on Docker hub](https://hub.docker.com/r/fluxrm/flux-sched) as `fluxrm/flux-sched:focal`,
and we strongly suggest you use this for your base container to make development easier!
If you intend to use the [Flux RESTful API](https://github.com/flux-framework/flux-restful-api)
to interact with your cluster, ensure that flux (python bindings) are on the path, along with
either python or python3 (depending on which you used to install Flux).
If/when needed we can lift some of these constraints, but for now they are
reasonable. If you use this image, you should have python3 and pip3 available to you,
and the active user is `fluxuser`. This means if you want to add content, either you'll
need to change the user to `root` in a build (and back to `fluxuser` at the end), use sudo, or
install to `/home/fluxuser`.


## Testing

Testing is underway! From a high level, we want three kinds of testing:

 - Unit tests, which will be more traditional `*_test.go` files alongside others in the repository (not done yet)
 - End to end "e2e" tests, also within Go, to test an entire submission of a job, also within Go. (not done yet)
 - Integration testing, likely some within Go and some external to it. (in progress)

### Integration

For the integration testing outside of Go, we currently have basic tests written that allow the following:

1. Write a custom resource definition (CRD) for a named mini cluster under `examples/tests/${name}` as `minicluster.yaml`.
2. The CRD should set `test:true` and include a command to run, and a container to do it.
3. Add your test name, container, and estimated running time to `.github/workflows/main.yaml`
4. If your tests require a working directory, it must be set in the CRD for the headless test.
5. If a test is deterministic, add a `test.out` to the output folder that we can validate results for.
6. We will validate output (if provided) and that containers exit with 0.

To run the test (and you can also do this locally) we use the `script/test.sh` and provide a name and the estimated
job time, just like in actions. The below example runs the "hello-world" test and gives it 30 seconds to finish.

```bash
./bin/bash script/test.sh hello-world 10
```
```console
...
NAME                  READY   STATUS    RESTARTS   AGE
flux-sample-0-ng8c5   1/1     Running   0          3s
flux-sample-1-nxqj9   1/1     Running   0          3s
flux-sample-2-vv7jr   1/1     Running   0          3s
flux-sample-3-kh2br   1/1     Running   0          3s
Pods: flux-sample-0-ng8c5 flux-sample-1-nxqj9 flux-sample-2-vv7jr flux-sample-3-kh2br
Pod: flux-sample-0-ng8c5
Actual:
hello world
Expected:
hello world
```
What you don't see in the above is that we also use kubectl to ensure that the exit code for all containers
(typically 4) is 0. Also note that the "sleep" time doesn't have to be exact, it's technically not necessary because we are waiting
for the output to finish coming (and the job to stop). I added it to provide a courtesy message to the user and developer.
Finally, note that for big containers it's suggested to pull them first, e.g.,:

```bash
$ minikube ssh docker pull ghcr.io/rse-ops/lammps:flux-sched-focal-v0.24.0
```
The tests above are headless, meaning they submit commands directly, and that way
we don't need to do it in the UI and can programmatically determine if they were successful.
Finally, note that if you have commands that you need to run before or after the tests,
you can add a `pre-run.sh` or `post-run.sh` in the directory. As an example, because minikube
is run inside of a VM, if you are using a host volume mount, it won't actually show up on your host!
This is because it's inside the VM. This you might want to move files there before the test, e.g.,:

```bash
#!/bin/bash

HERE=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

echo "Copying local volume to /tmp/data-volumes in minikube"

# We don't care if this works or not - mkdir -p seems to bork
minikube ssh -- mkdir -p /tmp/data-volumes
minikube cp ${HERE}/data/pancakes.txt /tmp/data-volumes/pancakes.txt
minikube ssh ls /tmp/data-volumes
```

and then clean up after

```bash
#!/bin/bash

echo "Cleaning up /tmp/data-volumes in minikube"
minikube ssh -- sudo rm -rf /tmp/data-volumes
```

This would be the same for anytime you use minikube and want to create a local volume. It's not actually on your host,
but rather in the VM. For an example test that does this, see the `examples/tests/volumes` example.

## Documentation

The documentation is provided in the `docs` folder of the repository, and generally most content that you might want to add is under
`getting_started`. For ease of contribution, files that are likely to be updated by contributors (e.g., mostly everything but the module generated files)
are written in markdown. If you need to use [toctree](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#table-of-contents) you should not use extra newlines or spaces (see index.md files for examples). The documentation is also provided in Markdown (instead of rst or restructured syntax) to make contribution easier for the community.

Finally, we recommend you use the same development environment also to build and work on
documentation. The reason is because we import the app to derive docstrings,
and this will require having Flux.

### Install Dependencies and Build

The documentation is built using sphinx, and generally you can
create a virtual environment:

```bash
$ cd docs
$ python -m venv env
$ source env/bin/activate
```
And then install dependencies:

```console
$ pip install -r requirements.txt

# Build the docs into _build/html
$ make html
```

### Preview Documentation

After `make html` you can enter into `_build/html` and start a local web
server to preview:

```console
$ python -m http.server 9999
```

And open your browser to `localhost:9999`
