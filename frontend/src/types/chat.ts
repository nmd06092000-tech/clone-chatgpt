export type MessageRole = "user" | "assistant" | "system";

export interface Message {
  id: string;
  conversation_id: string;
  role: MessageRole;
  content: string;
  sequence_no: number;
  created_at: string;
}

export interface Conversation {
  id: string;
  user_id: string;
  ai_mode_id: string;
  title: string;
  last_message_at?: string | null;
  created_at: string;
  updated_at: string;
  messages: Message[];
}

export interface User {
  id: string;
  display_name: string;
  email: string;
  created_at: string;
  updated_at: string;
}

export interface AiMode {
  id: string;
  key: string;
  display_name: string;
}