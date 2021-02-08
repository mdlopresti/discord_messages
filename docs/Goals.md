# Goals

## ~~MVP using CI~~ Done! [See MVP tag](https://github.com/mdlopresti/discord_messages/releases/tag/MVP)

1. ~~Automatically send out notifications to discord server channels~~
2. ~~Use Docker for the runtime environment~~
3. ~~Use GitHub Actions to run the container~~

## Improvements

1. ~~Push container image into repo instead of building each time~~
2. ~~Remove message logic from [Github Actions](https://github.com/mdlopresti/discord_messages/blob/master/.github/workflows/scheduled-messages.yml)~~
3. Remove which week is which logic from [Github Actions](https://github.com/mdlopresti/discord_messages/blob/master/.github/workflows/scheduled-messages.yml)

## Github Actions

Convert [container image](https://hub.docker.com/layers/mdlopresti/discord_messages/) into github action.  [doc link for later](https://docs.github.com/en/actions/creating-actions/creating-a-docker-container-action)

## Kubernetes

1. Create kubernetes job definition
  1. Should assign Environment variables via configMaps/secrets