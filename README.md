# ChatGPT UI Clone

This project is a ChatGPT-style chat interface built with Vue 3, TypeScript, Vite, and Tailwind CSS. The app includes a default empty state when there are no messages, a chat composer, a sidebar conversation area, and a New chat button that resets the interface back to the default state.

## Tech Stack

- Vue 3
- TypeScript
- Vite
- Tailwind CSS
- Axios
- FastAPI backend
- PostgreSQL
- Docker Compose

## Project Structure

```txt
clone-chatgpt/
├── backend/        # Backend API
├── frontend/       # Vue frontend
├── docker-compose.yml
└── README.md
```

## Frontend Setup

Move into the frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

## Run Frontend

Inside the `frontend` directory, run:

```bash
npm run dev
```

Then open the URL shown by Vite in the terminal, usually:

```txt
http://localhost:5173
```

## Run Backend And Database

If you need to run the backend with PostgreSQL, run this command from the project root:

```bash
docker compose up --build
```

The backend will be available at:

```txt
http://localhost:8000
```

## How To Use The App

When the app first opens, there are no messages yet, so it displays the default empty state:

- The title is centered on the screen
- The chat composer appears below the title
- The sidebar appears on the left

To send a message:

1. Type your message in the chat composer.
2. Press Enter or click the send button.
3. The message will be added to the chat list.
4. Once messages exist, the chat composer moves to the bottom of the screen like a normal chat interface.

To start a new chat:

1. Click the `New chat` button in the sidebar or header.
2. The app resets the current message list.
3. The screen returns to the default state with the title and composer centered.

## Main UI Flow

The main chat UI is based on the number of messages:

```txt
messages.length === 0  -> show the default empty state
messages.length > 0    -> show the message list
```

When the user clicks `New chat`, the app resets:

```ts
messages = [];
```

After the reset, Vue automatically renders the default interface again.

## Production Build

Inside the `frontend` directory, run:

```bash
npm run build
```

Preview the production build:

```bash
npm run preview
```
