# Environment Variables

The docker image accepts the following environment variables

| Name     | What is it?                                                             | Mandatory?                     |
| -------- | ----------------------------------------------------------------------- | ------------------------------ |
| WEBHOOK  | The url of the discord webhook                                          | Yes                            |
| MESSAGE  | The message to send                                                     | Yes                            |
| USERNAME | The name of the user that shows in discord as the source of the message | No, defaults to 'Notification' |