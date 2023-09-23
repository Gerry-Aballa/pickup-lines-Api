# An API that returns a random pickup line

[Test this API](http://ec2-3-7-73-121.ap-south-1.compute.amazonaws.com:8000/docs)


## Introduction

Welcome to the Random Lines API! This API allows you to retrieve random lines of text for various purposes. It's a simple and straightforward service that you can use in your applications or scripts.

## Base URL

The base URL for the API is:

```
http://ec2-3-7-73-121.ap-south-1.compute.amazonaws.com:8000
```

## Endpoint

To get a random pickup line make a GET request to the following endpoint:

```
/lines/random
```

## Usage

### Making a Request

You can use any HTTP client library or tool to make a GET request to the API endpoint. Here's an example using `curl` in the command line:

```bash
curl http://ec2-3-7-73-121.ap-south-1.compute.amazonaws.com:8000/lines/random
```

### Response

The API will respond with a JSON object containing the random line of text. An example response looks like this:

```json
{
  "mood": "Flirty",
  "pickupline": "Did you invent the airplane? Because you are clearly Mr. Wright.",
  "id": 107
}
```

### Error Handling

If there is an issue with your request, the API will respond with an error message in JSON format. For example:

```json
{
  "detail": "No pickuplines found."
}
```

## Rate Limiting

Please note that this API may have rate limiting in place to prevent abuse. If you encounter rate limiting, you may need to wait for some time before making additional requests.

## Conclusion

That's it! You now know how to use the Random Lines API. Feel free to integrate it into your projects, applications, or scripts as needed and add it to the list below at will.

- [pickuplines.py](twitter.com)
