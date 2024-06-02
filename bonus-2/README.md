# Bonus 2

![](../memes/scratch-the-surface.jpeg)

There are a lot more useful commands that you might need along your way to become a Docker Pro ;)

We will go over some of them real quickly!

## Stop and start

When containers are running in the background, you can stop them with

```shell
docker stop <container_name/container_id>
```

To start one container again, run

```shell
docker start <container_name/container_id>
```

## Log me baby

Whenever you detached from the output of your Docker container(s) and want to show the logs afterwards, you can use

```shell
docker logs <container_name/container_id>
```

Tip: Add the `--follow` (shorthand `-f`) flag after `logs` to keep the logs running. Otherwise, you just get the logs once and not continuously.

## Show me your true self

Sometimes it's helpful to execute a command inside a container.

For that purpose you can use

```shell
docker exec <container_name/container_id> <command>
```

If you also add `-it` after `exec` you can actually achieve two things at the same time:  

You can keep the connection to the command input open with `--interactive` (shorthand `-i`) and simultaneously get a terminal connection to the container with `--tty` (shorthand `-t`).  
So for example with

```shell
docker exec -it <container_name/container_id> /bin/bash
```

you can open a shell like bash and then try what you want to do directly in the container, e.g. investigating what went wrong ;)

## Temporary containers

You can also initiate a container from an image with

```shell
docker run --rm <image_name>
```

This `--rm` (like in "remove") flag functions similarly to summoning a temporary entity for a specific purpose. Once the task is accomplished, the container dissolves gracefully, leaving no residual artifacts.

If you want to be fancy, you can combine it with the `-it` flags from above. Then you get somewhat of an interactive playground that gets demolished once you type `exit`.  
Try it for yourself:

```shell
docker run -it --rm debian:bookworm-slim
```

Since there is sort of a "standard command" that runs, we can even omit a specific command like `bash` and still get an interactive shell connection.
