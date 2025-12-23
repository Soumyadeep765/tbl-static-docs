# Webhook Instance

The **Webhook instance** is used to generate **secure webhook URLs** for your bot.

These URLs allow **external sources**—such as websites, APIs, or dashboards—to **trigger bot commands directly**.

Each webhook URL is protected using **cryptographic signatures**, ensuring that only valid and authorized requests can execute commands.

This is useful when you want:

- Website → bot interactions
- API-driven bot actions
- Secure external triggers
- Automation without exposing bot tokens

Webhook-triggered commands behave like normal TBL commands, but are executed through a secure HTTP endpoint.
