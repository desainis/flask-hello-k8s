#### Introduction

#### Before you begin

#### Authorization

#### API endpoint
Use the following API endpoint for all of your API requests:

https://some-real-url.com/v1/

#### Versioning
The API is versioned to support the different infrastructure providers that are available for you to create clusters. All /v1 APIs can be used to work only with IBM Cloud classic infrastructure. To work with a cluster that was provisioned on IBM Virtual Private Cloud (VPC) infrastructure, you must use the /v2 API.

For information about the API versions, see About the API.

#### Error handling
This API uses standard HTTP response codes to indicate whether a method completed successfully. A 200 response indicates success. A 400 type response is some sort of failure, and a 500 type response usually indicates an internal system error. (_Note:_ Not every HTTP status code is used)

HTTP error code | Description | Recovery
-- | -- | --
200	| Success | The request was successful.
400	| Bad Request |	The input parameters in the request body are either incomplete or in the wrong format. Be sure to include all required parameters in your request.
401	| Unauthorized | You are not authorized to make this request. Log in to IBM Cloud and try again. If this error persists, contact the account owner to check your permissions.
403	| Forbidden | The supplied authentication is not authorized to access the cluster or an associated cluster resource. Check that you have the correct access credentials and permissions.
404	| Not Found | The requested resource could not be found.
408	| Request Timeout |	The connection to the server timed out. Wait a few minutes, then try again.
409	| Conflict | The cluster or an associated cluster resource with the same name or ID already exists.
500	| Internal Server Error | Your request could not be processed. Please wait a few minutes and try again.

#### Methods
- Request a health check for this API (use this as an indicator to know if the API is healthy). 
  - GET `/v1/health`

##### Request

- This method does not accept any request parameters.

##### Response

Field Name | Field Type | Example
-- | -- | --
message | string | UP
status_code | int | 200

```json
{
  "message": "UP", 
  "status_code": 200
}
```

___

- Request a "Hello World" message
  - GET `/v1/will`

##### Request

- This method does not accept any request parameters.

##### Response

Field Name | Field Type | Example
-- | -- | --
message | string | Hello World
status_code | int | 200

```json
{
  "message": "Hello World", 
  "status_code": 200
}
```

___

- Request a "It works!" message
  - GET `/v1/ready`

##### Request

- This method does not accept any request parameters.

##### Response

Field Name | Field Type | Example
-- | -- | --
message | string | It works!
status_code | int | 200

```json
{
  "message": "It works!", 
  "status_code": 200
}
```