/**
 * Minimal browser/server-side chatbot API client.
 * The API URL is intentionally supplied by the caller.
 */

export async function sendMessage(apiUrl, message, conversationId) {
  if (!apiUrl || !message?.trim()) {
    throw new Error("apiUrl and message are required");
  }

  const response = await fetch(apiUrl, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      conversation_id: conversationId ?? null,
      message: message.trim(),
    }),
  });

  if (!response.ok) {
    throw new Error(`chatbot request failed: HTTP ${response.status}`);
  }

  return response.json();
}
