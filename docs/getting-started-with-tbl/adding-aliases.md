# Using Aliases in Your Bot

Aliases allow a single command to be triggered using **multiple names**.  
They make bots more flexible and easier to use.

## What is an Alias?

An alias is an alternative trigger for a command.

This means:

- One command
- Multiple triggers
- Same behavior every time

## Why Aliases Are Useful

Aliases help you:

- Support different typing styles
- Match keyboard button text
- Provide short and long command names
- Reduce user mistakes

They improve usability without adding logic.

## Where Aliases Are Used

Aliases are defined inside a command’s configuration.

When a message arrives, TBL checks:

- The command name
- Then its aliases
- Then other matching rules

Aliases behave exactly like the main command.

## Adding Aliases to a Command

Open an existing command and add values in the **Aliases** field.

Each alias is treated as a separate trigger for the same command.

!!! note
    Aliases are **case-sensitive**.  
    `Help`, `help`, and `HELP` are treated as different triggers.

If you want to support multiple cases, you must add each variation as a separate alias.

## Aliases and Keyboards

Aliases work perfectly with keyboards.

For example:

- A keyboard button labeled `Help`
- An alias named `Help`

Both trigger the same command.

!!! tip
    Always add an alias that exactly matches your keyboard button text.

## Best Practices for Aliases

Follow these guidelines:

- Keep aliases short and clear
- Match keyboard labels exactly
- Avoid overlapping aliases across commands
- Add only meaningful alternatives

!!! tip
    Fewer, well-chosen aliases are better than many confusing ones.

## Common Mistakes to Avoid

Avoid:

- Using the same alias in multiple commands
- Adding unrelated words as aliases
- Forgetting case variations when needed

Aliases should always point clearly to one command.

## Test Your Aliases

After adding aliases:

- Open your bot in Telegram
- Try typing different alias forms
- Tap keyboard buttons
- Confirm they all trigger the same response

If everything works, your aliases are set up correctly.

## What You Learned

With aliases, you now know how to:

- Trigger one command in multiple ways
- Connect keyboards and text input
- Improve usability without logic
