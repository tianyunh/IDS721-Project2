# IDS721-Project2: Kubernetes based Continuous Delivery

[![Python 3.8](https://github.com/tianyunh/IDS721-Project2/actions/workflows/main.yml/badge.svg)](https://github.com/tianyunh/IDS721-Project2/actions/workflows/main.yml)

## Get Related Artists of a given artist on Spotify
This is a containerized fastAPI microservice that can search for an artist on Spotify and return all the artists similar to the identified artist as the output.

## Instructions
1. The service is deployed through Amazon ECS on [this link](http://project2-fargate-alb-748770289.us-east-2.elb.amazonaws.com/)
2. Type `\getRelatedArtists\` followed by the artist name you want to search after the address above
3. It will return all the artists similar to the input artist if the input name is valid and can be found on Spotify

## Techniques Used
- FastAPI
- Create a Dockerfile
- Push Docker Image to Amazon ECR
- Deploy through Amazon ECS
