# 1) Base image: official MySQL 8.0
FROM mysql:8.0

# 2) Set environment variables for first-time initialization
ENV MYSQL_ROOT_PASSWORD=rootpass \
    MYSQL_DATABASE=UD_db \
    MYSQL_USER=UD_admin \
    MYSQL_PASSWORD=UD_PWD

# 3) Expose MySQL port
EXPOSE 3306

# 4) (Optional) Copy initialization scripts into the container
#    Any .sql/.sh in this folder runs on first start.
# COPY ./init-scripts/ /docker-entrypoint-initdb.d/

# 5) Default CMD is baked into the mysql image (starts mysqld)


