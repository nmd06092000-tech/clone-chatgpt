export interface Conversation {
  id: number;
  title: string;
}

export interface Message {
  id: number;
  role: "user" | "assistant";
  content: string;
}

export interface Model {
  id: string;
  name: string;
}