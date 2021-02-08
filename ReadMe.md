# Scheduled Discord Messages

[![Find on DockerHub](https://img.shields.io/badge/On%20DockerHub%3F-Yup-green)](https://hub.docker.com/r/mdlopresti/discord_messages)

A discord notification bot project.  Currently this process is working via [scheduled github actions](https://github.com/mdlopresti/discord_messages/actions?query=workflow%3A%22scheduled+message+sending%22).  

The tech used in this project was selected as a learning project, it is definitely not the best approach to take but it is a good enough excuse to learn the tech.

## Docker Tags

| Tag      | Description                                                                                               | Build Status                                                                                             |
| -------- | --------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| notifier | a generic docker image capable of sending a discord message to a server via a web hook, no internal logic | ![CI](https://github.com/mdlopresti/discord_messages/workflows/Docker%20Image%20Notifier%20CI/badge.svg) |
| specific | a specialized version for my specific needs, shifts logic out of github actions                           | ![CI](https://github.com/mdlopresti/discord_messages/workflows/Docker%20Image%20Specific%20CI/badge.svg) |

## Other Documentation

- [Environment Variables for Container](https://github.com/mdlopresti/discord_messages/blob/master/docs/Environment_Variables.md)
- [Goals](https://github.com/mdlopresti/discord_messages/blob/master/docs/Goals.md)
