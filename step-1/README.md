# Step 1

First, change into the directory of `step 1`:

```shell
cd step-1
```

## Hello THA!

Create a new file called `app.py`[^1] (-> `nano app.py`) and fill it with

```python
print('Hello, THA!')
```

You can test if everything is working correctly by running

```shell
python app.py
```

## Dockerize me!

In order to get our "app" up and running in a container, we first need to create a definition for our app which is called a `Dockerfile`. You can imagine it as an architectural blueprint one uses for building a house. Each command like `FROM`, `COPY`, `CMD` etc. represents a layer in our container. The [official documentation](https://docs.docker.com/engine/reference/builder/) provides comprehensive information on every possible command.

Fill the `Dockerfile` (-> `nano Dockerfile`) with

```Dockerfile
# base image
FROM python

# copy the contents of the folder we are currently working in to our container
COPY . .

# run our app
CMD ["python", "app.py"]
```

### Build'n'run

Before we are able to run our very own container, we first need to build our custom Docker image via the Docker [command line interface](https://docs.docker.com/engine/reference/commandline/docker/).

```shell
docker build --tag applied-ai-docker-tutorial:step-1 .
```

Here, we are tagging (`--tag`, more often used via the shorthand `-t`) our image (based on the Dockerfile in the current directory -> `.`) with the name `applied-ai-docker-tutorial` and (optional) tag `step-1`[^2].

Following that, we can run our container with

```shell
docker run applied-ai-docker-tutorial:step-1
```

and should hopefully see `Hello, THA!` as the only output :)

### Image sizes

You can list all the locally available docker images via

```shell
docker images
```

We see that our "Hello, THA!" example is still pretty large, taking up more than 1 GB of disk space. To counter that, we might want to use a different python base image provided by [Docker Hub](https://hub.docker.com/_/python). Not only can we set different flavors of base images but also specify e.g. different python versions.

For example, try to replace the first line in the Dockerfile with

```Dockerfile
# base image
FROM python:3.12-slim
```

and rebuild your image with

```shell
docker build -t applied-ai-docker-tutorial:step-1-slim .
```

or use

```Dockerfile
# base image
FROM python:3.12-alpine

```

and rebuild your image with

```shell
docker build -t applied-ai-docker-tutorial:step-1-alpine .
```

Does running `docker images` show you any difference?

## Next step

Head over to [step 2](../step-2/README.md)!

---

[^1]: You can create files in Linux (without writing anything in them) with `touch <filename>`, e.g. `touch app.py`

[^2]: If no tag is provided, Docker implicitly assigns it the tag `latest`. It is also possible to assign multiple tags to an image. Just add `-t <name>:<optional_tag>` for each one you want to assign.
