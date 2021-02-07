# Environment Variables

## notifier tag

The notifier tagged docker image accepts the following environment variables

| Name     | What is it?                                                             | Mandatory?                     |
| -------- | ----------------------------------------------------------------------- | ------------------------------ |
| WEBHOOK  | The url of the discord webhook                                          | Yes                            |
| MESSAGE  | The message to send                                                     | Yes                            |
| USERNAME | The name of the user that shows in discord as the source of the message | No, defaults to 'Notification' |

## specific tag

The specific tagged docker image accepts the following environment variables

| Name      | What is it?                                                             | Mandatory?                     |
| --------- | ----------------------------------------------------------------------- | ------------------------------ |
| WEBHOOK   | The url of the discord webhook                                          | Yes                            |
| NEXT_DATE | The next scheduled session in 'year month_number day_number format      | Yes                            |
| NEXT_TIME | The next time a session happens, used in message sent                   | Yes                            |
| USERNAME  | The name of the user that shows in discord as the source of the message | No, defaults to 'Notification' |
