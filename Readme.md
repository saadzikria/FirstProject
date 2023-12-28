    ~/Desktop/Jazz/Docker Training/DOCKER_IMAGES  docker network create -d bridge my_network                                                                                 ✔  at 16:55:10  
19c030d8b83b62ec4206bd7f8add230823cfd6dd28792361d02ad6938600c6aa
    ~/Desktop/Jazz/Docker Training/DOCKER_IMAGES  docker network inspect my_network                                                                                          ✔  at 16:56:09  
[
    {
        "Name": "my_network",
        "Id": "19c030d8b83b62ec4206bd7f8add230823cfd6dd28792361d02ad6938600c6aa",
        "Created": "2023-12-28T11:56:09.84531351Z",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": {},
            "Config": [
                {
                    "Subnet": "172.22.0.0/16",
                    "Gateway": "172.22.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {},
        "Options": {},
        "Labels": {}
    }
]
    ~/Desktop/Jazz/Docker Training/DOCKER_IMAGES  docker run -d -itd --network=my_network --name nginx_container -p 80:80 nginx:stable-perl                                  ✔  at 16:56:26  
Unable to find image 'nginx:stable-perl' locally
stable-perl: Pulling from library/nginx
b5a0d5c14ba9: Downloading [=================>                                 ]   10.8MB/31.42MB
975b4ec1d253: Downloading [=======>                                           ]  3.925MB/25.6MB
5d968dafb983: Download complete 
8a1ecc36510f: Waiting 
6b66cbffcbde: Waiting 
71608b1f666b: Waiting 
c16d543409bb: Waiting 
^C%                                                                                                                                                                                                  
    ~/Desktop/Jazz/Docker Training/DOCKER_IMAGES  docker images                                                                                              255 ✘  took 8s   at 16:57:56  
REPOSITORY                                        TAG                  IMAGE ID       CREATED         SIZE
docker_images-web                                 latest               f4c2022711a3   9 minutes ago   158MB
<none>                                            <none>               20e0b40471a0   24 hours ago    1.11GB
<none>                                            <none>               cdc5f12d5bc5   25 hours ago    1.11GB
<none>                                            <none>               f2397c5f3dac   25 hours ago    1.11GB
<none>                                            <none>               c279db0ae5e2   25 hours ago    1.11GB
<none>                                            <none>               dc09242279ce   25 hours ago    1.11GB
haxceb/first_image_2                              latest               403b6b10180b   28 hours ago    149MB
first_image                                       latest               403b6b10180b   28 hours ago    149MB
<none>                                            <none>               50f476cf7414   29 hours ago    149MB
redis                                             latest               e40e2763392d   3 weeks ago     138MB
httpd                                             latest               b1866dff9b27   2 months ago    194MB
dev.local/appsody/jazzcash-appsody-stack          0                    f6a1c62258ad   6 months ago    765MB
dev.local/appsody/jazzcash-appsody-stack          0.4                  f6a1c62258ad   6 months ago    765MB
dev.local/appsody/jazzcash-appsody-stack          0.4.8                f6a1c62258ad   6 months ago    765MB
dev.local/appsody/jazzcash-appsody-stack          latest               f6a1c62258ad   6 months ago    765MB
payment-and-transaction-microservice-mockserver   latest               e63c550b2c14   6 months ago    927MB
insurance-microservice-mockserver                 latest               cab9325035d3   6 months ago    927MB
qrpayment-microservice-mockserver                 latest               68d64f72d7aa   6 months ago    927MB
mongo                                             latest               1f4172d24883   6 months ago    653MB
arm64v8/mongo                                     latest               376ea24ce0f0   6 months ago    624MB
nginx                                             stable-perl          0fdb020aeaa7   8 months ago    181MB
mongo                                             4.4.6                61ea24dc52c6   2 years ago     423MB
quay.io/infinispan/server                         10.1.8.Final-1       a0102492fb4e   3 years ago     428MB
appsody/init-controller                           0.3.5                61d9510c1dff   3 years ago     4.36MB
strimzi/kafka                                     0.17.0-kafka-2.4.0   9241736ea27b   3 years ago     558MB
    ~/Desktop/Jazz/Docker Training/DOCKER_IMAGES  docker run -d -itd --network=my_network --name nginx_container -p 80:80 0fdb020aeaa7                                       ✔  at 16:58:03  
Unable to find image '0fdb020aeaa7:latest' locally
^C%                                                                                                                                                                                                  
    ~/Desktop/Jazz/Docker Training/DOCKER_IMAGES  docker run -d -itd --network=my_network --name nginx_container -p 80:80 0fdb020aeaa7                                   255 ✘  at 16:58:19  
Unable to find image '0fdb020aeaa7:latest' locally
^C%                                                                                                                                                                                                  
    ~/Desktop/Jazz/Docker Training/DOCKER_IMAGES  docker run -d -itd --network=my_network --name nginx_container -p 80:80 nginx:latest                                   255 ✘  at 16:59:02  
Unable to find image 'nginx:latest' locally
^C%                                                                                                                                                                                                  
    ~/Desktop/Jazz/Docker Training/DOCKER_IMAGES  docker run -d -itd --network=my_network --name nginx_container -p 80:80 8be9ac03fc30                                   255 ✘  at 17:00:35  
95d984e66f941b9319f680e8eda723bba2f3abd85d7fd2684f1c0accee236add
    ~/Desktop/Jazz/Docker Training/DOCKER_IMAGES  docker run -d -itd --network=my_network --name nginx_container -p 80:80 8be9ac03fc30                                       ✔  at 17:01:14  
docker: Error response from daemon: Conflict. The container name "/nginx_container" is already in use by container "95d984e66f941b9319f680e8eda723bba2f3abd85d7fd2684f1c0accee236add". You have to remove (or rename) that container to be able to reuse that name.
See 'docker run --help'.
    ~/Desktop/Jazz/Docker Training/DOCKER_IMAGES  docker run -d -itd --network=my_network --name httpd_container -p 81:80 b1866dff9b27                                   125 ✘  at 17:01:35  
Unable to find image 'b1866dff9b27:latest' locally
^C%                                                                                                                                                                                                  
    ~/Desktop/Jazz/Docker Training/DOCKER_IMAGES  docker run -d -itd --network=my_network --name httpd_container -p 81:80 b1866dff9b2714b36aa43e16cc64dbd2e0f3334b2e07884ffbb5eb438f458dac
docker: Error response from daemon: image with reference b1866dff9b2714b36aa43e16cc64dbd2e0f3334b2e07884ffbb5eb438f458dac was found but does not match the specified platform: wanted linux/amd64, actual: linux/arm64.
See 'docker run --help'.
    ~/Desktop/Jazz/Docker Training/DOCKER_IMAGES  docker run -d -itd --network=my_network --name httpd_container -p 81:80 b1866dff9b27                                   125 ✘  at 17:02:30  
Unable to find image 'b1866dff9b27:latest' locally
^C%                                                                                                                                                                                                  
    ~/Desktop/Jazz/Docker Training/DOCKER_IMAGES  docker images                                                                                                          255 ✘  at 17:02:58  
REPOSITORY                                        TAG                  IMAGE ID       CREATED          SIZE
docker_images-web                                 latest               f4c2022711a3   15 minutes ago   158MB
<none>                                            <none>               20e0b40471a0   25 hours ago     1.11GB
<none>                                            <none>               cdc5f12d5bc5   25 hours ago     1.11GB
<none>                                            <none>               f2397c5f3dac   25 hours ago     1.11GB
<none>                                            <none>               c279db0ae5e2   25 hours ago     1.11GB
<none>                                            <none>               dc09242279ce   25 hours ago     1.11GB
first_image                                       latest               403b6b10180b   28 hours ago     149MB
haxceb/first_image_2                              latest               403b6b10180b   28 hours ago     149MB
<none>                                            <none>               50f476cf7414   29 hours ago     149MB
redis                                             latest               e40e2763392d   3 weeks ago      138MB
nginx                                             latest               d453dd892d93   2 months ago     187MB
httpd                                             latest               b1866dff9b27   2 months ago     194MB
dev.local/appsody/jazzcash-appsody-stack          0                    f6a1c62258ad   6 months ago     765MB
dev.local/appsody/jazzcash-appsody-stack          0.4                  f6a1c62258ad   6 months ago     765MB
dev.local/appsody/jazzcash-appsody-stack          0.4.8                f6a1c62258ad   6 months ago     765MB
dev.local/appsody/jazzcash-appsody-stack          latest               f6a1c62258ad   6 months ago     765MB
qrpayment-microservice-mockserver                 latest               68d64f72d7aa   6 months ago     927MB
payment-and-transaction-microservice-mockserver   latest               e63c550b2c14   6 months ago     927MB
insurance-microservice-mockserver                 latest               cab9325035d3   6 months ago     927MB
mongo                                             latest               1f4172d24883   6 months ago     653MB
arm64v8/mongo                                     latest               376ea24ce0f0   6 months ago     624MB
nginx                                             stable-perl          8be9ac03fc30   8 months ago     189MB
mongo                                             4.4.6                61ea24dc52c6   2 years ago      423MB
quay.io/infinispan/server                         10.1.8.Final-1       a0102492fb4e   3 years ago      428MB
appsody/init-controller                           0.3.5                61d9510c1dff   3 years ago      4.36MB
strimzi/kafka                                     0.17.0-kafka-2.4.0   9241736ea27b   3 years ago      558MB
    ~/Desktop/Jazz/Docker Training/DOCKER_IMAGES  docker run -d -itd --network=my_network --name httpd_container -p 81:80 d453dd892d93                                       ✔  at 17:03:18  
477e0c22026416a9d63a4d5e92e620d6cda5911ee49dff572a674030964d618b
    ~/Desktop/Jazz/Docker Training/DOCKER_IMAGES  docker run -d -itd --network=my_network --name nginx_container_2 -p 80:80 8be9ac03fc30                                     ✔  at 17:03:32  
b063fad92383d1b057e36591c21e3a1979947459c3c9b696440588002f637d11
docker: Error response from daemon: driver failed programming external connectivity on endpoint nginx_container_2 (be79fe7a765467a7c07b15a805665a0f8399dd5a74599bea1c61639592e86500): Bind for 0.0.0.0:80 failed: port is already allocated.
    ~/Desktop/Jazz/Docker Training/DOCKER_IMAGES  docker run -d -itd --network=my_network --name nginx_container_2 -p 82:80 8be9ac03fc30                                 125 ✘  at 17:05:30  
docker: Error response from daemon: Conflict. The container name "/nginx_container_2" is already in use by container "b063fad92383d1b057e36591c21e3a1979947459c3c9b696440588002f637d11". You have to remove (or rename) that container to be able to reuse that name.
See 'docker run --help'.
    ~/Desktop/Jazz/Docker Training/DOCKER_IMAGES  docker ps -a                                                                                                           125 ✘  at 17:05:38  
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS         PORTS                NAMES
b063fad92383   8be9ac03fc30   "/docker-entrypoint.…"   31 seconds ago   Created                             nginx_container_2
477e0c220264   d453dd892d93   "/docker-entrypoint.…"   2 minutes ago    Up 2 minutes   0.0.0.0:81->80/tcp   httpd_container
95d984e66f94   8be9ac03fc30   "/docker-entrypoint.…"   4 minutes ago    Up 4 minutes   0.0.0.0:80->80/tcp   nginx_container
    ~/Desktop/Jazz/Docker Training/DOCKER_IMAGES  docker stop b063fad92383 477e0c220264 95d984e66f94                                                                         ✔  at 17:06:01  
b063fad92383
477e0c220264
95d984e66f94
    ~/Desktop/Jazz/Docker Training/DOCKER_IMAGES  docker rm b063fad92383 477e0c220264 95d984e66f94                                                                           ✔  at 17:06:33  
b063fad92383
477e0c220264
95d984e66f94
    ~/Desktop/Jazz/Docker Training/DOCKER_IMAGES  docker network rm my_network                                                                                               ✔  at 17:06:49  
my_network
    ~/Desktop/Jazz/Docker Training/DOCKER_IMAGES  npm install pymongo                                                                                                        ✔  at 17:06:57  
npm ERR! code E404
npm ERR! 404 Not Found - GET https://registry.npmjs.org/pymongo - Not found
npm ERR! 404 
npm ERR! 404  'pymongo@*' is not in this registry.
npm ERR! 404 
npm ERR! 404 Note that you can also install from a
npm ERR! 404 tarball, folder, http url, or git url.

    ~/Desktop/Jazz/Docker Training/DOCKER_IMAGES  docker compose up                                                                                                          ✔  at 17:14:55  
[+] Building 47.7s (9/9) FINISHED                                                                                                                                                                    
 => [web internal] load .dockerignore                                                                                                                                                           0.0s
 => => transferring context: 2B                                                                                                                                                                 0.0s
 => [web internal] load build definition from Dockerfile                                                                                                                                        0.0s
 => => transferring dockerfile: 370B                                                                                                                                                            0.0s
 => [web internal] load metadata for docker.io/library/python:3.9.18-slim                                                                                                                       1.2s
 => CACHED [web 1/4] FROM docker.io/library/python:3.9.18-slim@sha256:96be08c44307e781fd9ce8e05b49c969b4cb902ec23594f904739c58da3a09ed                                                          0.0s
 => [web internal] load build context                                                                                                                                                           0.0s
 => => transferring context: 3.46kB                                                                                                                                                             0.0s
 => [web 2/4] COPY requirements.txt requirements.txt                                                                                                                                            0.0s
 => [web 3/4] COPY . .                                                                                                                                                                          0.0s
 => [web 4/4] RUN pip3 install -r requirements.txt                                                                                                                                             46.3s
 => [web] exporting to image                                                                                                                                                                    0.1s
 => => exporting layers                                                                                                                                                                         0.1s
 => => writing image sha256:29f7c152a182e36ac83c8cb17bf2fd19fe47ec184110f56f29e03e0b8f9af444                                                                                                    0.0s 
 => => naming to docker.io/library/docker_images-web                                                                                                                                            0.0s 
[+] Running 3/3                                                                                                                                                                                      
 ✔ Network docker_images_my_network   Created                                                                                                                                                   0.0s 
 ✔ Container docker_images-mongodb-1  Created                                                                                                                                                   0.0s 
 ✔ Container docker_images-web-1      Created                                                                                                                                                   0.0s 
Attaching to docker_images-mongodb-1, docker_images-web-1
docker_images-mongodb-1  | 
docker_images-mongodb-1  | WARNING: MongoDB 5.0+ requires a CPU with AVX support, and your current system does not appear to have that!
docker_images-mongodb-1  |   see https://jira.mongodb.org/browse/SERVER-54407
docker_images-mongodb-1  |   see also https://www.mongodb.com/community/forums/t/mongodb-5-0-cpu-intel-g4650-compatibility/116610/2
docker_images-mongodb-1  |   see also https://github.com/docker-library/mongo/issues/485#issuecomment-891991814
docker_images-mongodb-1  | 
docker_images-web-1 exited with code 0
docker_images-web-1 exited with code 0
docker_images-web-1 exited with code 0
^CGracefully stopping... (press Ctrl+C again to force)
Aborting on container exit...
[+] Stopping 2/2
 ✔ Container docker_images-web-1      Stopped                                                                                                                                                   0.0s 
 ✔ Container docker_images-mongodb-1  Stopped                                                                                                                                                  10.2s 
canceled
    ~/Desktop/Jazz/Docker Training/DOCKER_IMAGES  docker compose up                                                                                      INT ✘  took 4m 59s   at 17:20:23  
[+] Building 85.6s (10/10) FINISHED                                                                                                                                                                  
 => [web internal] load build definition from Dockerfile                                                                                                                                        0.0s
 => => transferring dockerfile: 370B                                                                                                                                                            0.0s
 => [web internal] load .dockerignore                                                                                                                                                           0.0s
 => => transferring context: 2B                                                                                                                                                                 0.0s
 => [web internal] load metadata for docker.io/library/python:3.9.18-slim                                                                                                                       3.3s
 => [web auth] library/python:pull token for registry-1.docker.io                                                                                                                               0.0s
 => [web 1/4] FROM docker.io/library/python:3.9.18-slim@sha256:96be08c44307e781fd9ce8e05b49c969b4cb902ec23594f904739c58da3a09ed                                                                 0.0s
 => [web internal] load build context                                                                                                                                                           0.0s
 => => transferring context: 3.04kB                                                                                                                                                             0.0s
 => CACHED [web 2/4] COPY requirements.txt requirements.txt                                                                                                                                     0.0s
 => [web 3/4] COPY . .                                                                                                                                                                          0.0s
 => [web 4/4] RUN pip3 install -r requirements.txt                                                                                                                                             82.1s
 => [web] exporting to image                                                                                                                                                                    0.1s 
 => => exporting layers                                                                                                                                                                         0.1s 
 => => writing image sha256:cb2141b22679dfbe4cdcfb987b5cf8f5ab35c62d401386f7ace9afd008b793d9                                                                                                    0.0s 
 => => naming to docker.io/library/docker_images-web                                                                                                                                            0.0s 
[+] Running 3/3                                                                                                                                                                                      
 ✔ Network docker_images_my_network   Created                                                                                                                                                   0.0s 
 ✔ Container docker_images-mongodb-1  Created                                                                                                                                                   0.1s 
 ✔ Container docker_images-web-1      Created                                                                                                                                                   0.0s 
Attaching to docker_images-mongodb-1, docker_images-web-1
docker_images-mongodb-1  | 
docker_images-mongodb-1  | WARNING: MongoDB 5.0+ requires a CPU with AVX support, and your current system does not appear to have that!
docker_images-mongodb-1  |   see https://jira.mongodb.org/browse/SERVER-54407
docker_images-mongodb-1  |   see also https://www.mongodb.com/community/forums/t/mongodb-5-0-cpu-intel-g4650-compatibility/116610/2
docker_images-mongodb-1  |   see also https://github.com/docker-library/mongo/issues/485#issuecomment-891991814
docker_images-mongodb-1  | 
docker_images-web-1      | INFO:     Started server process [1]
docker_images-web-1      | INFO:     Waiting for application startup.
docker_images-web-1      | INFO:     Application startup complete.
docker_images-web-1      | INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)
docker_images-web-1      | INFO:     172.26.0.1:34066 - "GET / HTTP/1.1" 200 OK
docker_images-web-1      | INFO:     172.26.0.1:34066 - "GET / HTTP/1.1" 200 OK
docker_images-web-1      | INFO:     172.26.0.1:32906 - "GET / HTTP/1.1" 200 OK

