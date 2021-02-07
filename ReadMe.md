# Scheduled Discord Messages

![Docker Image CI](https://github.com/mdlopresti/scheduled_discord_messages/workflows/Docker%20Image%20CI/badge.svg) [![Find on DockerHub](https://img.shields.io/badge/On%20DockerHub%3F-Yup-green)](https://hub.docker.com/layers/mdlopresti/scheduled_discord_messages)

A discord notification bot project.  Currently this process is working via [scheduled github actions](https://github.com/mdlopresti/scheduled_discord_messages/actions?query=workflow%3A%22scheduled+message+sending%22).  

The tech used in this project was selected as a learning project, it is definitely not the best approach to take but it is a good enough excuse to learn the tech.

## Docker Tags

- notifier
  - a generic docker image capable of sending a discord message to a server via a web hook, no internal logic
- specific
  - a specialized version for my specific needs, shifts logic out of github actions

## Goals

### ~~MVP using CI~~ Done! [See MVP tag](https://github.com/mdlopresti/scheduled_discord_messages/releases/tag/MVP)

1. ~~Automatically send out notifications to discord server channels~~
2. ~~Use Docker for the runtime environment~~
3. ~~Use GitHub Actions to run the container~~

### Improvements

1. ~~Push container image into repo instead of building each time~~
2. Remove as much logic as possible from [Github Actions](https://github.com/mdlopresti/scheduled_discord_messages/blob/master/.github/workflows/scheduled-messages.yml)

### Kubernetes

It is time to learn some Kubernetes.  Goal here is to shift from using Github Actions to run the containerized notification process and into Kubernetes.

1. Create kubernetes job definition
    1. Should assign Environment variables via configMaps/secrets

## Other Documentation

- [Environment Variables for Container](docs/Environment_Variables.md)
