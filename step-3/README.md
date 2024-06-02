# Step 3

First, change into the directory of `step 3`:

```shell
cd ../step-3
```

## Save the data

Docker treats containers like disposable products. This means that due to their isolated nature, data only remains stored in the container unless this is explicitly specified otherwise. If a container is stopped, deleted and recreated, it reverts to the original state of the image.

Fortunately, we can use [different mount methods](https://docs.docker.com/storage/volumes/) to save our progress!

## Bind mount

Using bind mounts, we can mount a folder of our local file system directly to a Docker container.
If the folder does not already exist, it is created by Docker.

The command for this is:

```shell
docker run --volume ./data:/data -p 5000:5000 applied-ai-docker-tutorial:step-2
```

We mount (`--volume`, shorthand `-v`) to the `data` folder in the current directory to `/data` in the container.

If we stop the container and create a new container from our image with

```shell
docker run -v ./data:/data -p 5000:5000 applied-ai-docker-tutorial:step-2
```

we should observe that our data is still there!  
And we can also see that our database file is saved locally in the `data` folder.

Note, that if we are running on Windows or macOS hosts, the host path has to be absolute!

## Create a named volume

Another method to persist data are the so-called named volumes.

We can create one with

```shell
docker volume create applied-ai-demo-data
```

and use it to bind to a container with

```shell
docker run -v applied-ai-demo-data:/data -p 5000:5000 applied-ai-docker-tutorial:step-2
```

There are several advantages of using named volumes over bind mounts, one of them being more performant. Since they are managed by Docker they are also generally easier to handle.

## Next step

Head over to [step 4](../step-4/README.md)!
