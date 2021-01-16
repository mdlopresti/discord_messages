![Docker Image CI](https://github.com/mdlopresti/scheduled_discord_messages/workflows/Docker%20Image%20CI/badge.svg)

# Scheduled Discord Messages

A discord notification bot/learn docker/github actions project.  Currrently this process is working via [scheduled github actions](https://github.com/mdlopresti/scheduled_discord_messages/actions?query=workflow%3A%22scheduled+message+sending%22).  

## Goals

#### ~~MVP~~ Done!

1. ~~Automatically send out notifications to discord server channels~~ Done!
2. ~~Use Docker for the runtime environment~~ Done!
3. ~~Use GitHub Actions to run the container~~ Done!

## Environment Variables

The docker image accepts the following environment variables

| Name     | What is it?                                                             | Mandatory?                     |
| -------- | ----------------------------------------------------------------------- | ------------------------------ |
| WEBHOOK  | The url of the discord webhook                                          | Yes                            |
| MESSAGE  | The message to send                                                     | Yes                            |
| USERNAME | The name of the user that shows in discord as the source of the message | No, defaults to 'Notification' |
