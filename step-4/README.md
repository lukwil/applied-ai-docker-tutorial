# Step 4

First, change into the directory of `step 4`:

```shell
cd ../step-4
```

## Do one thing - but do it right!

![](../memes/code-mess.png)

Docker is about the separation of concerns: A container only does one thing (and does it right).

This also means that we should put our database in a separate container. At the same time, we also want to switch from a file-based database such as SQLite to PostgreSQL.

## Networking

![](../memes/networking.jpeg)

In order for our web app to be able to communicate with the database (in another container!), both must be in the same Docker network.

You can create one with

```shell
docker network create applied-ai-demo-network
```

## Postgres setup

Now let's create our PostgreSQL database container! We can find an [official image in the Docker Hub](https://hub.docker.com/_/postgres), which is also documented there.

```shell
docker run --network applied-ai-demo-network --hostname applied-ai-demo-postgres --env POSTGRES_PASSWORD=mysecretpassword --detach postgres:16
```

We connect it to our previously created network (`--network`, no shorthand!), give it a hostname (`--hostname`, shorthand `-h`) where our todo app can reach it, and set the environment variable (`--env`, shorthand `-e`) for the password.

Note, that we don't include a port mapping. This is only needed when we want to access a container from our host, meaning the computer where Docker runs on.

We could also use `--name` (no shorthand!) to specify the name of the container for Docker, e.g. in the container overview of `docker ps`, as otherwise a random name is selected. This is a different setting than the hostname!

Note, that we use the `--detach` (shorthand `-d`) flag to detach from the container and run it in the background. This gives us the opportunity to do other things in our host terminal.

To see all containers that are currently running[^1], run

```shell
docker ps
```

Here, we should see our PostgreSQL container too!

## Change our app

Now we need to customize our app so that it can interact with the PostgreSQL container.

### Dependency update

To do this, the appropriate dependency for the PostgreSQL package must first be stored in the `requirements.txt`.
We add the following line at the end:

```shell
psycopg2-binary==2.9.9
```

### Establish a connection

Then we need to change our connection string in `line 5` in `app.py` so that we reach the correct database:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mysecretpassword@applied-ai-demo-postgres:5432/postgres'
```

### Remove legacy stuff

Since we want to keep our container (and our environment) clean, we can remove the now unnecessary `data` folder, since our data is stored externally in the PostgreSQL container respectively its volume:

```shell
rm -R ./data
```

### Build'n'run

Finally, we can build our modified container

```shell
docker build -t applied-ai-docker-tutorial:step-4 .
```

and run it:

```shell
docker run --network applied-ai-demo-network -p 5000:5000 applied-ai-docker-tutorial:step-4
```

Tip: Make sure to stop old todo app containers if one was started with the `--detach` flag. Otherwise, it won't work since our port (5000) is still being used.

### Be happy!

![](../memes/it%20worked-squirrel.jpeg)

![](../memes/it-worked.gif)

## Next step(s)

Head over to [bonus 1 (Docker compose)](../bonus-1/README.md) or [bonus 2 (Docker commands)](../bonus-2/README.md) if you want to!

---

[^1]: If you want to get all containers (even the ones that have been previously stopped) you can add the `--all` (shorthand `-a`) flag.
