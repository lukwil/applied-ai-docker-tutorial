# Applied AI: Intro to Docker

## Preparation

Head over to the [Docker playground](https://labs.play-with-docker.com/)[^1] and log in.

Then add a new instance with the button on the left.

You can setup the environment by copying and executing the following command:

```shell
curl https://raw.githubusercontent.com/lukwil/applied-ai-docker-tutorial/main/setup.sh | sh
```

You can then change into the directory of our tutorial:

```shell
cd applied-ai-docker-tutorial
```

We will use the nano editor, which makes it pretty easy to work with the files we need.  
To create or edit a file, simply type `nano <filename>` and make the changes. To exit nano, press <kbd>Ctrl</kbd>+<kbd>X</kbd> and then <kbd>y</kbd> (yes) to accept your changes or <kbd>n</kbd> (no) to discard them.

## Structure

0. [Introduction](step-0-intro/README.md) (5 min)
1. [Our first container](step-1/README.md) (5 min)
2. [Simple web app](step-2/README.md) (10 min)
3. [Data persistance](step-3/README.md) (10 min)
4. [Multi-container apps](step-4/README.md) (10 min)

Bonus:

1. [Docker compose](bonus-1/README.md) (5-10 min)
2. [More useful Docker commands](bonus-2/README.md) (5-10 min)

## Further reading

There are so many commands you may need, that it seems impossible at first to memorize them all. Luckily, there is an [official one-page cheatsheet](https://docs.docker.com/get-started/docker_cheatsheet.pdf) as well as the [official documentation](https://docs.docker.com/engine/reference/commandline/docker/). Also, consider using tools like ChatGPT - they can save you a lot of time finding the right commands and configuration!

---

[^1]: Alternatively, you can also use [Killercoda](https://killercoda.com/) and their playground Ubuntu instance. However, you only have one hour of runtime instead of four compared to the Docker playground.
