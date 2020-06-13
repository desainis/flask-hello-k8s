![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)
![technical-debut](https://forthebadge.com/images/badges/contains-technical-debt.svg)
![didnt-ask](https://forthebadge.com/images/badges/you-didnt-ask-for-this.svg)

___

```
 _________________________________________
/ He who steps on others to reach the top \
\ has good balance.                       /
 -----------------------------------------
          \
           \
            \          __---__
                    _-       /--______
               __--( /     \ )XXXXXXXXXXX\v.
             .-XXX(   O   O  )XXXXXXXXXXXXXXX-
            /XXX(       U     )        XXXXXXX\
          /XXXXX(              )--_  XXXXXXXXXXX\
         /XXXXX/ (      O     )   XXXXXX   \XXXXX\
         XXXXX/   /            XXXXXX   \__ \XXXXX
         XXXXXX__/          XXXXXX         \__---->
 ---___  XXX__/          XXXXXX      \__         /
   \-  --__/   ___/\  XXXXXX            /  ___--/=
    \-\    ___/    XXXXXX              '--- XXXXXX
       \-\/XXX\ XXXXXX                      /XXXXX
         \XXXXXXXXX   \                    /XXXXX/
          \XXXXXX      >                 _/XXXXX/
            \XXXXX--__/              __-- XXXX/
             -XXXXXXXX---------------  XXXXXX-
                \XXXXXXXXXXXXXXXXXXXXXXXXXX/
                  ""VXXXXXXXXXXXXXXXXXXV""
```

___
# Flask Hello World in K8s
A simple RESTful api written using Flask with a simple path to production deployment. 

## API Specifications

See [api specification](docs/hello-api.md) for further details. 

## Steps

You can deploy this application to your Kubernetes cluster by cloning this repo first and using the helm chart provided in `/helm` to deploy this simple rest api to your kubernetes cluster. After your app is live, you can access the `/health` endpoint to ensure the api is healthy. 

### Deploying to Kubernetes cluster

#### Native application development

1. Install [Python](https://www.python.org/downloads/)
2. Install all required dependencies `pip3 install -r requirements.txt`

3. To run your application locally:

```bash
python3 hello.py livereload # live reload will save you the hassle of reloading on code changes.
```

4. To run all unit tests:

```bash
python3 -m unittest tests/*.py
```

5. Use the `build.sh` to build the docker image

6. Use the `run.sh` to run a local docker container based on the image in step 4. (Optionally use your own)

_Note:_ All test cases should be included in the `tests/` folder.

## License

This sample application is licensed under the MIT License. 

[MIT License](https://opensource.org/licenses/MIT)

