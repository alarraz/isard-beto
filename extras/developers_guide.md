# Dockers and debug
## Docker-compose

To develop with docker-compose you can run docker-compose with two or more files .yml
In docker-compose.devel.yml you have your ./src mapped in isard-app and isard-hypervisor not run.

You can add devel-custom.yml with other options. For example, if you want tu run hypervisor and add 
extra volumes for ipython profile:
```yaml
version: "3.5"
services:
  isard-hypervisor:
    image: isard/hypervisor:${TAG}
  isard-app:
    volumes:
      ##### - only devel - ############################
      - "/opt/ipython_profile_default:/root/.ipython/profile_default"
``` 

If you want only one docker-compose file you can show the result .yml with order config

    docker-compose -f docker-compose.yml -f docker-compose.devel.yml -f devel-custom.yml config > debug.yml
    
To run your dockers:

    docker-compose -f docker-compose.yml -f docker-compose.devel.yml -f devel-custom.yml up -d

## Debug with ipython

If container isard-app-devel is running:

    docker exec -ti isard-app-devel bash -c "cd /isard/engine2 && ipython3"
   
    
## Debug with pycharm

Create a debug.yaml:

    docker-compose -f docker-compose.yml -f docker-compose.devel.yml -f devel-custom.yml config > debug.yml

Define interpreter:

        menu File 
          --> Settings 
            --> Project Interpreter 
              --> click in gear icon
                --> Add
                  - Type: docker-compose
                  - Name: Remote IsardApp Devel 
                  - Server: Docker
                  - Configuration file: ./debug.yml
                  - Service: isard-app
                  - Python interpreter path: python3
                  
Debug: 

If you want to debug for example engine.py

        menu Run 
          --> Edit configurations... 
            --> Add new configuration:
                  - Select type: Python
            --> Fill options:
                  - Name: engine.py in isard-app
                  - Script path:       /path_to_local_isard_repo/src/engine2/core/engine.py
                  - Working direcotry: /path_to_local_isard_repo/src/engine2
                  - Path mappings:     /path_to_local_isard_repo/src=/isard
                  
Then Shift + F9 to debug
             
                  
