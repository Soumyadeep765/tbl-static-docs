# Command Structure in TBL

On TeleBotHost, your entire bot is built out of **commands**. You don't have to write HTTP routers, register event listeners, or keep servers alive. Instead, you define commands in the dashboard. When a user sends a message, TBL matches it to a command, runs it, and finishes.

One update in, one execution path out. Simple, stable, and clean.

---

## What a Command Contains

In the dashboard editor, every command has a few key properties that control its behavior:

| Part | What it does | When to use it |
| --- | --- | --- |
| **Command** | The unique trigger name (e.g. `/start`, `Help`, `*`) | Always. This is how TBL matches incoming messages to your code. |
| **Answer** | A static text message sent automatically to the user | For simple text replies. It is sent *before* any logic runs. |
| **Keyboard** | Buttons shown below the message input field | To guide users (e.g. `Help, About`). Requires an Answer to be sent. |
| **Logic** | The JavaScript code executed inside the VM sandbox | For dynamic behaviors (database saves, external API calls). |
| **Aliases** | Alternative trigger names (e.g. `help, /h`) | To map multiple button taps or typos to a single command. |

---

## How `@` Shares Variables and Configs

The **`@`** command is a special hook that runs automatically **before** any other command on every update. But it is not just for rate limits or auth checks—it is also your global configuration center!

### The Combined Scope

When an update arrives, TBL compiles your code by concatenating your `@` initialization logic, your matched command's logic, and your `@@` post-processor logic **inside a single asynchronous block**:

```js
(async () => {
  // 1. @ Initialization logic runs first
  const adminId = 123456789;
  const userProfile = await db.user.get("profile");

  // 2. Your matched command logic runs second
  Bot.sendMessage("Hello, " + userProfile.name);

  // 3. @@ Post-processor logic runs last
  // ...
})();
```

Because all three sections run inside the **same function scope**, any variables you declare in `@` (using `const`, `let`, or `var`) are **immediately shared and accessible** inside your matched command and your `@@` code!

### Example: Loading Global Configurations

You can load values once in `@` and use them anywhere:

```js
// 1. Inside the Logic field of your `@` command:
const config = {
  maintenance: false,
  version: "1.2.0"
};

const userSession = await db.user.get("session") || { steps: 0 };
```

```js
// 2. Inside the Logic field of your `/status` command:
// You can read `config` and `userSession` directly!
if (config.maintenance) {
  Bot.sendMessage("Under maintenance. Back soon!");
} else {
  Bot.sendMessage("Version: " + config.version);
}
```

This makes sharing settings, cached database records, and utility states across all commands incredibly easy, clean, and completely eliminates redundant code!

---

## Next Steps in Command Flow

Now that you know how a command is structured, let's look at the fields you can use in the editor:

➔ **[Command Fields](command-fields.md)**
