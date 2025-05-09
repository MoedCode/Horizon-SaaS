
# Prerequisite: Docker Daemon Running in WSL2
```sh
# Start Docker manually in WSL2 (if you haven't already):
sudo dockerd --host=unix:///var/run/docker.sock \
             --storage-driver=vfs &> ~/dockerd.log &

# Give it a few seconds, then verify:
docker version
docker info


```
# 0- create docker image for mysqlDB
```sh
Thought for a couple of seconds


Here’s a complete A→Z walkthrough for creating and running a Dockerized MySQL container named `ud_db_cont` in your WSL2 Ubuntu—every step explained, with the exact commands you’ll run.

---

## 📋 Prerequisites

* **Docker Engine** running in WSL2 (you’ve already verified with `docker info`).
* A **WSL2 Ubuntu** shell open.

---

## 1. Create a Working Directory

**Why:** Keep your Docker artifacts (Dockerfile, init scripts) neatly contained.

```bash
cd ~/Coding/Graduation/Horizon-SaaS
mkdir mysql-docker
cd mysql-docker
```

---

## 2. Write the `Dockerfile`

**Why:** This declares your image’s base, configuration, and startup behavior.

Create a file named `Dockerfile` (no extension):

```bash
cat > Dockerfile << 'EOF'
# 1) Base image: official MySQL 8.0
FROM mysql:8.0

# 2) Set environment variables for first-time initialization
ENV MYSQL_ROOT_PASSWORD=rootpass \
    MYSQL_DATABASE=UD_PWD \
    MYSQL_USER=UD_admin \
    MYSQL_PASSWORD=ud_password

# 3) Expose MySQL port
EXPOSE 3306

# 4) (Optional) Copy initialization scripts into the container
#    Any .sql/.sh in this folder runs on first start.
# COPY ./init-scripts/ /docker-entrypoint-initdb.d/

# 5) Default CMD is baked into the mysql image (starts mysqld)
EOF
```

> **Breakdown:**
>
> * `FROM mysql:8.0` → use the official, pre-configured MySQL image.
> * `ENV …` → tells MySQL on first boot how to set up root/user/database.
> * `EXPOSE 3306` → documents that the container listens on port 3306.
> * `COPY` (commented) → shows how to include custom SQL scripts if you need them.

---

## 3. Build the Image

**Why:** Converts your Dockerfile into a reusable image you can run anywhere.

```bash
docker build -t ud_db_cont .
```

* `-t ud_db_cont` → tags the new image as `ud_db_cont`.
* `.` → context is the current folder (containing Dockerfile).

---

## 4. Create a Persistent Data Volume

**Why:** So your databases survive container restarts or rebuilds.

```bash
mkdir -p ~/mysql-data
```

This directory on WSL maps to MySQL’s data directory inside the container.

---

## 5. Run the MySQL Container

**Why:** Launches a live MySQL server instance from your image.

```bash
docker run -d \
  --name ud_db_cont \
  -e MYSQL_ROOT_PASSWORD=rootpass \
  -e MYSQL_DATABASE=UD_PWD \
  -e MYSQL_USER=UD_admin \
  -e MYSQL_PASSWORD=ud_password \
  -v ~/mysql-data:/var/lib/mysql \
  -p 3306:3306 \
  ud_db_cont
```

* `-d` → detached (background).
* `--name ud_db_cont` → container name.
* `-e …` → repeat the init variables (ensures idempotence).
* `-v ~/mysql-data:/var/lib/mysql` → mounts your WSL folder as the container’s data directory.
* `-p 3306:3306` → exposes port 3306 on your WSL localhost.

---

## 6. Verify & Connect

1. **Check it’s running**

   ```bash
   docker ps
   ```
2. **View logs**

   ```bash
   docker logs -f ud_db_cont
   ```
3. **Connect with MySQL client**

   ```bash
   mysql -h 127.0.0.1 -P 3306 -u UD_admin -pud_password UD_PWD
   ```

If you see the MySQL prompt, you’re in!

---

## 7. Cleanup (when you’re done)

**Why:** Keep your system tidy.

```bash
docker stop ud_db_cont
docker rm ud_db_cont
docker rmi ud_db_cont
```

Your `~/mysql-data` remains untouched, so you can start a new container on the same data whenever you like.

---

🎉 You now have a fully self-contained MySQL server running in Docker on WSL2, just like a cloud instance—portable, reproducible, and isolated.


```
```

# 1- run  docker commands
```sh
docker run -d \
  --name ud_db_cont \
  -p 5005:3306 \
  -e MYSQL_ROOT_PASSWORD=rootpass \
  -e MYSQL_DATABASE=UD_db \
  -e MYSQL_USER=UD_admin \
  -e MYSQL_PASSWORD=UD_PWD \
  ud_db_cont
```
# 2- docker interactive shell
```sh
docker exec -it ud_db_cont bash
```

✅ Step-by-Step: Change Exposed Port from 3306 → 3307
🔁 1. Stop and Remove the Old Container
```sh
docker stop ud_db_cont
docker rm ud_db_cont

```