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

You can deploy this application to your Kubernetes cluster by cloning this repo first and using the helm chart provided in `/flask-chart` to deploy this simple rest api to your kubernetes cluster. After your app is live, you can access the `/health` endpoint to ensure the api is healthy. 

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

7. Once your testing is complete, push the docker image to your favorite container registry. 

8. Edit the container image value in the helm chart and deploy your this application to your kubernetes cluster.

9. Test the helm deployment locally on minikube using:

```bash
helm install <release-name> ./flask-chart
```

You should now see the following pods, services and deployments (_Note_: the helm release name here is "hello-api")

```
11:00:58 PM flask-hello-k8s on 🚀 master [!?] on 🐳 v19.03.8 
➜  kubectl get all
NAME                                           READY   STATUS    RESTARTS   AGE
pod/hello-api-flask-chart-7994d796d8-dqcrj   1/1     Running   0          13m

NAME                              TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
service/hello-api-flask-chart   ClusterIP   10.109.170.75   <none>        80/TCP    13m
service/kubernetes                ClusterIP   10.96.0.1       <none>        443/TCP   3h46m

NAME                                      READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/hello-api-flask-chart   1/1     1            1           13m

NAME                                                 DESIRED   CURRENT   READY   AGE
replicaset.apps/hello-api-flask-chart-7994d796d8   1         1         1       13m
```

## License

This sample application is licensed under the MIT License. 

[MIT License](https://opensource.org/licenses/MIT)

