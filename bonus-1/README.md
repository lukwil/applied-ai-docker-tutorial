# Bonus 1

With every step of our Docker introduction, we have seen that the possibilities are endless, but at the same time the commands are getting longer and longer.

[Docker compose](https://docs.docker.com/compose/) simplifies multi-container Docker applications by defining them in a single file, allowing easy setup, configuration, and orchestration of multiple services. It provides a concise way to manage complex deployments, reducing the need for manual commands.

## File structure

If we take a look into `docker-compose.yml`, we can see the definition of our two services - one for the todo web app and one for the PostgreSQL database. We can provide the same information like image names, ports, environment variables, or volumes, as we would when running via the Docker command itself.

Luckily, all the services in one Docker compose file [are per default in one network](https://docs.docker.com/compose/networking/) which you don't have to provide yourself[^1]. The hostname we needed to provide earlier is simply the name of the service. There are also default values in place, for e.g. the container name itself. But of course, if you wanted to, you could still rename all of those yourself, see also the [compose file documentation](https://docs.docker.com/compose/compose-file/) for that purpose.

## Get stuff running

In the simplest way, given that you have a Docker compose file at hand, you can just type

```shell
docker compose up
```

and all your services in the file will be started.
You may as well apply the `-d` flag as we did for Docker.  
If you do the latter, you can stop all the services at once with

```shell
docker compose down
```

You can also just start specific services from your compose file by running

```shell
docker compose up <service_1> <service_2> ...
```

But bear in mind that you need to be in the folder where the Docker compose file in question resides to run any compose related commands - otherwise, how should Docker (compose) know, which services you want to start or stop? :)

---

[^1]: But you still can provide an external network if needed, e.g. to connect to other services outside your compose file.
