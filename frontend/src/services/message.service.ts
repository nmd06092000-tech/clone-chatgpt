import { api } from "./api";

const API_BASE = import.meta.env.VITE_API_BASE ?? "http://localhost:8000";

/** ====== Types ====== */
export type Role = "user" | "assistant" | "system";

export type Message = {
  id: string;
  conversation_id: string;
  role: Role;
  content: string;
  sequence_no: number;
  created_at?: string;
};

/** NDJSON streaming event */
type StreamEvent =
  | { type: "meta"; conversation_id?: string; message_id?: string }
  | { type: "delta"; text: string }
  | { type: "done" }
  | { type: "error"; message: string };

/** ====== CRUD (DB) ====== */

// Lấy messages của 1 conversation (dùng cho load lịch sử)
export async function listMessages(conversationId: string): Promise<Message[]> {
  const res = await api.get(`/messages/${conversationId}`);
  return res.data;
}

// Tạo message và lưu DB (cần backend có POST /messages)
export async function createMessage(payload: {
  conversation_id: string;
  role?: Role;
  content: string;
}): Promise<Message> {
  const res = await api.post("/messages", payload);
  return res.data;
}

/** ====== Streaming (AI reply) ======
 *  Backend phải có POST /api/chat/stream trả NDJSON theo dòng \n
 */
export async function streamAssistantReply(params: {
  // nếu backend bạn yêu cầu conversation_id thì thêm vào đây (khuyến nghị)
  conversation_id?: string;

  message: string;
  onDelta: (t: string) => void;
  onDone?: () => void;
  onError?: (msg: string) => void;
}) {
  const res = await fetch(`${API_BASE}/api/chat/stream`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    credentials: "include",
    body: JSON.stringify({
      message: params.message,
      ...(params.conversation_id ? { conversation_id: params.conversation_id } : {}),
    }),
  });

  if (!res.ok || !res.body) {
    params.onError?.(await res.text());
    return;
  }

  const reader = res.body.getReader();
  const decoder = new TextDecoder("utf-8");
  let buf = "";

  while (true) {
    const { value, done } = await reader.read();
    if (done) break;

    buf += decoder.decode(value, { stream: true });

    let idx: number;
    while ((idx = buf.indexOf("\n")) >= 0) {
      const line = buf.slice(0, idx).trim();
      buf = buf.slice(idx + 1);
      if (!line) continue;

      let evt: StreamEvent | null = null;
      try {
        evt = JSON.parse(line);
      } catch {
        continue;
      }
      if (!evt) continue;

      if (evt.type === "delta") params.onDelta(evt.text ?? "");
      else if (evt.type === "done") params.onDone?.();
      else if (evt.type === "error") params.onError?.(evt.message ?? "Unknown error");
    }
  }
}